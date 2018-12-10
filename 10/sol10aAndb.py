#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict, Counter


class Solution(object):

	def __init__(self):
		pass

	def solution(self, inputList):
		inputNumbers = common.pullNumbersFromList(inputList, True) 

		count = 1
		lastDiff = 0
		while (True):
			aboveThreshold = self.progressOneSecond(inputNumbers)

			if aboveThreshold:
				minX = min(x[0] for x in inputNumbers)
				minY = min(x[1] for x in inputNumbers)
				maxX = max(x[0] for x in inputNumbers)
				maxY = max(x[1] for x in inputNumbers)
				diff = maxX-minX

				if diff < 100:
					if lastDiff < diff:
						self.progressOneSecond(inputNumbers, True)
						self.drawStars(inputNumbers,  minX, maxX, minY, maxY)
						print('Count %d' % count)
						break
					


				lastDiff = diff

			count += 1



	def progressOneSecond(self, inputNumbers, reverse = False):

		cnt = Counter()

		for i in inputNumbers:
			i[0] = i[0] + (i[2] * (1 if not reverse else -1))
			i[1] = i[1] + (i[3] * (1 if not reverse else -1))
			cnt[i[0]] += 1

		mostCommon = Counter(cnt).most_common(1)

		lastValue = None
		for com in mostCommon:
			if lastValue is None:
				lastValue = com[1]
			elif lastValue != com[1]:
				return False

		if lastValue >= 8:
			return True

		return False



	def drawStars(self, inputNumbers, minX, maxX, minY, maxY):
		print('%s %s %s %s' % (minX, minY, maxX, maxY))

		grid = set()
		for i in inputNumbers:
			grid.add('%d,%d' % (i[0], i[1]))

		drawing = ''

		for y in range(minY , maxY ):
			for x in range(minX , maxX ):
				if  '%d,%d' % (x, y) in grid:
					drawing = '%s#' % drawing
				else:
					drawing = '%s.' % drawing
			drawing = '%s\n' % drawing

		print(drawing)


	def run(self):
		inputList = common.loadInput('input2.txt', True) #True = split, False = string

		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
