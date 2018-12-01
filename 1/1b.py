print("Advent 1.b")

inputFile = open('test-input-answer-10.TXT', 'r')
inputList = inputFile.read().strip().split()
inputFile.close()


def findRepeat():
	currentFrequency = 0;
	frequencyList = []
	
	while (True):
		print("*")
		for change in inputList:
			currentFrequency += int(change)

			if currentFrequency in frequencyList:
				return currentFrequency
			else:
				frequencyList.append(currentFrequency)



print("The first repeated frequency %d" % findRepeat())