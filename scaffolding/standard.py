#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from timeit import Timer


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		self.inputList = common.loadInput('input.txt', True) #True = split, False = string

	def run():
		print('Advent Day: X')
		#code to run



if __name__ == '__main__':
	Solution().run()
