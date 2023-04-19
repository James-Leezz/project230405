import requests
from lxml import etree
from pymongo import MongoClient
import random
import crawl_UA
import crawl_hash_table



class CrawlDfcf:

    def __init__(self):
        # self.init_url = "https://www.eastmoney.com/"
        self.init_url = crawl_hash_table.website_hash["东方财富"]
        self.header = {'User-Agent': random.choice(crawl_UA.user_agent)}

        self.client = MongoClient(host="127.0.0.1", port=27017)
        self.dfcfDatabase = self.client["ZZ_v1"]
        self.dfcfCollection = self.dfcfDatabase["dfcf"]
        self.funptr = -1

        self.jrj_subwebsite_hash = {
        }



    def get_main_url(self):
        # 首先访问init_url
        pass


    def process_main_url(self):
        # 读取mongodb的数据,执行对应的处理函数
        pass


    def run(self):
        pass


if __name__ == '__main__':
    a = CrawlDfcf()
    a.run()
