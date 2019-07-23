# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 链接
    url = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 区域
    area = scrapy.Field()
    # 租金
    rental = scrapy.Field()
    # 户型
    unit = scrapy.Field()
    # 方式
    way = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 大小
    size = scrapy.Field()
