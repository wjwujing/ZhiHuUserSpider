# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZhihuuserspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    知乎用户信息Item：
        username：用户名
        followees：用户关注的人
        followers：用户粉丝
        location： 位置
        business： 行业
        gender： 性别
        employment： 公司
        position： 职位
        education： 教育
        about_me： 个人简介
        likes： 获得的赞同数
        questions： 提问
        answers： 回答
        articles： 文章
        _id： 存入数据库时的主键
    """
    username = Field()
    followees = Field()
    followers = Field()
    location = Field()
    business = Field()
    gender = Field()
    employment = Field()
    position = Field()
    education = Field()
    about_me = Field()
    likes = Field()
    questions = Field()
    answers = Field()
    articles = Field()
    _id = Field()
