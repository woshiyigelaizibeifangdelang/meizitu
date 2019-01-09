# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MeizituPipeline(object):
    def open_spider(self, spider):
        self.fp = open('bang.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')

        return item

    def close_spider(self, spider):
        self.fp.close()