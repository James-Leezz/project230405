from pymongo import MongoClient
import queue
import requests
from lxml import etree
import json
import threading


# headers ="Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
# url = "http://www.jrj.com.cn/"
# html_ret = requests.get(url,headers).content.decode("gbk")
# html_content = etree.HTML(html_ret)
#
# div_list = html_content.xpath('//div[@class = "navsub"]//a')
#
# print(div_list[0].xpath("./text()")[0].encode())
# print(div_list[0].xpath('./@href'))

# a = queue.Queue(10);
# a.put(1)
# a.put(3)
# a.put(4)
# print(a.qsize())
# print(a.get())
# print(a.qsize())
# a.task_done()
# print(a.qsize())

for i in range(10):
    print(i)