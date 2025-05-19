# -*- coding: utf-8 -*-
import urllib.request
import json

raw_data = input("请输入链接列表:")

json_data = json.loads(raw_data)

urls = json_data['urls']
cookie = json_data['cookie']
ua = json_data['ua']
referer = json_data['referer']

url = urls[0]
print('Url: ', url)
request = urllib.request.Request(url)
# request.add_header("Cookie", cookie)
request.add_header('Referer', referer)
request.add_header('User-Agent', ua)

try:
    urllib.request.urlopen(request)
except Exception as e:
    print(e)
    print(e.args)



