import os
import sys
import shutil

''' remove the .svn/ dirs.'''

def rmsvn(path):
	for (rootdir, dirs, files) in os.walk(path):
		for dirname in dirs:
			if dirname == ".svn":
				shutil.rmtree(os.path.join(rootdir, dirname), ignore_errors=True)
	print("remove '.svn' dirs complete.")

if __name__ == '__main__':
	#for arg in sys.argv:
	#	print(arg)
	path = sys.argv[1]
	rmsvn(path)