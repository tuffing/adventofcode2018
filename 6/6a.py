import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict

inputList = common.loadInput('input.txt', True) #True = split, False = string
inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

print("Advent 6a.")

gridSize = max(max(inputNumbers, key=lambda x: max(x))) + 1 #one bigger as the gridcount starts at 0
pointIsInfinite = set()

sizes = defaultdict(int)

for n in range(gridSize):
	for m in range(gridSize):
		smallestDistance = None
		closest = None
		closestIndex = 0

		for index,point in enumerate(inputNumbers):
			dist = abs(n - point[0]) + abs(m - point[1])
			if smallestDistance is None or dist < smallestDistance:
				#print(index)
				smallestDistance = dist
				closestIndex = index
				closest = point
			elif dist == smallestDistance:
				closest = None

		if closest is not None:
			pointString = '%d,%d' % (closest[0],closest[1])
			sizes[pointString] = sizes[pointString] + 1

		if closest is not None and (n == 0 or n == gridSize-1 or m == 0 or m == gridSize-1):
			pointIsInfinite.add('%d,%d' % (closest[0],closest[1]))

#print(max(sizes.iteritems(), key=operator.itemgetter(1))[0])
print(sizes)
for key in pointIsInfinite:
	sizes.pop(key)

print(max(sizes.values()))

#print(sizes)
