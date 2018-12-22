#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict

class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass


	#The region at 0,0 (the mouth of the cave) has a geologic index of 0.
	#The region at the coordinates of the target has a geologic index of 0.
	#If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
	#If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
	#Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.
	#A region's erosion level is its geologic index plus the cave system's depth, all modulo 20183. Then:
	
	#If the erosion level modulo 3 is 0, the region's type is rocky.
	#If the erosion level modulo 3 is 1, the region's type is wet.
	#If the erosion level modulo 3 is 2, the region's type is narrow.
	def solution(self, depth, target):
		print('Solution Here')
		sys.setrecursionlimit(41000)
		
		grid = defaultdict(dict)
		visual = defaultdict(int)
		
		for y in range(0, target[1] + 1):
			for x in range(0, target[0] + 1):
				geo = 0
				if x == 0:
					geo = y * 48271
				elif y == 0:
					geo = x * 16807
				else:
					geo = grid[(x-1,y)]['erosion'] * grid[(x,y-1)]['erosion']
					
				erosion = (geo + depth) % 20183
				rtype = erosion % 3
				grid[(x,y)] = {'erosion': erosion, 'geo': geo, 'type': rtype, 'distance': 0}
				visual[(x,y)] = rtype
		
		targ = grid[target]
			
		total = sum(visual.values()) - visual[(0,0)] - visual[target]
		
		
		for y in range(0, target[1]):
			s = ''
			for x in range(0, target[0]):
				sym = '.'
				if grid[(x,y)]['type'] == 1:
					sym = '='
				if grid[(x,y)]['type'] == 2:
					sym = '|'                                
				s += sym
			print(s)
		
		#self.findPointDistances(0,0, visual, 0, target[0], 0, target[1])
					
		return total


	
	def run(self):
		#print('Advent Day: %s' % self.solution(11820, (7,782)))
		print('Advent Day: %s' % self.solution(510, (10,10)))
		



if __name__ == '__main__':
	Solution().run()
