# -*- coding: utf-8 -*-
import os
import subprocess
import sys

sys.path.append('../../')
from Downloader import downloader
from Common import local_properties

from datetime import datetime
import urllib.parse

book_name = "wfqdyyq"
url_pattern = "https://i.hamreus.com/ps4/w/" + book_name \
              + "/{}/{}.jpg.webp?e=1605774950&m=WKE-pulKQ2AyCxtdPnbyug"

start_page = 108  # 从第n页开始下载
max_chapter = 14
max_pages = [13, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 9, 15, 1]
chapter_formats = {14: "附页"}
page_formats = {8: '{:03d}', 11: 't3649462_{:04d}', 12: 't3655090_{:04d}', 13: 't3660588_{:04d}',
                14: 't3661517_{:04d}'}

tasks = []
dir_name = "{}_{}".format(book_name, datetime.now().microsecond)
page_overall = 1
for c in range(max_chapter):
    chpt = c + 1
    for i in range(max_pages[c]):
        # 章节格式
        cp_fmt = "第{:02d}回"
        if chpt in chapter_formats.keys():
            cp_fmt = chapter_formats[chpt]
        # 页码格式
        fmt = "{:04d}"
        if chpt in page_formats.keys():
            fmt = page_formats[chpt]
        chpt_name = urllib.parse.quote(cp_fmt.format(chpt).encode('utf-8'))
        url = url_pattern.format(chpt_name, fmt.format(i + 1))

        # print(url)
        # file_name = url.split("/")[-1].split("?")[0]  # .replace(".webp","")
        ext = url.split("/")[-1].split("?")[0].split(".")[-1]
        ext = url.split("/")[-1].split("?")[0].split(".")[-1]
        # 页码.格式
        file_name = "{:04d}.{}".format(page_overall, ext)
        page_overall += 1
        # print(file_name)

        task = {'url': url, 'file_name': file_name}
        if page_overall >= start_page:
            tasks.append(task)

# dir_name = url.split("/")[-3]
# dir_name = urllib.parse.unquote(dir_name)

print("dir_name: {}".format(dir_name))
print("start from Page.{}".format(start_page))
print("")

proxy = local_properties.PROXY_SERVER
config = {'proxy': proxy, 'referer': 'https://www.manhuagui.com/'}
# config = {'referer': 'https://www.manhuagui.com/'}
dir_path = "download\{}".format(dir_name)

# ------下载
downloader.download(tasks, dir_path, config)

# 打开下载目录
to_open_path = "{}\{}\\".format(os.getcwd(), dir_path)
print("Open:{}".format(to_open_path))
subprocess.Popen('explorer /select, {}'.format(to_open_path), shell=True)
