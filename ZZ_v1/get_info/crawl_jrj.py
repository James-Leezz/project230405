# http://www.jrj.com.cn/
# 2023/04/05

import requests
from lxml import etree
from pymongo import MongoClient
import random

import crawl_UA


class CrawlJrj:

    def __init__(self):
        self.init_url = "http://www.jrj.com.cn/"
        self.header = {'User-Agent': random.choice(crawl_UA.user_agent)}
        # 存放主页的主要链接
        # self.main_url_queue = queue.Queue(100)

        self.client = MongoClient(host="127.0.0.1", port=27017)
        self.jrjDatabase = self.client["ZZ_v1"]
        self.jrjCollection = self.jrjDatabase["jrj"]
        self.main_url_num = 1
        self.funptr = -1
        self.jrj_subwebsite_hash = {
            "财经": self.fun1,
            "科技": self.fun2,
            "消费": self.fun3,
            "医药": self.fun4,
            "房产": self.fun5,
            "研究院": self.fun6,
            "股票": self.fun7,
            "行情": self.fun8,
            "研报": self.fun9,
            "公司": self.fun10,
            "观点": self.fun11,
            "新三板": self.fun12,
            "理财": self.fun13,
            "基金": self.fun14,
            "银行": self.fun15,
            "保险": self.fun16,
            "信托": self.fun17,
            "私募": self.fun18,
            "中资行": self.fun19,
            "大盘": self.fun20,
            "市况": self.fun21,
            "观察": self.fun22,
            "题材": self.fun23,
            "慧眼": self.fun24,
            "专栏": self.fun25,
            "区块链": self.fun26,
            "元宇宙": self.fun27,
            "信贷": self.fun28,
            "期货": self.fun29,
            "期指": self.fun30,
            "外汇": self.fun31,
            "债券": self.fun32,
            "科创板": self.fun33,
            "主力": self.fun34,
            "公告": self.fun35,
            "异动": self.fun36,
            "提示": self.fun37,
            "内参": self.fun38,
            "视频": self.fun39,
            "产业": self.fun40,
            "汽车": self.fun41,
            "智头条": self.fun42,
            "ESG": self.fun43,
            "商业": self.fun44,
            "24小时": self.fun45,
            "新股": self.fun46,
            "港股": self.fun47,
            "美股": self.fun48,
            "沪港通": self.fun49,
            "早餐": self.fun50,
            "云图": self.fun51,
            "中概股": self.fun52
        }

    def get_main_url(self):
        # 首先访问http: // www.jrj.com.cn /
        # 获取52个主要的url，保存到mongodb中
        html_ret_init = requests.get(self.init_url, headers=self.header)
        html_content_init = html_ret_init.content.decode("gbk")
        html_content_init = etree.HTML(html_content_init)
        div_a = html_content_init.xpath('//div[@class = "navsub"]//a')
        for i in div_a:
            item_tmp = {"num": self.main_url_num, "name": i.xpath('./text()')[0], "link": i.xpath('./@href')[0]}
            # item_tmp["num"] = num
            # item_tmp["name"] = i.xpath('./text()')[0]
            # item_tmp["link"] = i.xpath('./@href')[0]
            self.main_url_num = self.main_url_num + 1
            print(item_tmp["name"])
            self.jrjCollection.insert_one(item_tmp)

    def process_main_url(self):
        # 读取mongodb的数据,执行对应的处理函数
        total_main_url_num = self.jrjCollection.find().count()
        for i in range(total_main_url_num):
            item_tmp = self.jrjCollection.find_one({"num": i + 1})
            item_tmp_num = item_tmp["num"]
            item_tmp_name = item_tmp["name"]
            item_tmp_link = item_tmp["link"]
            # 通过 item_tmp_name 找到对应的处理函数指针，执行对应的函数
            self.funptr = self.jrj_subwebsite_hash[item_tmp_name]
            self.funptr(item_tmp_num, item_tmp_name, item_tmp_link)

    def run(self):
        self.get_main_url()
        self.process_main_url()

    def fun1(self, num, name, link):
        print("fun1")
        print(num)
        print(name)
        print(link)

        sub_html_ret_init = requests.get(link, headers=self.header)
        sub_html_content_init = sub_html_ret_init.content.decode("gbk")
        sub_html_content_init = etree.HTML(sub_html_content_init)
        # 获取11个头部导航链接
        div_a = sub_html_content_init.xpath('//div[@class="navtop"]//a')

        # 在mongodb中创建表(collection)
        jrj_finance = self.jrjDatabase["jrj_finance"]

        # 将11个头部导航链接存入mongodb的 jrj_finance表中（collection中）
        num = 1
        for i in div_a:
            item_tmp = {"num": num, "name": i.xpath('./text()')[0], "link": i.xpath('./@href')[0]}
            # item_tmp["num"] = num
            # item_tmp["name"] = i.xpath('./text()')[0]
            # item_tmp["link"] = i.xpath('./@href')[0]
            num = num + 1
            print(item_tmp["name"])
            jrj_finance.insert_one(item_tmp)

        # 7*24实时要闻
        jrj_finance.insert_one({"num": num, "name": "7_24实时要闻", "link": "http://finance.jrj.com.cn/yaowen/"})
        num = num + 1
        jrj_finance.insert_one({"num": num, "name": "国际财经", "link": "http://finance.jrj.com.cn/list/guojicj.shtml"})
        num = num + 1
        jrj_finance.insert_one({"num": num, "name": "区块链", "link": "http://bc.jrj.com.cn/"})
        num = num + 1
        jrj_finance.insert_one(
            {"num": num, "name": "宏观_国内财经", "link": "http://finance.jrj.com.cn/list/guoneicj.shtml"})
        num = num + 1
        jrj_finance.insert_one(
            {"num": num, "name": "产业_热点追踪", "link": "http://finance.jrj.com.cn/list/industrynews.shtml"})
        num = num + 1
        jrj_finance.insert_one({"num": num, "name": "商业", "link": "http://biz.jrj.com.cn/"})
        num = num + 1
        jrj_finance.insert_one({"num": num, "name": "公司", "link": "http://finance.jrj.com.cn/list/companynews.shtml"})
        num = num + 1
        jrj_finance.insert_one({"num": num, "name": "科技快讯", "link": "http://finance.jrj.com.cn/tech/"})


    def fun2(self, num, name, link):
        pass

    def fun3(self, num, name, link):
        pass

    def fun4(self, num, name, link):
        pass

    def fun5(self, num, name, link):
        pass

    def fun6(self, num, name, link):
        pass

    def fun7(self, num, name, link):
        pass

    def fun8(self, num, name, link):
        pass

    def fun9(self, num, name, link):
        pass

    def fun10(self, num, name, link):
        pass

    def fun11(self, num, name, link):
        pass

    def fun12(self, num, name, link):
        pass

    def fun13(self, num, name, link):
        pass

    def fun14(self, num, name, link):
        pass

    def fun15(self, num, name, link):
        pass

    def fun16(self, num, name, link):
        pass

    def fun17(self, num, name, link):
        pass

    def fun18(self, num, name, link):
        pass

    def fun19(self, num, name, link):
        pass

    def fun20(self, num, name, link):
        pass

    def fun21(self, num, name, link):
        pass

    def fun22(self, num, name, link):
        pass

    def fun23(self, num, name, link):
        pass

    def fun24(self, num, name, link):
        pass

    def fun25(self, num, name, link):
        pass

    def fun26(self, num, name, link):
        pass

    def fun27(self, num, name, link):
        pass

    def fun28(self, num, name, link):
        pass

    def fun29(self, num, name, link):
        pass

    def fun30(self, num, name, link):
        pass

    def fun31(self, num, name, link):
        pass

    def fun32(self, num, name, link):
        pass

    def fun33(self, num, name, link):
        pass

    def fun34(self, num, name, link):
        pass

    def fun35(self, num, name, link):
        pass

    def fun36(self, num, name, link):
        pass

    def fun37(self, num, name, link):
        pass

    def fun38(self, num, name, link):
        pass

    def fun39(self, num, name, link):
        pass

    def fun40(self, num, name, link):
        pass

    def fun41(self, num, name, link):
        pass

    def fun42(self, num, name, link):
        pass

    def fun43(self, num, name, link):
        pass

    def fun44(self, num, name, link):
        pass

    def fun45(self, num, name, link):
        pass

    def fun46(self, num, name, link):
        pass

    def fun47(self, num, name, link):
        pass

    def fun48(self, num, name, link):
        pass

    def fun49(self, num, name, link):
        pass

    def fun50(self, num, name, link):
        pass

    def fun51(self, num, name, link):
        pass

    def fun52(self, num, name, link):
        pass


if __name__ == '__main__':
    a = CrawlJrj()
    a.run()
