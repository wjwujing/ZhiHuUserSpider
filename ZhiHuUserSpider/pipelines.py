# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, codecs
import pymongo
from .items import ZhihuuserspiderItem
from scrapy.exceptions import DropItem


class ZhihuuserspiderPipeline(object):
    def __init__(self):
        """
        :summary: 类初始化方法,在这里初始化数据库
        """
        import pymongo
        # 连接MongoDB数据库zhihu,集合zh_user
        connection = pymongo.MongoClient('127.0.0.1', 27017)
        self.db = connection["zhihu"]
        self.zh_user = self.db['zh_user']

    def process_item(self, item, spider):
        """
        :summary: 先判断item是否已经实例化,如果是,就把数据存储进MOngoDB中
        :param item:
        :param spider:
        :return:
        """
        if isinstance(item, ZhihuuserspiderItem):
            self.saveOrUpdate(self.zh_user, item)
        # return item

    def saveOrUpdate(self, collection, item):
        """
        :summary: 把数据存进MongoDB
        :param collection:
        :param item:
        :return:
        """
        collection.insert(dict(item))
        return item


# 以json的格式存储
class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('zhihu.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "," + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()






























