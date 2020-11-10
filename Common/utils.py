# -*- coding: utf-8 -*-
import re


def verify_file_name(file_name):
    file_name = file_name.replace('\\', '_').replace('/', '_')
    file_name = re.sub('[\/:*?"<>|]', '-', file_name)
    if (len(file_name) > 150):  # 文件名超长
        file_name = file_name[-149:]
    return file_name
