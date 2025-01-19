from pathlib import Path
from typing import Union

import scrapy
from scrapy import Selector
from scrapy.http import Response
class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["https://books.toscrape.com/"]
    start_urls = ["https://books.toscrape.com"]

    def _parse_and_page(self, active_url: str) -> dict:
        self.driver.get(active_url)

        return {
            "title": response.css("div.product_main h1::text").get(),
            "price": response.css(".price_color::text").get().replace("£", ""),
            "amount_in_stock": response.css("p.instock.availability').re_first(r'\((\d+) available\)"),
            "rating": response.css("p.star-rating::attr(class)").get().split()[-1],
            "category": response.css("ul.breadcrumb li:nth-of-type(3) a::text").get(),
            "description": response.css("#product_description h2::text").get(),
            "upc": response.css("table.table-striped tr:nth-child(1) td::text").get()
        }

    def parse(self, response: Response, **kwargs):
        for li in response.css("ol.row li"):
            relative_url = li.css("a::attr(href)").get()
            full_url = urljoin(start_urls, relative_url)

            yield {_parse_and_page(response, full_url)}
