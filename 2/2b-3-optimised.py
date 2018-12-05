from timeit import Timer


print("2b optimal attempt 2")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split()
inputFile.close()

def runTestPass():
	linelength = len(inputList[0])

	for x in range(linelength):
		items = set()
		lastLength = 0
		for i in inputList:
			newString = "%s%s" % (i[:x-1],i[x:])
			items.add(newString)
			if (len(items) == lastLength):
				print("Our string is %s", newString)
			else:
				lastLength = len(items)


print("2b-3\n----")
t = Timer("runTestPass()", "from __main__ import runTestPass")
print("Time: %s\n----------------" % t.timeit(number=1)) 

