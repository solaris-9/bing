# -*- coding: utf-8 -*-
import scrapy


class DictSpider(scrapy.Spider):
    name = 'dict'
    allowed_domains = ['cn.bing.com']
    start_urls = ['http://cn.bing.com/']

    def parse(self, response):
        pass
