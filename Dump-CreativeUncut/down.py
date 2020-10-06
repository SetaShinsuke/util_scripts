# -*- coding: utf-8 -*-
import locale
import os
import io
import re
import subprocess
import sys
import urllib.request
from datetime import datetime
# import chardet

import requests

# reload(sys)
# sys.setdefaultencoding('utf-8')
print("in: {}".format(sys.stdin.encoding))
print("out: {}".format(sys.stdout.encoding))


break_line = "----n----"
referer_host = "https://www.creativeuncut.com/"
proxy_server = "'192.168.50.96:8787'"

def r_in(hint):
    # return input(hint.encode(sys.stdin.encoding))
    return input(hint)


def r_out(content):
    # return content.encode(sys.stdout.encoding)
    return content


def r_print(content):
    print(r_out(content))


urls_str = r_in("输入网址列表:")

dir_path = u"download\{}_{}".format("download", datetime.now().microsecond)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

def filter_fun(item):
    return item.startswith("http")

img_urls = urls_str.split(break_line)
img_urls = list(filter(filter_fun, img_urls))
# r_print("Download urls: {}".format(img_urls))

total = len(img_urls)
downloaded = 0
max_amount = total
# max_amount = 3
for img_url in img_urls:
    if downloaded >= max_amount:
        break
    if not img_url.startswith("http"):
        downloaded += 1
        continue
    print("url: {}".format(img_url))
    file_name = img_url.split('/')[-1].replace('\\', '_').replace('/', '_')
    # file_name = img_url.split('/')[-1].encode('gbk', 'ignore').replace('\\', '_').replace('/', '_')
    r_print("Downloading {}/{} : {}".format(downloaded + 1, total, file_name))
    final_url = img_url

    proxy = urllib.request.ProxyHandler({'http': proxy_server})
    opener = urllib.request.build_opener(proxy)
    # 添加 referer 并下载
    opener.addheaders = [('Referer', referer_host)]
    urllib.request.install_opener(opener)
    resp = urllib.request.urlretrieve(final_url, "{}\{}".format(dir_path, file_name))
    # print("file size: {}".format(resp.headers['content-length']))
    downloaded += 1
r_print(u"Download finished {}/{}!\nSaved at \{}".format(downloaded, total, dir_path))