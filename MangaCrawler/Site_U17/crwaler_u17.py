# -*- coding: utf-8 -*-

import requests

from u17_urls import BOOK_URL

book_id = input("输入漫画ID: ")
# 《超合金社团》ID: 53591

book_url = BOOK_URL + "" + book_id
BOOK_API = "http://app.u17.com/v3/appV3/android/phone/comic/detail_static"
book_url = BOOK_API

args = {'android_id': '0A00270000130000', 'v': '3070099', 'model': 'VPhone',
        'come_from': 'wandoujia'}
args['comicid'] = book_id
# args = {}
print('args: %s', args)

# todo: 增加 Header 字段
request = requests.get(book_url, args)

print("url: %s", request.url)
print("request: %s", request)
