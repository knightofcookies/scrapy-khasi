from typing import List
import scrapy
from khasi_news.items import KhasiNewsItem


class KynjatshaiSpider(scrapy.Spider):
    name = "kynjatshai"
    allowed_domains = ["kynjatshai.com"]

    def start_requests(self):
        url = "https://kynjatshai.com/sitemap_index.xml"
        yield scrapy.Request(url=url, callback=self.parse, meta={"playwright": True})

    def parse(self, response):
        links: List[str] = response.css("table tbody tr td a ::attr(href)").extract()
        print(links)  # DEBUG
        for link in links:
            if "post-sitemap" in link:
                yield scrapy.Request(
                    url=link, callback=self.parse_sitemap, meta={"playwright": True}
                )

    # def start_requests(self):
    #     url = "https://kynjatshai.com/post-sitemap1.xml"
    #     yield scrapy.Request(
    #         url=url, callback=self.parse_sitemap, meta={"playwright": True}
    #     )

    def parse_sitemap(self, response):
        links = response.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            yield scrapy.Request(
                url=link, callback=self.parse_article_page, meta={"playwright": True}
            )

    def parse_article_page(self, response):
        te = response.css("body main div div article p::text").extract()
        te_processed = []
        for item in te:
            for i in item.split("\n"):
                te_processed.append(i.strip())
        article_text = "".join(te_processed)

        title_selector = """body main div div h1::text"""
        title = response.css(title_selector).get()

        if article_text is not None and article_text != "":
            news_item = KhasiNewsItem()
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["content"] = article_text

            yield news_item
