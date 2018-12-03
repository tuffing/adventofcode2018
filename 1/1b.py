from timeit import Timer

print("Advent 1.b")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split()
inputFile.close()


def findRepeat():
	currentFrequency = 0;
	frequencyList = []
	
	while (True):
		for change in inputList:
			currentFrequency += int(change)

			if currentFrequency in frequencyList:
				print("The first repeated frequency %d" % currentFrequency)
				return currentFrequency
			else:
				frequencyList.append(currentFrequency)


print("Naive bruteforce approach\n----")
t = Timer("findRepeat()", "from __main__ import findRepeat")
print("Time: %s\n----------------" % t.timeit(number=1)) # 62.72738941095304


def findRepeatUsingSets():
	currentFrequency = 0;
	previousSetSize = 0;
	frequencyList = set()
	
	while (True):
		for change in inputList:
			currentFrequency += int(change)
			frequencyList.add(currentFrequency)

			if len(frequencyList) == previousSetSize:
				print("The first repeated frequency %d" % currentFrequency)
				return currentFrequency

			previousSetSize = len(frequencyList)

print("Using sets instead, exploiting that the set size will not increase if it receives a duplicate\n----")
t2 = Timer("findRepeatUsingSets()", "from __main__ import findRepeatUsingSets")
print("Time: %s \n----------------" % t2.timeit(number=1)) # 0.03885865292977542
