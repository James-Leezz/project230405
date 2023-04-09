from pymongo import MongoClient
import queue
import requests
from lxml import etree
import json
import threading


headers ="Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
url = "http://www.jrj.com.cn/"
html_ret = requests.get(url,headers).content.decode("gb2312")
html_content = etree.HTML(html_ret)

div_list = html_content.xpath('//div[@class = "navsub"]//a')

print(div_list[0].xpath("./text()"))
print(div_list[0].xpath('./@href'))

