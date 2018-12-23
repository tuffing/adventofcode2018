#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
import operator

class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		inputNumbers = common.pullNumbersFromList(inputList, True)
		mr = max(inputNumbers, key=operator.itemgetter(3))
		
		results = list(filter(lambda x: abs(x[0]-mr[0]) + abs(x[1]-mr[1]) + abs(x[2]-mr[2]) <= mr[3], inputNumbers))
		#test = list(filter(lambda x: x[0] >= 0, inputNumbers))
		
		print('Solution Here')
		return len(results)

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: %s' % self.solution(inputList))
		



if __name__ == '__main__':
	Solution().run()
