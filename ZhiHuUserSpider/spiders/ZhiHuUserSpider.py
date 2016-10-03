# -*- coding: utf-8 -*-
from ..settings import *
import scrapy
from scrapy.http import Request
from ..items import ZhihuuserspiderItem


# 为了创建一个Spider,必须继承scrapy.Spider类
class ZhiHuUserSpider(scrapy.Spider):
    # 爬虫的名字,用于区别Spider,该名字必须是唯一的
    name = 'ZhiHuUserSpider'
    # 只爬取某个域名
    allowed_domain = ['www.zhihu.com']
    # Spider启动时爬取的第一个url
    start_url = ['https://www.zhihu.com/people/amberno1111']
    
    def __init__(self, *args, **kwargs):
        """
        :summary: 类初始化函数, 由于知乎使用了相对url,因此在这里设置一个base_url
        :param args: 
        :param kwargs: 
        """
        super(ZhiHuUserSpider, self).__init__(*args, **kwargs)
        self.base_url = 'https://www.zhihu.com'

    def make_requests_from_url(self, url):
        """
        :summary: 重写make_requests_from_url()方法, 把cookie传入
        :param url:
        :return:
        """
        return Request(url, method='GET', headers=ZHIHU_HEADER, cookies=ZHIHU_COOKIE)

    def start_requests(self):
        """
        :summary: 设置每一次访问url都给服务器发送带有cookie的请求
        :return:
        """
        for url in self.start_url:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        """
        :summary: 解析用户主页,把获取到的数据存入Item里面
        :param response:
        :return:
        """
        item = ZhihuuserspiderItem()
        sel = response.xpath('//div[@class="zm-profile-header ProfileCard"]')
        item['username'] = sel.xpath('//div[@class="title-section"]/span[@class="name"]/text()').extract()
        follow = response.xpath('//div[@class="zm-profile-side-following zg-clear"]/a/strong/text()').extract()
        if follow:
            if follow[0]:
                item['followees'] = int(follow[0])
            if follow[1]:
                item['followers'] = int(follow[1])
        item['location'] = sel.xpath('//span[@class="location item"]/text()').extract()
        item['business'] = sel.xpath('//span[@class="business item"]/a/text()').extract()
        item['gender'] = 'male' if sel.xpath('//i[contains(@class, "icon icon-profile-male")]') else 'female'
        item['employment'] = sel.xpath('//span[@class="employment item"]/a/text()').extract()
        item['position'] = sel.xpath('//span[@class="position item"]/a/text()').extract()
        item['education'] = sel.xpath('//span[@class="education item"]/a/text()').extract()
        item['about_me'] = sel.xpath('//span[@class="description unfold-item"]/span/text()').extract()
        item['likes'] = sel.xpath('//span[@class="zm-profile-header-user-agree"]/strong/text()').extract()
        profile = sel.xpath('//div[@class="profile-navbar clearfix"]/a/@href').extract()
        item['questions'] = self.base_url + profile[1]
        item['answers'] = self.base_url + profile[2]
        item['articles'] = self.base_url + profile[3]
        yield item





