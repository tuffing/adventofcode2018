#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict



class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, serial):
		grid = defaultdict(list)

		for y in range(1, 301):
			grid[y] = [self.calculateCoods(serial, x, y) for x in range(1, 301)]


		squares = defaultdict(int)


		z = [self.checkGrid(grid, squares, x, y) for y in range(1, 301) for x in range(0, 300)]

		#print(grid)
		v=list(squares.values())
		k=list(squares.keys())
		

		return k[v.index(max(v))]



	def checkGrid(self, grid, squares, x, y):
		for gridSize in range (1, 301):
			total = 0
			if y + gridSize > len(grid) - 1 or x + gridSize > len(grid):
				break;

			lastSizeSquareName = '%d,%d,%d' % (x+1,y, gridSize - 1)

			if lastSizeSquareName in squares.keys():
				total = squares[lastSizeSquareName]

				for i in range(y, y+gridSize):
					#print('%d,%d' % (ix,iy))
					total += grid[i][x+gridSize-1]


				for i in range(x, x+gridSize-1):
					total += grid[y+gridSize-1][i]


			else:
				total = grid[y][x]

			squares['%d,%d,%d' % (x+1,y, gridSize)] = total
		if '%d,%d,%d' % (x+1,y, gridSize) in ['90,269,16', '5,2,3', '2.9.3']:
			print('aaaaa %s' % total)



	def calculateCoods(self, serial, x, y):
		rackId = x + 10
		powerlevel = ((rackId * y) + serial) * rackId

		levelAsString = str(powerlevel)
		powerlevel = 0
		if (len(levelAsString) >= 3):
			powerlevel = int(levelAsString[-3])

		return powerlevel - 5


	def run(self):
		print('Advent Day: X solution: %s ' % self.solution(18))
		



if __name__ == '__main__':
	Solution().run()
