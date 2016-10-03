# -*- coding: utf-8 -*-
from scrapy.http.request import Request
import scrapy


class PriceministerSpider(scrapy.Spider):
    name = "priceminister"
    # allowed_domains = ["http://www.priceminister.com/"]
    start_urls = (
        'http://www.priceminister.com/',
    )
    # pythonscraping.com/blog/xpath-and-scrapy
    def parse(self, response):
        categories = response.xpath('//li[@class="category"]/a/@href')
        selector_iterator = iter(categories)
        for selector in selector_iterator:
            end_url = selector.extract()
            yield Request(self.start_urls[0] + end_url, callback=self.parse_category)

    def parse_category(self, response):
        print "yolo"

    def parse_item(self, response):
        pass
