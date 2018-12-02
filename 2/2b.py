import jellyfish
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


print('Find Each rows best Match')
processMatches()

print('Find the set with the lowest score')
lowestScore = findMatchWithLowestScore()

print('The common letters are %s' % ''.join(list(filter(lambda x:x in list(lowestScore), bestMatchPerColumn[lowestScore]['match']))))
