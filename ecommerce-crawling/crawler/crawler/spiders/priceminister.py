# -*- coding: utf-8 -*-
import scrapy


class PriceministerSpider(scrapy.Spider):
    name = "priceminister"
    allowed_domains = ["http://www.priceminister.com/"]
    start_urls = (
        'http://www.http://www.priceminister.com//',
    )

    def parse(self, response):
        pass
