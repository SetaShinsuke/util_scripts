# -*- coding: utf-8 -*-
import os
import re
import urllib.request

CONFIG_KEY_PROXY = "proxy"
CONFIG_KEY_REFERER = "referer"


def filter_fun(item):
    return item.startswith("http")


# config: 代理服务器等
def download_by_strs(urls_str, separator, dir_path, config=None):
    img_urls = urls_str.split(separator)
    download_by_list(img_urls, dir_path, config)


def download_by_list(img_urls, dir_path, config=None):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    img_urls = list(filter(filter_fun, img_urls))
    total = len(img_urls)
    downloaded = 0
    failed = 0
    max_amount = total
    # max_amount = 3
    print("max_amount: {}".format(max_amount))
    for img_url in img_urls:
        if downloaded >= max_amount:
            break
        print("url: {}".format(img_url))
        file_name = img_url.split('/')[-1].replace('\\', '_').replace('/', '_')
        file_name = re.sub('[\/:*?"<>|]', '-', file_name)
        if (len(file_name) > 150): # 文件名超长
            file_name = file_name[-149:]
        if os.path.exists("{}\{}".format(dir_path, file_name)): #检查重名
            name = file_name.split(".")[0]
            file_name = file_name.replace(name, "{}_{}".format(name, downloaded))
        print("Downloading {}/{} : {}".format(downloaded + 1, total, file_name))
        final_url = img_url

        opener = urllib.request.build_opener()
        print("config: {}".format(config))
        if config is not None and CONFIG_KEY_PROXY in config.keys():
            # 添加 http 代理
            proxy_server = config[CONFIG_KEY_PROXY]
            proxy = urllib.request.ProxyHandler({'http': proxy_server})
            opener = urllib.request.build_opener(proxy)
            print("使用代理: {}".format(proxy_server))
        if config is not None and CONFIG_KEY_REFERER in config.keys():
            # 添加 referer
            referer_host = config[CONFIG_KEY_REFERER]
            opener.addheaders = [('Referer', referer_host)]
            print("使用referer: {}".format(referer_host))
        urllib.request.install_opener(opener)

        try:
            resp = urllib.request.urlretrieve(final_url, "{}\{}".format(dir_path, file_name))
        except Exception as err:
            print("----\nSomething wrong happened!")
            print(type(err))
            print(err.args)
            print(err)
            print("----")
            failed += 1
            pass
        downloaded += 1
    print(u"Download finished {}/{}!\nSaved at \{}".format(downloaded, total, dir_path))
    if failed > 0:
        print("{}\{} download failed!!".format(failed, total))
