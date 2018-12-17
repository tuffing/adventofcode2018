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
		#parse input list
		grid = defaultdict(int) # 0 = rock, 1 = running water, 2 = still
		
		for i in inputList:
			xy = i.split(', ')
			reverse = False
			if xy[0][0] == 'y':
				reverse = True
			
			xy[0] = xy[0].replace('x=', '').replace('y=', '')
			xy[1] = xy[1].replace('y=', '').replace('x=', '')
			
			coordRange = self.breakDownRange(xy[1])
			
			for c in coordRange:
				a = xy[0]
				if reverse:
					grid[(c, int(a))] = 0
				else:
					grid[(int(a), c)] = 0
				
		minY =  min(grid, key = lambda t: t[1])[1]
		maxY =  max(grid, key = lambda t: t[1])[1]
		
		startingPoint = (500, minY - 1)
		
		queue = deque()
		queue.append(startingPoint)
		
		while len(queue):
			flow = queue.pop()
			if flow[1] > maxY:
				continue

			if flow[1] >= minY:
				grid[flow] = 1			
			
			
			#can go down?
			if (flow[0], flow[1]+1) not in grid.keys():
					
				queue.append((flow[0], flow[1]+1))
				continue
			
			if (flow[0], flow[1]+1) in grid.keys() and grid[(flow[0], flow[1]+1)] == 1:
				continue
			
			#fill up a row?
			right = self.findExtents(grid, 1, flow)
			left = self.findExtents(grid, -1, flow)
			
			#enclosed space!
			if right[1] == flow[1] and left[1] == flow[1]: 
				for x in range(left[0]+1, right[0]):
					grid[(x, flow[1])] = 2
					
				queue.append((flow[0], flow[1] - 1))
				continue
			
			if (right[0] - 1, right[1]+1) in grid.keys() and grid[(right[0] - 1, right[1]+1)] == 1:
				continue
		
			if (left[0] + 1, left[1]+1) in grid.keys() and grid[(left[0] + 1, left[1]+1)] == 1:
				continue		
				
			#there's a hole!
			if right[1] == flow[1] + 1:
				queue.append(right)
			else: 
				right = (right[0]-1, right[1])
				
			if left[1] == flow[1] + 1:
				queue.append(left)
			else: 
				left = (left[0]+1, left[1])
				
			for x in range(left[0], right[0]+1):
				grid[(x, flow[1])] = 1
		
			#while True:
		
		wet = 0
		for k, v in grid.items():
			if v in [1,2]:
				wet += 1
				
		still = 0
		for k, v in grid.items():
			if v == 2:
				still += 1
				
		
		minx =  min(grid, key = lambda t: t[0])[0]
		maxx =  max(grid, key = lambda t: t[0])[0]
		
		for y in range(minY, maxY+1):
			line = ''
			for x in range(minx, maxx+1):
				if (x,y) in grid.keys():
					sym = '#'
					if grid[(x,y)] == 1:
						sym = '|'
					elif grid[(x,y)] == 2:
						sym = '~'
						
					line = '%s%s' % (line, sym)
				else: 
					line = '%s.' % line
			print(line)
		
		print('still: %s' % still)
		return wet
	
	def findExtents(self, grid, direction, point):
		x = point[0]
		while True:
			x += direction
			
			#hole
			if (x, point[1] +1) not in grid.keys():
				return (x, point[1] +1)
			#wall
			if (x, point[1]) in grid.keys():
				if grid[(x, point[1])] != 1:# or ((x, point[1]+1) in grid.keys() and grid[(x, point[1]+1)] == 1):
					return (x, point[1])
				
	
	def breakDownRange(self, value):
		# e.g 498..504
		minMax = value.split('..')
		values = []
		for x in range(int(minMax[0]), int(minMax[1]) + 1):
			values.append(x)
		
		return values

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: %s', self.solution(inputList))
		



if __name__ == '__main__':
	Solution().run()
