import os, sys, shutil

dayName = sys.argv[1]

#dir is not keyword
def createDir(name):
  try:
    os.makedirs(name)
  except OSError:
    pass


createDir(dayName)

path = os.path.dirname(os.path.abspath(__file__))
shutil.copyfile('%s/scaffolding/standard.py' % path, '%s/%s/%sa.py' % (path,dayName,dayName))
shutil.copyfile('%s/scaffolding/standard.py' % path, '%s/%s/%sb.py' % (path,dayName,dayName))

#put in the base code that we use on every part
titleA = "print(\"Advent %sa.\")" % dayName
with open("%s/%sa.py" % (dayName, dayName), "a") as partA:
    partA.write(titleA)
partA.close()

titleB = "print(\"Advent %sb.\")" % dayName
with open("%s/%sb.py" % (dayName, dayName), "a") as partB:
    partB.write(titleB)
partB.close()


