#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict, deque


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		nums = common.pullNumbersFromList(inputList, True)
		unassigned = deque(nums)
		
		
		consts = defaultdict(list)
		count = 0
		#first pass
		while len(unassigned):
			i = unassigned.popleft()
			if len(consts) == 0:
				consts[0].append(i)
				count += 1
				continue

			found = -1
			keys = list(consts.keys())
			for k in keys:
				v = consts[k]
				for coord in v:
					if self.calcManhatten(i, coord) <= 3:
						if found < 0:
							consts[k].append(i)
							found = k
						else:
							consts[found].extend(consts[k])
							del(consts[k])
						break
			
			if found < 0:
				consts[count].append(i)
				count += 1
				
		
		
		print('Solution Here %s' % len(consts))
		return len(consts)
	
	
	def calcManhatten(self, one, two):
		return abs(one[0] - two[0]) + abs(one[1] - two[1]) + abs(one[2] - two[2]) + abs(one[3] - two[3])

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: %s' % self.solution(inputList))
		



if __name__ == '__main__':
	Solution().run()
