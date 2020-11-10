# -*- coding: utf-8 -*-
import os
import subprocess
import sys

sys.path.append('../../')
from Downloader import downloader
from Common import local_properties

from datetime import datetime
import urllib.parse

ps = "ps1"
book_name = "wfqddyL"
e = "1605939985"
m = "x8chgL048SGqN3OSo4lyVA"
url_pattern = "https://i.hamreus.com/" + ps + "/w/" + book_name \
              + "/{}/{}.jpg.webp?e=" + e + "&m=" + m

start_page = 1  # 从第n页开始下载
max_chapter = 1
max_pages = [140]
# max_pages = [2]
# 用于单独下载某几页
spec_pages = []

chapter_formats = {'default': "{:02d}"}  # {14: "附页"}
page_formats = {'default': "{:04d}"}
# page_formats = {8: '{:03d}', 11: 't3649462_{:04d}', 12: 't3655090_{:04d}', 13: 't3660588_{:04d}',
#                 14: 't3661517_{:04d}'}

tasks = []
dir_name = "{}_{}".format(book_name, datetime.now().microsecond)
page_overall = 1
for c in range(max_chapter):
    chpt = c + 1
    for i in range(max_pages[c]):
        # 章节格式
        cp_fmt = chapter_formats['default']
        if chpt in chapter_formats.keys():
            cp_fmt = chapter_formats[chpt]
        # 页码格式
        fmt = page_formats['default']
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

        # 根据需求, 添加任务
        task = {'url': url, 'file_name': file_name, 'page': page_overall}
        if page_overall >= start_page:
            if len(spec_pages) == 0 or page_overall in spec_pages:
                tasks.append(task)
        page_overall += 1
        # print(file_name)

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
result = downloader.download(tasks, dir_path, config)
failed_pages = []
if len(result) > 0:
    log_file = "{}\crwaler_log.txt".format(dir_path)
    f = open(log_file, "w+")
    for item in result:
        f.write("{}\n".format(item))
        failed_pages.append(item['page'])
    f.write("Failed pages: \n{}\n".format(failed_pages))
    f.close()

# 打开下载目录
to_open_path = "{}\{}\\".format(os.getcwd(), dir_path)
print("Open:{}".format(to_open_path))
subprocess.Popen('explorer /select, {}'.format(to_open_path), shell=True)

# input("按任意键结束")
