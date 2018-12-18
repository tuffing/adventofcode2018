#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		
		for tick in range (0, 10):
			inputList = self.tick(inputList)
		
		trees = 0
		lumbar = 0
		for row in inputList:
			for cell in row:
				if cell == '|':
					trees += 1
				elif cell == '#':
					lumbar += 1
					
				
		result = trees * lumbar
		print('Solution Here')
		return result
	
	def tick(self, inputList):
		#An open acre will become filled with trees if three or more adjacent acres contained trees.
	                #Otherwise, nothing happens.
		#An acre filled with trees will become a lumberyard 
		         #if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
		#An acre containing a lumberyard will remain a lumberyard 
		         #if it was adjacent to at least one other lumberyard and at least one acre containing trees. 
		         #Otherwise, it becomes open.
		workingList = list()
		
		for y, row in enumerate(inputList):
			workingList.append(list())
			for x, cell in enumerate(row):
				if cell == '|':
					test = 'hi'
				if cell == '.' and self.checkForSurroundSymbols(x, y, inputList, '|', 3) >= 3:
					workingList[y].append('|')
				elif cell == '.':
					workingList[y].append('.')
				if cell == '|' and self.checkForSurroundSymbols(x, y, inputList, '#', 3) >= 3:
					workingList[y].append('#')
				elif cell == '|':
					workingList[y].append('|')				
				if cell == '#' and (self.checkForSurroundSymbols(x, y, inputList, '#', 1) == 0 or self.checkForSurroundSymbols(x, y, inputList, '|', 1) == 0):
					workingList[y].append('.')
				elif cell == '#':
					workingList[y].append('#')					
		return workingList
					
	
	def checkForSurroundSymbols(self, x, y, inputList, symbol, goalCount):
		count = 0
		#top row
		if y - 1 >= 0:
			for i in range (x-1, x+2):
				if i >= 0 and i < len(inputList[y-1]):
					if inputList[y-1][i] == symbol:
						count += 1
		if count >= goalCount:
			return count
		
		#middle
		if x - 1 >= 0:
			if inputList[y][x-1] == symbol:
				count += 1
		if x + 1 < len(inputList[y]):
			if inputList[y][x+1] == symbol:
				count += 1
		
		if count >= goalCount:
			return count
		
		#bottom row
		if y + 1 < len(inputList):
			for i in range (x-1, x+2):
				if i >= 0 and i < len(inputList[y-1]):
					if inputList[y+1][i] == symbol:
						count += 1		
		
		return count
			
	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: %s' % self.solution(inputList))
		



if __name__ == '__main__':
	Solution().run()
