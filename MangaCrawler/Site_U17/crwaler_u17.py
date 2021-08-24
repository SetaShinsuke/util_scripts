# -*- coding: utf-8 -*-

from urllib import request
import json

from Downloader.downloader import CONFIG_KEY_UA
from u17_urls import BOOK_URL, CHAPTER_URL

import sys
import os
from pathlib import Path

sys.path.append('../../')
from Downloader import downloader
from Common import utils

from datetime import datetime
from os.path import join
import shutil

MAX_RETRY = 2
FILE_TAIL = '-_1'
header_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}


def load_book():
    # book_id = '53591'
    book_id = input("输入漫画ID: ")
    # 《超合金社团》ID: 53591

    book_url = BOOK_URL + "" + book_id

    req = request.Request(book_url, headers=header_dict)
    print("req: {}".format(req))

    try:
        # 发送请求
        print("正在获取漫画数据...")
        result = request.urlopen(req)
        result = str(result.read(), encoding='utf-8')
        result_json = json.loads(result)
        data = result_json['data']['returnData']
        print('漫画数据已获取!')
        return data
    except BaseException as e:
        print("Something went wrong: ", type(e), str(e))
        return False


# -----------------------------
# MAIN()
# [{chapter_name: '第一话', chapter_ids: [1001, 1002...], tasks: []}, ...]
chapter_sorted = []
sub_chapter_total = 0

book_data = load_book()
if (book_data):
    comic_name = book_data['comic']['name']
    author_name = book_data['comic']['author']['name']
    book_name = comic_name + "-" + author_name
    print('Book name: ' + book_name)

    chapter_list = book_data['chapter_list']
    print('章节总数: {}'.format(len(chapter_list)))

    start = int(input('请输入开始章节: ')) - 1
    end = int(input('请输入结束章节: '))
    if (start < 0):
        start = 0
    if (end > len(chapter_list)):
        end = len(chapter_list)
    sub_list = chapter_list[start: end]
    sub_chapter_total = len(sub_list)

    print('start: {}, end: {}'.format(start, end))

    # 整理章节数据
    for item in sub_list:
        name = item['name']
        name = ''.join([i for i in name if not i.isdigit()]).replace('I', '').replace(
            'V', '').replace(' ', '').replace('fcan', 'If I Can')
        # 这个不规则命名真的乌鸡鲅鱼
        image_total = item['image_total']
        chapter_id = item['chapter_id']
        # 整合章节名一样的子章节
        if (len(chapter_sorted) > 0 and chapter_sorted[-1]['chapter_name'] == name):
            chapter_sorted[-1]['chapter_ids'].append(chapter_id)
        else:
            chapter_sorted.append({'chapter_name': name, 'chapter_ids': [chapter_id]})

    # -----------------------
    # 章节整理完毕
    print(chapter_sorted)
    print('------------------------')
    # 挨个获取章节数据
    sub_index = 0
    file_index = 0
    for chapter in chapter_sorted:
        chapter['tasks'] = []
        for id in chapter['chapter_ids']:
            chapter_url = CHAPTER_URL + "" + id
            req = request.Request(chapter_url, headers=header_dict)
            print("req: {}".format(req))
            retry = 0
            while (retry <= MAX_RETRY):
                try:
                    # 发送请求
                    print("正在获取[{}/{}]数据...".format(sub_index + 1, sub_chapter_total))
                    result = request.urlopen(req)
                    result = str(result.read(), encoding='utf-8')
                    result_json = json.loads(result)
                    image_list = result_json['data']['returnData']['image_list']
                    for img in image_list:
                        file_index += 1
                        chapter['tasks'].append(
                            {'url': img['location'], 'file_name': '{:03d}.jpg'.format(file_index)})
                    print('[{}/{}]数据已获取!'.format(sub_index + 1, sub_chapter_total))
                    sub_index += 1
                    break
                except BaseException as e:
                    print("Something went wrong: ", type(e), str(e))
                    print('retry: {}'.format(retry))
                    retry += 1

        print('chapter: ' + chapter['chapter_name'])
        print(chapter['tasks'])

    # ----------
    # 开始进行下载
    # download\超合金社团_1123444-_1-_1
    folder_name = utils.verify_file_name(comic_name)
    download_root = "download\{}{}".format(folder_name, FILE_TAIL)
    while (Path(download_root).is_dir()):  # 文件夹已存在
        download_root = download_root + FILE_TAIL
    to_open_path = "download"
    print('正在开始下载, 目标目录: {}'.format(download_root))

    for chapter in chapter_sorted:
        chapter_name = chapter['chapter_name']
        # download\超合金社团\第一话
        dir = "{}\{}".format(download_root, chapter_name)
        tasks = chapter['tasks']
        config = {CONFIG_KEY_UA: header_dict['User-Agent']}
        result = downloader.download(tasks,config=config, dir_path=download_root)
        failed_pages = []
        if len(result) > 0:
            timestamp = datetime.now().microsecond
            log_file = "{}\crwaler_log_{}.txt".format(download_root, timestamp)
            f = open(log_file, "w+")
            for item in result:
                f.write("{}\n".format(item))
                failed_pages.append(item['page'])
            f.write("Failed pages: \n{}\n".format(failed_pages))
            f.close()
        else:  # 全部下载成功
            try:
                # 打包zip, 超合金社团-2.zip
                zip_path = join(os.getcwd(), download_root)
                no = len(download_root.split(FILE_TAIL)) - 1
                shutil.make_archive('download\{}-{}'.format(comic_name, no), 'zip',
                                    zip_path)
            except BaseException as e:
                print("Something went wrong: ", type(e), str(e))

    # 打开下载目录
    print("Open:{}".format(to_open_path))
    os.startfile(to_open_path)
