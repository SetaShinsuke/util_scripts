# -*- coding: utf-8 -*-  
import os
from os import listdir
from os.path import isfile,  join

import  sys
reload(sys)
sys.setdefaultencoding('utf-8')

# hint: unicode
# return: unicode
def r_in(hint):
    return raw_input(hint.encode(sys.stdout.encoding)).decode(sys.stdin.encoding)

# content: unicode
# return: str
def r_out(content):
	ret = ""
	try:
		ret = content.encode(sys.stdout.encoding)
	except BaseException, e:
		# print "Cannot print as wish, try print unicode...", type(e), str(e)
		ret = content.encode("utf-8")
	return ret

# unicode -> str 并打印
def r_print(content):
    print r_out(content)

# 要替换的字符串
# --------------------------------------
org_str = u"™"
rst_str = u""
# --------------------------------------
while len(org_str)<=0 :
	org_str = r_in(u"请输入要替换掉的字符:")

# 打印一个 unicode，在打印一个 str
print u"要修改的字符: ", r_out(org_str)
rst_str = r_in(u"将其修改为:")

# 打印一整个 str, decode 在内部完成s
print r_out(org_str)
print r_out(rst_str)
# print "replace \"{}\" to \"{}\"".format(r_out(org_str), r_out(rst_str))

path = u"{}".format(os.getcwd())
print "current path: {}".format(path)
print "-----------------\n"

i = 0
for f in listdir(path):
	# 因为 path 是 unicode 对象，所以 listdir 的结果也都是 unicode，需要手动 encode 之后输出
	# print "type f: ", type(f), "\nf: ", f
	# print "type org_str:", type(org_str), "\norg_str: ", org_str
	if org_str in f :
		i = i+1
		# print "{} contains 'test' - {}".format(f,  i)
		file = join(path, f.encode("utf-8","ignore")) # 手动 encode
		new_file = join(path, f.replace(org_str, rst_str))
		if file != new_file:
			print "path: {}\nnew path: {}\n".format(r_out(file), r_out(new_file))
			try:
				os.rename(file, new_file)
			except BaseException, e:
				print "Something went wrong: ", type(e), str(e)

	# if isfile(file):
	# 	print file
	# print "\n"

r_in("Success!\nPress any key to exit ...")