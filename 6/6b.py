import sys
sys.path.append('../')
from scaffolding import common

inputList = common.loadInput('input.txt', True) #True = split, False = string
inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

print("Advent 6b.")

gridSize = max(max(inputNumbers, key=lambda x: max(x))) + 1 #one bigger as the gridcount starts at 0
maxDistance = 10000
regionSize = 0

for n in range(gridSize):
	for m in range(gridSize):
		count = 0

		for point in inputNumbers:
			count = count + abs(n - point[0]) + abs(m - point[1])

			if count >= maxDistance:
				continue

		if count < maxDistance:
			regionSize = regionSize + 1
			



#print(max(sizes.iteritems(), key=operator.itemgetter(1))[0])


print(regionSize)

#print(sizes)
