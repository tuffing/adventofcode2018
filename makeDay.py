#!/usr/bin/python3
#
import os, sys, shutil, stat


class Makeday(object):

	def generate(self, dayName):
		#dir is not keyword
		def createDir(name):
		  try:
		    os.makedirs(name)
		  except OSError:
		    pass


		createDir(dayName)


		path = os.path.dirname(os.path.abspath(__file__))
		#solution files
		shutil.copyfile('%s/scaffolding/standard.py' % path, '%s/%s/sol%sa.py' % (path,dayName,dayName))
		shutil.copyfile('%s/scaffolding/standard.py' % path, '%s/%s/sol%sb.py' % (path,dayName,dayName))

		#unittests
		shutil.copyfile('%s/scaffolding/solutiontest.py' % path, '%s/%s/test%sa.py' % (path,dayName,dayName))
		shutil.copyfile('%s/scaffolding/solutiontest.py' % path, '%s/%s/test%sb.py' % (path,dayName,dayName))

		#test input
		shutil.copyfile('%s/scaffolding/testInput.txt' % path, '%s/%s/testInput.txt' % (path,dayName))

		#set executable on all the scripts
		#solution files
		st = os.stat('%s/%s/sol%sa.py' % (path,dayName,dayName))
		os.chmod('%s/%s/sol%sa.py' % (path,dayName,dayName), st.st_mode | stat.S_IEXEC)
		st = os.stat('%s/%s/sol%sb.py' % (path,dayName,dayName))
		os.chmod('%s/%s/sol%sb.py' % (path,dayName,dayName), st.st_mode | stat.S_IEXEC)
		
		#test files
		st = os.stat('%s/%s/test%sa.py' % (path,dayName,dayName))
		os.chmod('%s/%s/test%sa.py' % (path,dayName,dayName), st.st_mode | stat.S_IEXEC)

		st = os.stat('%s/%s/test%sb.py' % (path,dayName,dayName))
		os.chmod('%s/%s/test%sb.py' % (path,dayName,dayName), st.st_mode | stat.S_IEXEC)

if __name__ == '__main__':
	Makeday().generate(sys.argv[1])


