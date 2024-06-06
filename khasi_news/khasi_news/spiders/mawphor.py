from typing import List
import scrapy
from khasi_news.items import KhasiNewsItem


class MawphorSpider(scrapy.Spider):
    name = "mawphor"
    allowed_domains = ["mawphor.com"]

    def start_requests(self):
        url = "https://mawphor.com/sitemap.xml"
        yield scrapy.Request(url=url, callback=self.parse, meta={"playwright": True})

    def parse(self, response):
        links: List[str] = response.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            if "post-sitemap" in link:
                yield scrapy.Request(
                    url=link, callback=self.parse_sitemap, meta={"playwright": True}
                )

    def parse_sitemap(self, response):
        links = response.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            yield scrapy.Request(
                url=link, callback=self.parse_article_page, meta={"playwright": True}
            )

    def parse_article_page(self, response):
        te = response.css("article div.entry-content p::text").extract()
        te_processed = []
        for item in te:
            for i in item.split("\n"):
                te_processed.append(i.strip())
        article_text = "".join(te_processed)

        title_selector = """article div.post-header h1.single-post-title 
            span.post-title ::text"""
        title = response.css(title_selector).get()

        if article_text is not None and article_text != "":
            news_item = KhasiNewsItem()
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["content"] = article_text

            yield news_item
