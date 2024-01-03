import os
import sys
from urllib.parse import unquote

args = sys.argv
print(args)

if (len(args) >= 2):
    params = args[1].replace('akuma-idm://', '')
    # os.system('pause')
    params = params.split('-----')
    url = params[0].replace('&', '^&').replace(' ', '` ')
    name = unquote(params[1])
    print(url)
    print(name)
    dir = f'C:\\Users\\24783\\Downloads\\Video'
    # cmd = f'"C:\\Program Files (x86)\\Internet Download Manage\\IDMan.exe" /p "{dir}" /f "{name}" /d "{url}"'
    cmd = f'cmd /C ""C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe" /n /p "{dir}" /f "{name}" /d "{url}""'
    print('\n')
    print(cmd)
    os.system(cmd)

# os.system('pause')
os.system('timeout 10')

# "C:\Users\24783\Documents\Shortcuts\akuma-scheme.bat" %1
