from typing import List
import scrapy
from scrapy_selenium import SeleniumRequest
from khasi_news.items import KhasiNewsItem


class RupangSpider(scrapy.Spider):
    name = "rupang"
    allowed_domains = ["urupang.com"]

    # custom_settings = {"FEEDS": {"rupang.csv": {"format": "csv"}}}

    # The below two methods can be commented out
    # to crawl all the post sitemaps at once.
    # def start_requests(self):
    #     url = "https://www.urupang.com/sitemap_index.xml"
    #     yield SeleniumRequest(url=url, callback=self.parse)

    # def parse(self, response):/
    #     links: List[str] = response.css("table tbody tr td a ::attr(href)").extract()
    #     for link in links:
    #         if "post-sitemap" in link:
    #             yield SeleniumRequest(url=link, callback=self.parse_sitemap)

    # Comment this method out to crawl the entire site
    def start_requests(self):
        url = "https://www.urupang.com/post-sitemap2.xml"
        yield SeleniumRequest(url=url, callback=self.parse_sitemap)

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

        if article_text is not None and article_text != "":
            news_item = KhasiNewsItem()
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["content"] = article_text

            yield news_item
