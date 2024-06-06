from typing import List
import scrapy
from khasi_news.items import KhasiNewsItem


class UnongsainhimaSpider(scrapy.Spider):
    name = "unongsainhima"
    allowed_domains = ["unongsainhima.com"]
    start_urls = ["https://unongsainhima.com"]

    def start_requests(self):
        url = "https://unongsainhima.com/sitemap_index.xml"
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
        te = selector.css("article p::text").extract()
        te_processed = []
        for item in te:
            for i in item.split("\n"):
                te_processed.append(i.strip())
        article_text = "".join(te_processed)

        title_selector = """#main > div > div.main-content > header > 
            h1 ::text"""
        title = selector.css(title_selector).get()

        if article_text is not None and article_text != "":
            news_item = KhasiNewsItem()
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["content"] = article_text

            yield news_item
