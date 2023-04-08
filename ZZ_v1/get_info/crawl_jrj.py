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
        self.url_queue = queue.Queue(10)
        self.html_ret_queue = queue.Queue(10)
        self.html_content_queue = queue.Queue(10)
        self.client = MongoClient(host = "127.0.0.1", port = 27017)
        self.collection = self.client["ZZ_v1"]["jrj"]

    def get_url_queue(self):
        pass
