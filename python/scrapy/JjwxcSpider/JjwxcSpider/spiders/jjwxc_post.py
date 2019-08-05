# -*- coding: utf-8 -*-
import scrapy
import re

from JjwxcSpider.items import JjwxcspiderItem

chapterid = 0
num = 0
tr = 5


class JjwxcSpider(scrapy.Spider):
	name = 'jjwxc_post'
	allowed_domains = ['jjwxc.net']
	start_urls = ['http://www.jjwxc.net/onebook.php?novelid=3373718']

	def parse(self, response):
		global chapterid, num
		# if tr <= 28:
		if num >= 5:
			page_list = response.xpath('//*[@id="oneboolt"]/tbody/tr' + str([num]))
			print(page_list)
			for page_li in page_list:
				item = JjwxcspiderItem()
				item['url'] = page_li.xpath('td[2]/span/div[1]/a/@href').extract_first()
				item['title'] = page_li.xpath('td[2]/span/div[1]/a/text()').extract_first()
			# item['chapter'] = ''.join(page_li.xpath('td[1]/text()').extract_first())
			# item['body'] = ''
				page_url = item['url']
				print('------------' + page_url + '------------')
			# yield scrapy.Request(url=page_url, meta={'item': item}, callback=self.parse)
				yield item

	# http://www.jjwxc.net/onebook.php?novelid=3373718&chapterid=2
	# chapterid += 1
	# num += 1
	# if chapterid <= 24:
	# 	# 获取下一页链接
	# 	link = 'http://www.jjwxc.net/onebook.php?novelid=3373718&chapterid=' + str(chapterid)
	#
	# 		#print('第' + str(num) + '页链接为：' + link)
	#
	# 	yield scrapy.Request(link, callback=self.parse)

	'''获取第二层的数据'''


# def parse_item(self, response):
# 	item = response.meta['item']
# 	item['body'] = response.xpath('//div[@class="noveltext"]/text()').extract()
# 	yield item
