# -*- coding: utf-8 -*-
import os
from os import listdir
from Common.utils import flush, flush_reset

path = input('请输入图片目录:')

if (len(path) <= 0):  # 当前目录
    path = os.getcwd()
    print("current path: {}".format(path))
    print("-----------------\n")

biggers_dir = os.path.join(path, 'biggers')
if(not os.path.isdir(biggers_dir)):
    os.makedirs(biggers_dir)
print(f'Biggers path: {biggers_dir}')

i = 0
moved = 0
for f in listdir(path):
    i += 1
    if (f.endswith('.jpg')):
        png_file = f.replace('.jpg', '.png')
        jpg_path = os.path.join(path, f)
        png_path = os.path.join(path, png_file)
        if (os.path.exists(png_path)):
            jpg_size = os.path.getsize(jpg_path)
            png_size = os.path.getsize(png_path)
            to_move = png_file
            if (jpg_size > png_size):
                to_move = f
            flush(f'Moving file: {to_move}')
            os.rename(os.path.join(path, to_move), os.path.join(biggers_dir, to_move))
            moved += 1

flush_reset()
print(f'{moved}/{i} file moved.')