# -*- coding: utf-8 -*-  
import os
from os import listdir
from os.path import isfile,  join

import  sys
reload(sys)
sys.setdefaultencoding('utf-8')

def r_in(hint):
    return raw_input(hint.encode(sys.stdin.encoding))

def r_out(content):
    return content.encode(sys.stdout.encoding)


def r_print(content):
    print r_out(content)

# 要替换的字符串
org_str = ""
while len(org_str)<=0 :
	org_str = r_in("请输入要替换掉的字符:")

rst_str = r_in("将其修改为:")

print "replace \"{}\" to \"{}\"".format(org_str, rst_str)

path = "{}".format(os.getcwd())
print "current path: {}".format(path)
print "-----------------\n"

i = 0
for f in listdir(path):
	if org_str in f :
		i = i+1
		# print "{} contains 'test' - {}".format(f,  i)
	file = join(path, f)
	new_file = join(path, f.replace(org_str, rst_str))
	if file != new_file:
		print "path: {}\nnew path: {}\n".format(file, new_file)
	os.rename(file, new_file)

	# if isfile(file):
	# 	print file
	# print "\n"

r_in("Success!\nPress any key to exit ...")