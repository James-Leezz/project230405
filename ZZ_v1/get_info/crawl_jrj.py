# http://www.jrj.com.cn/
# 2023/04/05
import asyncio

import requests
import queue
from lxml import etree
from pymongo import MongoClient
import json
import threading
import random

import crawl_UA
import crawl_hash_table_jrj

class crawl_jrj:

    def __init__(self):
        self.init_url = "http://www.jrj.com.cn/"
        self.header = {'User-Agent' : random.choice(crawl_UA.user_agent)}
        # 存放主页的主要链接
        # self.main_url_queue = queue.Queue(100)

        self.client = MongoClient(host = "127.0.0.1", port = 27017)
        self.jrjDatabase = self.client["ZZ_v1"]
        self.jrj_caijingCollection = self.jrjDatabase["jrj_caijing"]

    def get_main_url(self):
        # 首先访问http: // www.jrj.com.cn /
        # 获取52个主要的url，保存到mongodb中
        html_ret_init = requests.get(self.init_url, headers = self.header)
        html_content_init = html_ret_init.content.decode("gbk")
        html_content_init = etree.HTML(html_content_init)
        div_a = html_content_init.xpath('//div[@class = "navsub"]//a')
        num = 1
        for i in div_a:
            item_tmp = {}
            item_tmp["num"] = num
            num = num + 1
            item_tmp["name"] = i.xpath('./text()')[0]
            item_tmp["link"] = i.xpath('./@href')[0]
            print(item_tmp["name"])
            self.jrj_caijingCollection.insert((item_tmp))
            # self.main_url_queue.put(item_tmp)


    def process_main_url(self):
        # 读取mongodb的数据,执行对应的处理函数
        total_main_url_num = self.jrj_caijingCollection.find().count()
        for i in range(total_main_url_num):
            item_tmp = self.jrj_caijingCollection.find_one({"num" : i + 1})
            item_tmp_num = item_tmp["num"]
            item_tmp_name = item_tmp["name"]
            item_tmp_link = item_tmp["link"]
            # 通过 item_tmp_name 找到对应的处理函数指针，执行对应的函数
            fun_ptr = crawl_hash_table_jrj.jrj_subwebsite_hash[item_tmp_name]
            print(fun_ptr)
            fun_ptr(item_tmp_num, item_tmp_link)


    def run(self):
        self.get_main_url()
        self.process_main_url()


if __name__ == '__main__':
    a = crawl_jrj()
    a.run()