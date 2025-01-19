import scrapy
class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["https://books.toscrape.com/"]
    start_urls = ["https://books.toscrape.com"]

