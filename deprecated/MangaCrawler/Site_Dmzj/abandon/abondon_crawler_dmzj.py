# -*- coding: utf-8 -*-
import os
import sys
import urllib.request

sys.path.append('../../')
from Downloader import downloader
from Common import local_properties
from Common import utils

from bs4 import BeautifulSoup

# soup = BeautifulSoup(open("web.html"))
#
# page_select =

# http://images.dmzj.com/w/五分钱电影院/全一卷/Five_Cents_Cinema_Red-001.jpg

# url = "http://manhua.dmzj.com/wufenqiandyyh/23616.shtml"
url = "https://www.dmzj.com/info/yuyanshutongrenzuopinji.html"

REFERER_URL = "http://manhua.dmzj.com/"
config = {'referer': REFERER_URL}
# config['proxy'] = local_properties.PROXY_SERVER

print("url: ", url)

request = urllib.request.Request(url)
headers = {"user-agent": "Mozilla/5.0"}
opener = urllib.request.build_opener()
if 'proxy' in config.keys():
    proxy_server = local_properties.PROXY_SERVER
    proxy = urllib.request.ProxyHandler({'http': proxy_server})
    opener = urllib.request.build_opener(proxy)
    print("使用代理: {}".format(proxy_server))
if 'referer' in config.keys():
    headers['referer'] = REFERER_URL
    print("使用referer: {}".format(REFERER_URL))
opener.addheaders = headers.items()
print(opener.addheaders)
urllib.request.install_opener(opener)

r = urllib.request.urlopen(request, timeout=1000)
print("Reading...")
read = r.read()
print("Response code: ", r.getcode())
print("Response length: ", len(read))
# print(read)

try:
    html_file = "web.html"
    f = open(html_file, "w+")
    f.write(read.decode('unicode_escape'))
    f.close()
    print("HTML wrote to file.")
except Exception as e:
    print("Something wrong! \n", e)
