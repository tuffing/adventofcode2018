import jellyfish
from timeit import Timer
from collections import deque

print("Advent 2.b")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split()
inputFile.close()


bestMatchPerColumn = {}

def processMatches():
	inputQueue = deque(inputList)

	row = inputQueue.pop()
	while row is not None:
		bestMatchScore = -1
		bestMatchRow = ''
		for rowToCompare in inputQueue:
			score = jellyfish.levenshtein_distance(row, rowToCompare)
			if bestMatchScore == -1 or score < bestMatchScore:
				bestMatchScore = score
				bestMatchRow = rowToCompare

		bestMatchPerColumn[row] = {'match': bestMatchRow, 'score': bestMatchScore}

		if len(inputQueue) > 1:
			row = inputQueue.pop()
		else:
			return


def findMatchWithLowestScore():
	lowestSoFar = None
	for row,match in bestMatchPerColumn.items():
		if lowestSoFar is None or bestMatchPerColumn[lowestSoFar]['score'] > match['score']:
			lowestSoFar = row
	
	return lowestSoFar


def runCalculations():
	print('Find Each rows best Match')
	processMatches()

	print('Find the set with the lowest score')
	lowestScore = findMatchWithLowestScore()

	print('The common letters are %s' % ''.join(list(filter(lambda x:x in list(lowestScore), bestMatchPerColumn[lowestScore]['match']))))


print("Using levenshtein_distance\n----")
t = Timer("runCalculations()", "from __main__ import runCalculations")
print("Time: %s\n----------------" % t.timeit(number=1)) #5


def processMatchesHammingDistance():
	inputQueue = deque(inputList)

	row = inputQueue.pop()
	while row is not None:
		bestMatchScore = -1
		bestMatchRow = ''
		for rowToCompare in inputQueue:
			score = jellyfish.hamming_distance(row, rowToCompare)
			if bestMatchScore == -1 or score < bestMatchScore:
				bestMatchScore = score
				bestMatchRow = rowToCompare

		bestMatchPerColumn[row] = {'match': bestMatchRow, 'score': bestMatchScore}

		if len(inputQueue) > 1:
			row = inputQueue.pop()
		else:
			return

def runCalculations2():
	print('Find Each rows best Match')
	processMatchesHammingDistance()

	print('Find the set with the lowest score')
	lowestScore = findMatchWithLowestScore()

	print('The common letters are %s' % ''.join(list(filter(lambda x:x in list(lowestScore), bestMatchPerColumn[lowestScore]['match']))))



print("Using Hamming distance\n----")
t = Timer("runCalculations2()", "from __main__ import runCalculations2")
print("Time: %s\n----------------" % t.timeit(number=1)) #.05