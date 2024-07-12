from typing import List
import scrapy
from khasi_news.items import KhasiNewsItem


class BatesitvSpider(scrapy.Spider):
    name = "batesitv"
    allowed_domains = ["batesitv.com"]

    def start_requests(self):
        url = "https://batesitv.com/category/khasi/"
        yield scrapy.Request(url=url, callback=self.parse, meta={"playwright": True})

    def parse(self, response):
        links: List[str] = response.css("h2.entry-title a ::attr(href)").extract()
        for link in links:
            yield scrapy.Request(
                url=link, callback=self.parse_article_page, meta={"playwright": True}
            )
        next_link = response.css("div.nav-links a.next ::attr(href)")
        if next_link is not None:
            yield scrapy.Request(
                url=next_link, callback=self.parse, meta={"playwright": True}
            )

    def parse_article_page(self, response):
        te = response.css("div.entry-content p::text").extract()
        te_processed = []
        for item in te:
            for i in item.split("\n"):
                te_processed.append(i.strip())
        article_text = "".join(te_processed)

        title_selector = """h1.entry-title ::text"""
        title = response.css(title_selector).get()

        if article_text is not None and article_text != "":
            news_item = KhasiNewsItem()
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["content"] = article_text

            yield news_item
