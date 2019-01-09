# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    # 发布时间
    price = scrapy.Field()
    # 浏览量
    color = scrapy.Field()
    # 收藏量
    sku = scrapy.Field()
    # 下载量
    details = scrapy.Field()
    # 图片地址
    # image_src = scrapy.Field()
