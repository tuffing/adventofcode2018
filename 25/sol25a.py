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
		
		#first pass
		while len(unassigned):
			i = unassigned.popleft()
			if len(consts) == 0:
				consts[0].append(i)
				continue

			found = False			
			for k,v in consts.items():
				for coord in v:
					if self.calcManhatten(i, coord) <= 3:
						consts[k].append(i)
						found = True
						break
				if found == True:
					break
			
			if not found:
				consts[len(consts)].append(i)
		
		
		#merge lists if possible
		for k in range(0, len(consts)):
			v = consts[k]
			groups = list(consts.values())
			groups.remove(v)
			match = False
			for coord1 in v:
				for list2 in groups:
					for coord2 in list2:
						if self.calcManhatten(coord1, coord2) <= 3:
							list2.extend(v)
							del(consts[k])
							match = True
							break
					if match:
						break
				if match:
					break
		
		print('Solution Here %s' % len(consts))
		return len(consts)
	
	
	def calcManhatten(self, one, two):
		return abs(one[0] - two[0]) + abs(one[1] - two[1]) + abs(one[2] - two[2]) + abs(one[3] - two[3])

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: %s' % self.solution(inputList))
		



if __name__ == '__main__':
	Solution().run()
