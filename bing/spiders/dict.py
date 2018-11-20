# -*- coding: utf-8 -*-
import scrapy
from bing.items import BingItem
from .wordList import words

class DictSpider(scrapy.Spider):
    name = 'dict'
    allowed_domains = ['cn.bing.com']
    start_urls = (
        'https://cn.bing.com/dict/search?q=%s&FORM=BDVSP6&mkt=zh-cn' % w for w in words
    )

    def parse(self, response):
        p = BingItem()
        
        '''p[u'word'] = bytes(response.xpath('//div[@id="headword"]/h1/strong/text()').extract()[0]).decode('utf8').strip()
        p[u'prUS'] = bytes(response.xpath('//div[@class="hd_prUS"]/text()').extract()[0]).decode('utf8').strip()
        p[u'prUK'] = bytes(response.xpath('//div[@class="hd_pr"]/text()').extract()[0]).decode('utf8').strip()
        p[u'pClass'] = bytes(response.xpath('//span[@class="pos"]/text()').extract()[0]).decode('utf8').strip()
        p[u'defBing'] =bytes(response.xpath('//span[@class="def"]/span[1]/text()').extract()[0]).decode('utf8').strip()
        p[u'defWeb'] =bytes(response.xpath('//span[@class="def"]/span[last()]/text()').extract()[0]).decode('utf8').strip()'''
        p[u'word'] = u''+response.xpath('//div[@id="headword"]/h1/strong/text()').extract()[0].strip()
        p[u'prUS'] = u''+response.xpath('//div[@class="hd_prUS"]/text()').extract()[0].strip()
        p[u'prUK'] = u''+response.xpath('//div[@class="hd_pr"]/text()').extract()[0].strip()
        p[u'pClass'] = u''+response.xpath('//span[@class="pos"]/text()').extract()[0].strip()
        p[u'defBing'] =u''+response.xpath('//span[@class="def"]/span[1]/text()').extract()[0].strip()
        p[u'defWeb'] =u''+response.xpath('//span[@class="def"]/span[last()]/text()').extract()[0].strip()
        yield p
        
        pass
