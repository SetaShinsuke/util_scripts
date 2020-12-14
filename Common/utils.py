# -*- coding: utf-8 -*-
import re
import urllib.parse
import pyperclip


def verify_file_name(file_name):
    file_name = file_name.replace('\\', '_').replace('/', '_')
    file_name = re.sub('[\/:*?"<>|]', '-', file_name)
    if (len(file_name) > 150):  # 文件名超长
        file_name = file_name[-149:]
    return file_name


def url_encode(string, encoding='utf-8'):
    return urllib.parse.quote(string, encoding)


def url_decode(string, encoding='utf-8'):
    return urllib.parse.unquote(string, encoding)

def copy_to_clipboard(string):
    pyperclip.copy(string)
