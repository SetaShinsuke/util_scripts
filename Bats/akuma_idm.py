import os
import sys
from urllib.parse import unquote

args = sys.argv
print(args)

# akuma-idm://xxx.com/xxx.jpg-----abc.jpg-----C:\Users\24783\Downloads\chapter_01
if (len(args) >= 2):
    params = args[1].replace('akuma-idm://', '')
    # os.system('pause')
    params = params.split('-----')
    url = params[0].replace('&', '^&').replace(' ', '` ')
    # 防止出现冒号被edge吞的情况 2024.10.20
    url = url.replace('http//', 'http://').replace('https//', 'https://')
    name = unquote(params[1])
    print('url: ')
    print(url)
    print('name: ')
    print(name)
    dir = f'C:\\Users\\24783\\Downloads\\Video'
    if (len(params) >= 3):  # 有目录参数
        dir = unquote(params[2])
    # cmd = f'"C:\\Program Files (x86)\\Internet Download Manage\\IDMan.exe" /p "{dir}" /f "{name}" /d "{url}"'
    cmd = f'cmd /C ""C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe" /n /p "{dir}" /f "{name}" /d "{url}""'
    print('\nCMD:')
    print(cmd)
    os.system(cmd)

# os.system('pause')
os.system('timeout 10')

# "C:\Users\24783\Documents\Shortcuts\akuma-scheme.bat" %1
