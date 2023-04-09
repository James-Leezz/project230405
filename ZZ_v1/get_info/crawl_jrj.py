# http://www.jrj.com.cn/
# 2023/04/05

import requests
import queue
from lxml import etree
from pymongo import MongoClient
import json
import threading
import random

import crawl_UA

class crawl_jrj:

    def __init__(self):
        self.init_url = "http://www.jrj.com.cn/"
        self.header = {'User-Agent' : random.choice(crawl_UA.user_agent)}
        # 存放主页的主要链接
        self.main_url_queue = queue.Queue(100)

        self.html_ret_queue = queue.Queue(10)
        self.html_content_queue = queue.Queue(10)
        self.client = MongoClient(host = "127.0.0.1", port = 27017)
        self.collection = self.client["ZZ_v1"]["jrj"]

    def get_main_url_queue(self):
        # 首先访问http: // www.jrj.com.cn /
        html_ret_init = requests.get(self.init_url, headers = self.header)
        html_content_init = html_ret_init.content.decode("utf-8")
        html_content_init = etree.HTML(html_content_init)
        div_a = html_content_init.xpath('//div[@class = "navsub"]//a')
        for i in div_a:
            item_tmp = {}
            item_tmp["link"] = div_a.xpath('//@href')
            item_tmp["name"] = div_a.xpath('//text()')
            self.main_url_queue.put(item_tmp)




    def send_url_request(self):
        pass

    def process_html_ret(selfself):
        pass

    def save_content(self):
        pass

    def run(self):
        pass


