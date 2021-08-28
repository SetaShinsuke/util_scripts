# -*- coding: utf-8 -*-
# 直接考虑 tasks.json 已经获取到的情况, 参考 [Site_Dmzj]
#
# ---- 参考格式 ----
# {'config': {'book_name': xxx, 'referer': xxx}, 'chapter1': [...], 'chapter2': [...]...}
# 'chapter': {'url': xxxx, 'file_name': xxx, 可选 'page': xxxx}

import json
import os
from os import listdir
import subprocess
import sys
from datetime import datetime
from os.path import join
import shutil

sys.path.append('../../')
from Downloader import downloader
from Common import local_properties
from Common import utils

# todo: 测试数量
TEST_AMOUNT = -1

# 可配置项
CONFIG = 'config'
CONFIG_BOOK_NAME = 'book_name'
CONFIG_REFERER = 'referer'
CONFIG_PROXY = False

TASK_FILE = "tasks.json"
DOWNLOAD_DIR = 'dir'
FILE_NAME = 'file_name'
URL = 'url'

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"

task_path = join(os.getcwd(), "tasks")

# 任务结束后将文件名改掉!
task_file_name = TASK_FILE

step = utils.requireInt('按( ? )个章节打包: ')

if (step <= 0):
    step = False
else:
    # {'group_1': [{'chapter1': []}, {'chapter2': []}]..., 'group_2': ...}
    groups = {}
    config = False
    for f in listdir(task_path):
        if (not f.startswith('tasks')):
            continue
        # 读取Task
        task_json = {}
        try:
            f_full = join(task_path, f)
            raw_str = open(f_full, 'r', encoding='utf-8').read()
            task_json = json.loads(raw_str)
        except Exception as e:
            print("读取任务文件失败!")
            print(e)
            input("按任意键退出")
            sys.exit(0)
        if (task_json[CONFIG]):
            config = task_json[CONFIG]
            del task_json[CONFIG]
        # 分组
        index = -1
        # tasks_0.json
        try:
            index = int(f.split('.json')[0].split('tasks_')[-1])
            group = int(index // step)

            group_name = f'task_{group}'
            if (group_name in groups):
                groups[group_name].append(task_json)
            else:
                groups[group_name] = [task_json]
            os.remove(f_full)
        except BaseException as e:
            print(f'Sth wrong: {str(e)}, {e.args}')
    print('Tasks 已整理!')
    for task_group in groups:
        try:
            tasks = groups[task_group]
            tJson = {}
            for m in tasks:
                for k in m:
                    tJson[k] = m[k]

            print(tJson)
            with open(f'{join(task_path, task_group)}.json', 'w', encoding='utf8') as outfile:
                json.dump(tJson, outfile, ensure_ascii=False)
        except BaseException as e:
            print(f'Dump JSON error: {str(e)}')

to_open_path = "download"


def handleTask(task_file):
    print(f'Handle task: {task_file}')
    if (True):
        return

    task_file = join(task_path, task_file_name)
    if not os.path.exists(task_file):
        terminate = input("未发现任务清单{}, 按任意键退出".format(TASK_FILE))
        sys.exit(0)

    try:
        raw_str = open(task_file, 'r', encoding='utf-8').read()
        task_json = json.loads(raw_str)
    except Exception as e:
        print("读取任务文件失败!")
        print(e)
        input("按任意键退出")
        sys.exit(0)

    # 根文件夹名 \download\书名_2333450
    timestamp = datetime.now().microsecond
    download_root = "download\download_{}".format(timestamp)
    book_name = "{}".format(timestamp)
    referer = False
    proxy = False
    if (task_json[CONFIG] and len(task_json[CONFIG]) > 0):
        # 书名
        try:
            book_name = utils.verify_file_name(task_json[CONFIG][CONFIG_BOOK_NAME])
            download_root = "download\{}_{}".format(book_name, timestamp)
        except BaseException:
            pass
        # referer
        try:
            referer = task_json[CONFIG][CONFIG_REFERER]
        except BaseException:
            pass
        # 代理
        try:
            proxy = task_json[CONFIG][CONFIG_PROXY]
        except BaseException:
            pass
        del task_json[CONFIG]

    tasks = []
    for k in task_json:
        chapter_name = utils.verify_file_name(k)
        dir = "{}\{}".format(download_root, chapter_name)
        page_details = task_json[k]
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
            task = {'url': url, 'file_name': p['file_name']}
            if ('page' in p):
                task['page'] = p['page']
            task['dir'] = dir
            tasks.append(task)
            i = i + 1
        print("添加书目: ", chapter_name, "(", i, " pages)")

    # config = {'proxy': proxy, 'referer': REFERER_DMZJ, 'ua': UA}
    config = {'ua': UA}
    if (referer):
        config['referer'] = referer
    if (proxy):
        config['proxy'] = proxy

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
    else:  # 没有失败的任务
        # 改文件名
        new_file = join(task_path, "finished_{}_{}".format(timestamp, task_file_name))
        try:
            # todo: 改文件名
            # new_file = task_file
            os.rename(task_file, new_file)
            # 打包zip
            zip_path = join(os.getcwd(), download_root)
            shutil.make_archive(download_root, 'zip', zip_path)
        except BaseException as e:
            print("Something went wrong: ", type(e), str(e))


# main
for f in listdir(task_path):
    if f.startswith('task'):
        task_file_name = f
        handleTask(f)
        if (not step):
            break

# 打开下载目录
print("Open:{}".format(to_open_path))
os.startfile(to_open_path)
# popen_result = subprocess.Popen('explorer /select, {}'.format(to_open_path), shell=True)
# print("p_result: ", popen_result)

# input("按任意键结束")
