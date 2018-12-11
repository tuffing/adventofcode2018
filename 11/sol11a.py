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


		z = [self.checkGrid(grid, squares, x, y) for y in range(1, 231) for x in range(0, 300)]

		#print(grid)
		v=list(squares.values())
		k=list(squares.keys())
		
		print(squares['5,2'])
		print(grid[5][1])
		#print('%s %s' % (k, v))
		return k[v.index(max(v))]

		#eturn max(squares.iterkeys(), key=(lambda key: stats[key]))


	def checkGrid(self, grid, squares, x, y):
		if y + 3 > len(grid) - 1 or x + 3 > len(grid) - 1:
			return;

		total = 0
		for iy in range(y, y+3):
			for ix in range(x, x+3):
				#print('%d,%d' % (ix,iy))
				if x+1==5 and y == 2:
					print(grid[iy][ix])
				total += grid[iy][ix]

		squares['%d,%d' % (x+1,y)] = total



	# Find the fuel cell's rack ID, which is its X coordinate plus 10.
	# Begin with a power level of the rack ID times the Y coordinate.
	# Increase the power level by the value of the grid serial number (your puzzle input).
	# Set the power level to itself multiplied by the rack ID.
	# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
	# Subtract 5 from the power level.
	# For example, to find the power level of the fuel cell at 3,5 in a grid with serial number 8:

	# The rack ID is 3 + 10 = 13.
	# The power level starts at 13 * 5 = 65.
	# Adding the serial number produces 65 + 8 = 73.
	# Multiplying by the rack ID produces 73 * 13 = 949.
	# The hundreds digit of 949 is 9.
	# Subtracting 5 produces 9 - 5 = 4.
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
