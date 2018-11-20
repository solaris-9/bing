# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import unicodecsv as csv
import time
import json

class BingPipeline(object):
    def __init__(self):
        self.file = open('log/DICT.%s.txt' % time.strftime('%Y%m%d-%H%M%S', time.localtime()), 'wb')
        fields = (
            'word',
            'prUS',
            'prUK',
            'pClass',
            'defBing',
            'defWeb',
        )
        self.writer = csv.DictWriter(self.file, fieldnames=fields, dialect='excel-tab')
        self.writer.writeheader()
        
    def process_item(self, item, spider):
        try:
            self.writer.writerow(item)
        except Exception as e:
            print(u'####Word: %s handling error!' % item['word'])
            print(e)
            
        return item

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('log/DICT.%s.json' % time.strftime('%Y%m%d-%H%M%S', time.localtime()), 'tw')
    
    def close_spider(self, spider):
        self.file.close()
    
    def process_item(self, item, spider):
        try:
            print("^^^^^: " + dict(item).__repr__())
            line = json.dumps(dict(item), indent=4, ensure_ascii=False) + "\n"
            print("@@@@@: " + line)
            self.file.write(line)
            #print(bytes(line))
        except Exception as e:
            print(u'####Word: %s handling error!' % item['word'])
            print(e)
        return item