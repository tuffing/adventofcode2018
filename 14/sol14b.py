#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import deque



class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, recipeToMatch):
		values = [3, 7]
		last = '37'
		elf1 = 0
		elf2 = 1
		found = False
		
		while not found:
			result = values[elf1] + values[elf2]
			digits = [int(i) for i in str(result)]
			values.extend(digits)
			
			for d in digits:
				last = '%s%s' % (last, d)
				if len(last) > len(recipeToMatch):
					last = last[len(last)-len(recipeToMatch):]
			
				if last == recipeToMatch:
					found = True
			
			#move the elves
			elf1 += values[elf1] + 1
			elf2 += values[elf2] + 1
			
			elf1 = elf1 % len(values)
			elf2 = elf2 % len(values)
		
		length = (len(values) - len(recipeToMatch))
		if last != recipeToMatch:
			length -= 1
			
		return len(values) - len(recipeToMatch)

	def run(self):
		print('Advent Day: %s' % self.solution('330121'))




if __name__ == '__main__':
	Solution().run()
