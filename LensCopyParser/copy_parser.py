# -*- coding: utf-8 -*-
import os
import sys
from os.path import join


sys.path.append('../')
from Common import utils

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

# 输入[r]继续
FLAG = "r"

def main():
    input_file = join(os.getcwd(), INPUT_FILE)

    print("Input file: " + input_file)
    if not os.path.exists(input_file):
        terminate = input("未发现任务清单{}, 按任意键退出".format(INPUT_FILE))
        sys.exit(0)

    # raw_str = input("Input text: ")

    try:
        raw_str = open(input_file, 'r', encoding='utf-8').read()
        print("Input text: \n{}".format(raw_str))
    except Exception as e:
        print("读取任务文件失败!")
        print(e)
        input("按任意键退出")
        sys.exit(0)

    result_str = raw_str.replace(" ", "").replace(",", "，").replace("?", "？").replace("\n\n","\n")
    print("result str: \n{}".format(result_str))
    utils.copy_to_clipboard(result_str)
    print("result str copied!")

    return input("Success!\nPress ["+ FLAG +"] to rename again\nOtherwise to EXIT\n")

is_resume = True
while (is_resume) :
    # print "\n" + str(resume)
    result = main()
    print("Input: " + str(result))
    is_resume = (result == FLAG)



