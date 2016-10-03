# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
# from .items import ZhihuuserspiderItem
# from scrapy.exceptions import DropItem
#
#
# class ZhihuuserspiderPipeline(object):
#     def __init__(self):
#         """
#         :summary: 类初始化方法,在这里初始化数据库,数据库相关的db_name以及collection_name存储在settings中,scrapy会自动调用
#         """
#         import pymongo
#         connection = pymongo.MongoClient('127.0.0.1', 27017)
#         self.db = connection["zhihu"]
#         self.zh_user = self.db['zh_user']
#
#
#
#
#     def process_item(self, item, spider):
#         return item


import json, codecs


# 以json的格式存储
class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('zhihu.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()






























