print("Advent 2.a")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split()
inputFile.close()
totals = [0,0]

def findDuplicates():
	for line in inputList:
		characters = list(line)
		characters.sort()
		duplicatesFound = False
		triplicatesFound = False
		
		letterCount = 1
		lastLetter = ''
		for letter in characters:
			if letter == lastLetter:
				letterCount = letterCount + 1
			else:
				lastLetter = letter
				duplicatesFound = duplicatesFound or isDuplicates(letterCount)
				triplicatesFound = triplicatesFound or isTriplicates(letterCount)
				letterCount = 1

		duplicatesFound = duplicatesFound or isDuplicates(letterCount)
		triplicatesFound = triplicatesFound or isTriplicates(letterCount)

def isDuplicates(letterCount):
	if letterCount == 2:
		totals[0] = totals[0] + 1
		return True

	return False

def isTriplicates(letterCount):
	if letterCount == 3:
		totals[1] = totals[1] + 1
		return True
	return False

findDuplicates()

#test = map(countXinARow, inputList)
print('twos: %d, threes: %d, multipled: %d' % (totals[0], totals[1], totals[0]*totals[1]))
