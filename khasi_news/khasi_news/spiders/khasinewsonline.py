import scrapy
from khasi_news.items import KhasiNewsItem

# Issue: https://khasinewsonline.com has 16 articles and low quality articles

class KhasinewsonlineSpider(scrapy.Spider):
    name = "khasinewsonline"
    allowed_domains = ["khasinewsonline.com"]

    def start_requests(self):
        url = "https://khasinewsonline.com/wp-sitemap-posts-post-1.xml"
        yield scrapy.Request(
            url=url, callback=self.parse_sitemap, meta={"playwright": True}
        )

    def parse_sitemap(self, response):
        links = response.css("table tbody tr td a ::attr(href)").extract()
        for link in links:
            yield scrapy.Request(
                url=link, callback=self.parse_article_page, meta={"playwright": True}
            )

    def parse_article_page(self, response):
        te = response.css(
            "main article div.article-inner div.entry-content p::text"
        ).extract()
        te_processed = []
        for item in te:
            for i in item.split("\n"):
                te_processed.append(i.strip())
        article_text = "".join(te_processed)

        title_selector = """main article div.article-inner header.entry-header 
            h1.entry-title ::text"""
        title = response.css(title_selector).get()

        if article_text is not None and article_text != "":
            news_item = KhasiNewsItem()
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["content"] = article_text

            yield news_item
