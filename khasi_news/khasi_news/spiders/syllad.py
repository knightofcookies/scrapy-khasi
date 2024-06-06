from typing import List
import scrapy
from khasi_news.items import KhasiNewsItem

# Issue : https://www.syllad.com has a mixture of English and Khasi articles
# with no categorization on the sitemap level
# Solution : <article> tag has the `category-khasi` class for Khasi articles


class SylladSpider(scrapy.Spider):
    name = "syllad"
    allowed_domains = ["syllad.com"]

    def start_requests(self):
        url = "https://www.syllad.com/sitemap_index.xml"
        yield scrapy.Request(url=url, callback=self.parse, meta={"playwright": True})

    def parse(self, response):
        selector = scrapy.Selector(text=response.text)
        links: List[str] = selector.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            if "post-sitemap" in link:
                yield scrapy.Request(
                    url=link, callback=self.parse_sitemap, meta={"playwright": True}
                )

    def parse_sitemap(self, response):
        selector = scrapy.Selector(text=response.text)
        links = selector.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            yield scrapy.Request(
                url=link, callback=self.parse_article_page, meta={"playwright": True}
            )

    def parse_article_page(self, response):
        selector = scrapy.Selector(text=response.text)
        te = selector.css(
            """article.category-khasi div.entry-content p ::text"""
        ).extract()
        te_processed = []
        for item in te:
            for i in item.split("\n"):
                te_processed.append(i.strip())
        article_text = " ".join(te_processed)

        title_selector = """article.category-khasi div.entry-content
            header.entry-header h1.entry-title::text"""
        title = selector.css(title_selector).get()

        if article_text is not None and article_text != "":
            news_item = KhasiNewsItem()
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["content"] = article_text

            yield news_item
