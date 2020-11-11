# -*- coding: utf-8 -*
from os import listdir
import pyperclip

path = input("请输入JS文件目录:")

js_str = ""
for f in listdir(path):
    if f.split('.')[-1] == 'js':
        js_str = open("{}\{}".format(path, f), 'r').read()
        js_str = js_str.replace('\n','').replace('    ','')
        break

# {{ 转义 {
pattern = "javascript:(function(){{{}}})();"
data = pattern.format(js_str)
print("data: ", data)

pyperclip.copy(data)