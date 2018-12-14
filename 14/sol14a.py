#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import deque



class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, recipeCount):
		values = [3, 7]
		elf1 = 0
		elf2 = 1
		
		
		goal = recipeCount + 10
		while len(values) <= goal:
			result = values[elf1] + values[elf2]
			digits = [int(i) for i in str(result)]
			values.extend(digits)
			
			#move the elves
			elf1 += values[elf1] + 1
			elf2 += values[elf2] + 1
			
			elf1 = elf1 % len(values)
			elf2 = elf2 % len(values)
		
		values = values[recipeCount:]
		trim = 10 - len(values)
		print(values[:trim])
		return ''.join( map(str, values[:trim]) )

	def run(self):
		print('Advent Day: %s' % self.solution(330121))




if __name__ == '__main__':
	Solution().run()
