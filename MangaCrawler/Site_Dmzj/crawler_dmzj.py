# -*- coding: utf-8 -*-
import json
import os
from os import listdir
import subprocess
import sys
from datetime import datetime
from os.path import join

sys.path.append('../../')
from Downloader import downloader
from Common import local_properties
from Common import utils

# todo: 测试数量
# TEST_AMOUNT = -1
TEST_AMOUNT = 2

TASK_FILE = "tasks.json"
DOWNLOAD_DIR = 'dir'
FILE_NAME = 'file_name'
URL = 'url'

REFERER_DMZJ = "http://manhua.dmzj.com/"
UA = "Mozilla/5.0"

# task_path = input("请输入目标目录: ")
# if len(task_path) <= 0:
#     print("未输入, 将在当前目录进行操作!")
#     task_path = join(os.getcwd(), "tasks")

task_path = join(os.getcwd(), "tasks")

# 任务结束后将文件名改掉!
task_file = "{}\\tasks\{}".format(task_path, TASK_FILE)
task_file_name = TASK_FILE

for f in listdir(task_path):
    if f.startswith('task'):
        task_file_name = f
        break

task_file = join(task_path, task_file_name)
print("Task file: " + task_file)
if not os.path.exists(task_file):
    terminate = input("未发现任务清单{}, 按任意键退出".format(TASK_FILE))
    sys.exit(0)

# raw_str = input("请输入任务清单:")

try:
    raw_str = open(task_file, 'r', encoding='utf-8').read()
    dic = json.loads(raw_str)
except Exception as e:
    print("读取任务文件失败!")
    print(e)
    input("按任意键退出")
    sys.exit(0)
# print(dic)

timestamp = datetime.now().microsecond
download_root = "download\download_{}".format(timestamp)
if 'book-name' in dic:
    book_name = utils.verify_file_name(dic['book-name'])
    download_root = "download\{}_{}".format(book_name, timestamp)
    del dic['book-name']

tasks = []
for k in dic:
    chapter_name = utils.verify_file_name(k).replace("- 动漫之家漫画网", "")
    dir = "{}\{}".format(download_root, chapter_name)
    page_details = dic[k]
    i = 0
    for p in page_details:
        if TEST_AMOUNT > 0 and i > TEST_AMOUNT:
            break
        url = p['url']
        splits = url.split(":")
        while (len(splits) > 2):
            # http:https://xxxxxx.xxx
            start = len(splits[0]) + 1
            end = len(url)
            url = url[start: end]
            splits = url.split(":")
        task = {'url': url, 'file_name': p['file_name'], 'page': p['page']}
        task['dir'] = dir
        tasks.append(task)
        i = i + 1
    print("添加书目: ", chapter_name, "(", i, " pages)")

proxy = local_properties.PROXY_SERVER
config = {'proxy': proxy, 'referer': REFERER_DMZJ, 'ua': UA}

# ------下载
result = downloader.download(tasks, config=config)
failed_pages = []
if len(result) > 0:
    log_file = "{}\crwaler_log_{}.txt".format(download_root, timestamp)
    f = open(log_file, "w+")
    for item in result:
        f.write("{}\n".format(item))
        failed_pages.append(item['page'])
    f.write("Failed pages: \n{}\n".format(failed_pages))
    f.close()

# 改文件名
new_file = join(task_path, "finished_{}_{}".format(timestamp, task_file_name))
try:
    os.rename(task_file, new_file)
except BaseException as e:
    print("Something went wrong: ", type(e), str(e))

# 打开下载目录
to_open_path = "{}\{}\\".format(os.getcwd(), download_root)
print("Open:{}".format(to_open_path))
subprocess.Popen('explorer /select, {}'.format(to_open_path), shell=True)

# input("按任意键结束")
