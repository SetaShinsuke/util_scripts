# -*- coding: utf-8 -*-  
import os
from os import listdir
from os.path import isfile,  join

# 要替换的字符串
org_str = "to_replace"
rst_str = "result"

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
	print "path: {}\nnew path: {}\n".format(file, new_file)
	os.rename(file, new_file)

	# if isfile(file):
	# 	print file
	# print "\n"