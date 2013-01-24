import os
import sys
import getopt

def walkDir(dir):
	generator_ = os.walk(dir)
	for rootDir, pathList, fileList in generator_ :
		for f in fileList:
			#print(os.path.join(rootDir, f))
			write2file_2(os.path.join(rootDir, f), ["blablablabla\n", "xxxxx\n"])

#def displayDir2(dir):
#    for i in os.listdir(dir):
#        file = os.path.join(dir,i)
#        if os.path.isdir(file):
#            displayDir2(file)
#        else:
#            print file

def write2file(filepath, str_):
	f = open(filepath, 'r+')
	original_content = f.read()
	f.seek(0)
	print("original content: " + original_content)
	new_content = str_ + '\n' + original_content
	print("new content: " + new_content)
	f.write(new_content)
	f.close()

def write2file_2(filepath, strList):
	f = open(filepath, 'r+')
	content = f.readlines()
	#content = ["blablabla\n", "lskdfsdk\n", "xxxxx\n"] + content
	content = strList + content
	f.seek(0)
	f.writelines(content)
	f.close()

def print_tree_(dir_, parent_prefix, current_level, depth, only_dir):
	'''
	print the guide line of 'dir_' for 'depth'.

	dir_ : the directory to print
	parent_prefix : the string attach in front of the guide line, '' is recommanded
	current_level : the starting level, 0 is recommanded
	depth : 0 or less mean NO depth limited
	only_dir : true if only print directory

	Thoughts:
		For every line to print, first print the parent's prefix,
		then print the own prefix, and at last, print the name of files/dirs.
	'''

	if depth > 0 and current_level >= depth:
		return None
	# current_level starts from 0, depth starts from 1.
	current_level += 1

	NORMAL_PREFIX = '|-- '
	NORMAL_PREFIX_4_CHILDREN = '|   '
	LAST_PREFIX = '|-- '
	LAST_PREFIX_4_CHILDREN = '    '
	
	# TODO: now the list is sorted by alphabeta, they can also be sorted by other.
	# e.g. sorted by modified time.
	child_list = os.listdir(dir_)
	child_list_size = len(child_list)
	
	index = 0
	while(index < child_list_size):
		child_name = child_list[index]
		child_path = os.path.join(dir_, child_name)
		if os.path.isdir(child_path):
			# deal with the non-last children of THIS level. For files, this will be the same.
			if index < child_list_size - 1:
				print(parent_prefix + NORMAL_PREFIX + str(child_name) + '\n', end='')
				print_tree_(child_path, parent_prefix + NORMAL_PREFIX_4_CHILDREN, current_level, depth, only_dir)
			# deal with the last child of THIS level, sometimes, its prefix is different from prefix of others.
			# For files, this will be the same.
			else:
				print(parent_prefix + LAST_PREFIX + str(child_name) + '\n', end='')
				print_tree_(child_path, parent_prefix + LAST_PREFIX_4_CHILDREN, current_level, depth, only_dir)
		else:
			if not only_dir:
				if index < child_list_size - 1:
					print(parent_prefix + NORMAL_PREFIX + str(child_name) + '\n', end='')
				else:
					print(parent_prefix + LAST_PREFIX + str(child_name) + '\n', end='')

		index += 1

def print_tree():
	'''Usage:
	utils.py [--dir=xxx] [--depth=xxx] [--only_dir] [--help]
	'''

	# these are the default values.
	dir_ = '.'
	depth = 0
	only_dir = False

	# short argv list must provided to 'getopt'
	shortargv = ''
	longargv = ['dir=', 'depth=', 'only-dir', 'help']
	try:
		(opts, args) = getopt.getopt(sys.argv[1:], shortargv, longargv)
	except getopt.GetoptError as e:
		print("Errors accured when get options using 'getopt', please check out your options.")
		print("Error:: opt: " + e.opt)
		print("Error:: msg: " + e.msg)
		return None
	
	for (opt, val) in opts:
		if opt == '--help':
			print("Usage: utils.py [--dir=xxx] [--depth=xxx] [--only_dir] [--help]")
			return None
		elif opt == '--dir' and len(val) > 0:
			dir_ = val
		elif opt == '--depth' and len(val) > 0 and int(val) > 0:
			depth = int(val)
		elif opt == '--only_dir':
			only_dir = True

	if not os.path.isdir(dir_):
		print(str(dir_) + " is not a directory.")
		return None
	print(dir_)
	print_tree_(dir_, '', 0, depth, only_dir)


def filter_files(base_folder, filtered_folder):
	'''filter files in filtered_folder. If a file is in base_folder,
	then filter out it from filtered_folder if exists.
	e.g. filter_files('res/hdpi/', 'res/xhdpi/')
	filter files which are in hdpi/ out from xhdpi/ if exists.
	'''
	if not os.path.isdir(base_folder) or not os.path.isdir(filtered_folder):
		print("Make sure both '%s' and '%s' are folders." % (str(base_folder), str(filtered_folder)))
		return None
	file_list_base = os.listdir(base_folder)
	file_list_addon = os.listdir(filtered_folder)

	count = 0
	for x in file_list_addon:
		path = os.path.join(filtered_folder, x)
		#path = os.path.realpath(x)
		if os.path.isfile(path) and x in file_list_base:
			os.remove(path)
			count += 1
	print("delete %d files." % count)

if __name__ == '__main__':
	#walkDir("E:/python/tmp")
	#print_tree()
	filter_files('tmp_1', '')
