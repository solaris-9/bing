# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    word = scrapy.Field()
    prUS = scrapy.Field()
    prUK = scrapy.Field()
    pClass = scrapy.Field()
    defBing = scrapy.Field()
    defWeb = scrapy.Field()
	
    pass
