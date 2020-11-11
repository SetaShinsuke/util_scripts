# -*- coding: utf-8 -*-
import json
import os
import subprocess
import sys
from datetime import datetime

sys.path.append('../../')
from Downloader import downloader
from Common import local_properties
from Common import utils

TASK_FILE = "tasks.txt"
DOWNLOAD_DIR = 'dir'
FILE_NAME = 'file_name'
URL = 'url'

REFERER_DMZJ = "http://manhua.dmzj.com/"
UA = "Mozilla/5.0"

here = os.getcwd()
task_file = "{}\{}".format(here, TASK_FILE)

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
tasks = []
for k in dic:
    book_name = utils.verify_file_name(k).replace("- 动漫之家漫画网", "")
    dir = "{}\{}".format(download_root, book_name)
    page_details = dic[k]
    i = 0
    for p in page_details:
        # todo: 测试数量
        # if i > 2:
        #     break
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
    print("添加书目: ", book_name, "(", i, " pages)")

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

# 打开下载目录
to_open_path = "{}\{}\\".format(os.getcwd(), download_root)
print("Open:{}".format(to_open_path))
subprocess.Popen('explorer /select, {}'.format(to_open_path), shell=True)

# input("按任意键结束")
