# -*- coding: utf-8 -*-
from datetime import datetime
import sys

sys.path.append('../')
from Downloader import downloader
from Common import local_properties

separator = "---n---"
img_urls = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1435198787,338833352&fm=26&gp=0.jpg"
img_urls += separator

# 测试代理
# img_urls += "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
# img_urls += seperator

img_urls += "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1435198787,338833352&fm=26&gp=0.jpg"
img_urls += separator

img_urls += "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=4199386165,4259832396&fm=26&gp=0.jpg"
img_urls += separator

img_urls += "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604999723554&di=c4d8a52e7676b78a18e25c648ff041b2&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201609%2F24%2F20160924023109_khXSy.jpeg"
# print("start download...")
img_urls += separator

dir_path = "download\{}_{}".format("download_test", datetime.now().microsecond)
# downloader.download_by_strs(img_urls, seperator, dir_path)
# config = {'proxy':  local_properties.PROXY_SERVER, 'referer': 'https://www.google.com/'}
# downloader.download_by_strs(img_urls, seperator, dir_path, config)

img_urls = img_urls.split(separator)
tasks = []
i = 0
for img in img_urls:
    i += 1
    print("{} url: {}".format(i, img))
    tasks.append({'url': img, 'file_name': '{}.jpg'.format(i)})

downloader.download(tasks, dir_path)
