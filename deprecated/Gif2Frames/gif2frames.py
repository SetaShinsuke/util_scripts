# -*- coding: utf-8 -*-
from PIL import Image
file_name = input('Input file name: ')
im = Image.open(f'{file_name}.gif')

for i in range(12):
    im.seek(i)
    im.save(f'{file_name}_{i+1}.png')