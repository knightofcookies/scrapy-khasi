from typing import List
import scrapy
from scrapy_selenium import SeleniumRequest


class RupangSpider(scrapy.Spider):
    name = "rupang"
    allowed_domains = ["urupang.com"]

    def start_requests(self):
        url = "https://www.urupang.com/sitemap_index.xml"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        links: List[str] = response.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            if 'post-sitemap' in link:
                yield SeleniumRequest(url=link, callback=self.parse_sitemap)

    def parse_sitemap(self, response):
        links = response.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            yield SeleniumRequest(url=link, callback=self.parse_article_page)

    def parse_article_page(self, response):
        te = response.css("main.content p::text").extract()
        te_processed = []
        for item in te:
            for i in item.split("\n"):
                te_processed.append(i.strip())
        article_text = "".join(te_processed)

        title_selector = """body > div.site-container > div
         > div > main > article > header > h1 ::text"""
        title = response.css(title_selector).get()
        yield {"text": title + article_text}
