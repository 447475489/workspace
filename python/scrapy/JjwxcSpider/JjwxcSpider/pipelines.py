# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JjwxcspiderPipeline(object):
	# def __init__(self):
	# 	self.json_file = open("jjwxc_post.json", "wb+")
	# 	self.json_file.write('[\n]'.encode("utf-8"))
	#
	# # 重写close_spider回调方法，用于关闭文件
	# def close_spider(self, spider):
	# 	print('----关闭文件-----')
	# 	# 后退两个字符，也就是去掉最后一条记录之后的换行符和逗号
	# 	self.json_file.seek(-2, 1)
	# 	self.json_file.write('\n'.encode("utf-8"))
	# 	self.json_file.close()

	def process_item(self, item, spider):

		# print("章节序号", item['chapter'])
		print("章节标题:", item['title'])
		print("章节链接:", item['url'])
		# print("正文", item['body'])

		# 将item对象转换为json字符串
		# item['body'] = json.dumps(dict(item), ensure_ascii=False)
		# text = item['body'].replace('"', '\n').replace(',', '').replace('\\r\\n', '')
		# # 写入json字符串
		# # self.json_file.write(text.encode("utf-8"))
		# with open('text.txt', 'w', encoding='utf-8') as f:  # ("第" + item['chapter'] + "章 " + item['title'] + '.txt')
		# 	for line in text:
		# 		f.writelines(line)

		return item
