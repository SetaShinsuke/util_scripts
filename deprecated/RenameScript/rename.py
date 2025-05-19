# -*- coding: utf-8 -*-  
import os
from os import listdir
from os.path import isfile,  join

import  sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 要替换的字符串
# --------------------------------------
org_str = ""
rst_str = ""
path = ""
# --------------------------------------

# 输入[r]继续重命名
FLAG = "r"

# hint: unicode
# return: unicode
def r_in(hint):
    return input(hint)
    # return raw_input(hint.encode(sys.stdout.encoding)).decode(sys.stdin.encoding)

# content: unicode
# return: str
def r_out(content):
    return content
    # ret = ""
    # try:
    #     ret = content.encode(sys.stdout.encoding)
    # except BaseException as e:
    #     # print "Cannot print as wish, try print unicode...", type(e), str(e)
    #     ret = repr(content)
    # return ret

# unicode -> str 并打印
def r_print(content):
    print(r_out(content))

def uni_chk(content):
    if(content.startswith("\\u")): # \u 开头
        try:
            content = unichr(int(content[2:], 16))
            print("自动转换为 unicode 字符: ", r_out(content))
        except BaseException as e:
            print("Unicode trans error: ", type(e), str(e))
            content = ""
    return content

# 输入要执行的目录
rename_path = r_in(u"请输入目标目录: ")
if len(rename_path) <= 0:
    print("未输入, 将在当前目录进行操作!")

def main():
    org_str = u""
    rst_str = u""
    # 输入要修改的字符
    while len(org_str)<=0 :
        org_str = r_in(u"请输入要替换掉的字符:")
        org_str = uni_chk(org_str)
    
    # 打印一个 unicode，在打印一个 str
    print("要修改的字符: ", r_out(org_str))
    rst_str = r_in(u"将其修改为:")
    rst_str = uni_chk(rst_str)
    
    # 打印一整个 str, decode 在内部完成s
    print(r_out(org_str))
    print(r_out(rst_str))
    # print "replace \"{}\" to \"{}\"".format(r_out(org_str), r_out(rst_str))
    
    # 读取当前目录，返回值是 str，按照 系统编码 解码成 unicode 使用    
    path = rename_path
    if(len(path) <= 0):  #当前目录
        path = os.getcwd().decode(sys.stdin.encoding)
    print("current path: {}".format(r_out(path)))
    print("-----------------\n")
    
    i = 0
    for f in listdir(path):
        # 因为 path 是 unicode 对象，所以 listdir 的结果也都是 unicode，需要手动 encode 之后输出
        # print "type f: ", type(f), "\nf: ", f
        # print "type org_str:", type(org_str), "\norg_str: ", org_str
        if org_str in f :
            i = i+1
            # print "{} contains 'test' - {}".format(f,  i)
            # file = join(path, f.encode("utf-8","ignore")) # 手动 encode -> str
            file = join(path, f)
            new_file = join(path, f.replace(org_str, rst_str))
            if file.endswith(u".py") or file.endswith(u".exe"):
                print("PY file or EXE file, skip!")
                continue
            if file != new_file:
                print("path: {}\nnew path: {}\n".format(r_out(file), r_out(new_file)))
                try:
                    os.rename(file, new_file)
                except BaseException as e:
                    print("Something went wrong: ", type(e), str(e))
    
        # if isfile(file):
        #     print file
        # print "\n"
    
    return r_in("Success!\nPress ["+ FLAG +"] to rename again\nOtherwise to EXIT\n")

is_resume = True
while (is_resume) :
    # print "\n" + str(resume)
    result = main()
    print("Input: " + str(result))
    is_resume = (result == FLAG)

# r_in("Success!\nPress any key to exit ...")