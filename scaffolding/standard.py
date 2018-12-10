#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		print('Solution Here')
		return 1

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
