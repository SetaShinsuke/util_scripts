# -*- coding: utf-8 -*-
from datetime import datetime
import os
import sys
from os import listdir
from os.path import isfile, join

from PIL import Image

path = input("请输入图片路径:")

if (len(path) <= 0):  # 当前目录
    print("未输入, 将在当前目录进行操作!")
    path = os.getcwd()
print("current path: {}".format(path))
print("Start convert...\n")

dir = "{}\converted_{}".format(path, datetime.now().microsecond)

total = 0
success = 0
fail = 0
for f in listdir(path):
    f_abs = "{}\{}".format(path, f)
    if os.path.isfile(f_abs) and f.split(".")[-1] == "webp":
        total += 1
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
            im = Image.open(f_abs).convert("RGB")
            im.save("{}\{}.jpg".format(dir, f.split(".")[0]), "jpeg")
            success += 1
        except Exception as e:
            fail += 1
            print(e)
            continue

print("Convert finished!\n{}\{} Success!".format(success, total))
if fail > 0:
    print("Fail: ", fail)
print("\n")
