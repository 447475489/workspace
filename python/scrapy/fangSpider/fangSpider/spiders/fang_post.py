# -*- coding: utf-8 -*-
import scrapy
import logging
from fangSpider.items import FangspiderItem

i = 0


class FangSpider(scrapy.Spider):
	name = 'fang_post'
	allowed_domains = ['fang.com']
	start_urls = ['https://wuhan.zu.fang.com/']

	def parse(self, response):
		global i
		# 爬取所有房屋信息
		houseList = response.xpath('//*[@class="houseList"]/dl/dd')

		for house in houseList:
			item = FangspiderItem()
			item['name'] = house.xpath('p[1]/a/text()').extract_first()
			item['area'] = house.xpath('p[3]/a[1]/span/text()').extract_first()
			item['rental'] = house.xpath('div[2]/p/span/text()').extract_first()
			item['unit'] = house.xpath('normalize-space(p[2])').extract_first().split('|')[1]
			item['way'] = house.xpath('normalize-space(p[2])').extract_first().split('|')[0]
			item['orientation'] = house.xpath('normalize-space(p[2])').extract_first().split('|')[-1]
			item['size'] = house.xpath('normalize-space(p[2])').extract_first().split('|')[2]

			yield item

		i += 1
		if i < 101:
			# 获取下一页链接
			link = 'https://wuhan.zu.fang.com/house/i3' + str(i)
			# print(link)
			yield scrapy.Request(link, callback=self.parse)
