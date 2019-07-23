# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class FangspiderPipeline(object):
	def __init__(self):
		client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
		self.db = client[settings['MONGO_DB']]  # 获得数据库的句柄
		self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
		# 数据库登录需要账户密码的话
		self.db.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])

	def process_item(self, item, spider):
		print("名称", item['name'])
		print("区域", item['area'])
		print("租金", item['rental'])
		# print("户型", item['unit'])
		# print("方式", item['way'])
		# print("朝向", item['orientation'])
		# print("大小", item['size'])

		postItem = dict(item)  # 把item转化为字典形式
		self.coll.insert(postItem)  # 向数据库插入一条记录
		return item
