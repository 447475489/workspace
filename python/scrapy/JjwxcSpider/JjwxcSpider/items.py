# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JjwxcspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 章节url
    url = scrapy.Field()
    # 章节标题
    title = scrapy.Field()
    # 章节序号
    chapter = scrapy.Field()
    # 内容提要
    summary = scrapy.Field()
    # 正文
    body = scrapy.Field()