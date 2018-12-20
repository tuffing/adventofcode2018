#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import deque, defaultdict
import copy

class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		reg = deque(inputList)
		
		sys.setrecursionlimit(41000)
		
		rooms = defaultdict(lambda: defaultdict(str))
		x = (0,0)
		
		symbols = {'wall': '#', 'dunno': '?', 'doorV': '|', 'doorH': '-', 'room': '.'}
		
		directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
		doorToUse = {'N': symbols['doorH'], 'E': symbols['doorV'], 'S': symbols['doorH'], 'W': symbols['doorV']}
		
		self.processQueue(reg, rooms, x, symbols, directions, doorToUse)
		
		rKeys = list(rooms.keys())
		rKeys.sort()
		
		minY = rKeys[0]
		maxY = rKeys[len(rKeys)-1]
		minX = 0
		minX = 0
		
		for y in rKeys:
			row = rooms[y]
			keys = list(row.keys())
			keys.sort()
			
			minX = keys[0]
			maxX = keys[len(keys)-1]			
			
			s = ''
			for k in keys:
				if row[k] == symbols['dunno']:
					row[k] = symbols['wall']
				s = '%s%s' % (s, row[k])
			#print(s)
			
		rooms[0][0] = 0
		originalRooms = copy.deepcopy(rooms)
		self.findPointDistances(0, 0, rooms, minX, maxX, minY, maxY)
		
		highest = 0
		over1000 = 0
		for y in rKeys:
			row = rooms[y]
			keys = list(row.keys())
			keys.sort()
			s = ''
			for k in keys:
				if row[k] == symbols['dunno']:
					row[k] = symbols['wall']
				s = '%s%s' % (s, row[k])
				if row[k] != '#':
					if row[k] > highest:
						highest = row[k]
					
					if row[k] / 2 >= 1000 and originalRooms[y][k] not in '-|':
						value = row[k]
						over1000 += 1
					
				
			#print(s)
		
		print('Solution Here higest: %s OVER 1000: %s' % (int(highest / 2), over1000))
		return 1

	def processQueue(self, reg, rooms, initialX, symbols, directions, doorToUse):
		x = initialX
		
		while True:
			#current spot is a room
			rooms[x[1]][x[0]] = symbols['room'] 
			
			#the corners of the current room is always a door
			rooms[x[1]-1][x[0] - 1] = symbols['wall'] 
			rooms[x[1]+1][x[0] - 1] = symbols['wall'] 
			rooms[x[1]-1][x[0] + 1] = symbols['wall'] 
			rooms[x[1]+1][x[0] + 1] = symbols['wall']
			
			#possble doors
			sides = [(x[0] - 1, x[1]), (x[0] + 1, x[1]), (x[0], x[1] - 1),  (x[0], x[1] + 1)]
			for s in sides:
				if rooms[s[1]][s[0]] not in [symbols['doorV'], symbols['doorH']]:
					rooms[s[1]][s[0]] = symbols['dunno']
			
			if len(reg):	
				n = reg.popleft()
				if n == '^':
					n = reg.popleft()
				
				if n == '(':
					p = -1
					newReg = deque()
					last = ''
					while True:
						n = reg.popleft()
						if n == '(':
							p -= 1
						if n == ')':
							p += 1
						if p == 0:
							break
						last = n
						newReg.append(n)
					#if last != '|':
					self.processQueue(newReg, rooms, x, symbols, directions, doorToUse)
					
					continue
					#if len(reg):
					#	n = reg.popleft()

				if n == '|':
					x = initialX
					if len(reg):
						n = reg.popleft()
				
				if n != '$' and n != ')' and n != '|':
					rooms[x[1]+directions[n][1]][x[0]+directions[n][0]] = doorToUse[n]
					x = (x[0]+(directions[n][0]*2), x[1]+(directions[n][1]*2))			
				
			else:
				return		
		

	def findPointDistances(self, x, y, rows, minX, maxX, minY, maxY):
		distance = int(rows[y][x]) + 1
		obstacles = ['#', '?']
		
		# left
		if x - 1 >= minX:
			if rows[y][x-1] not in obstacles and (rows[y][x-1] in ['|','-','.'] or int(rows[y][x-1]) > distance):
				rows[y][x-1] = distance
				self.findPointDistances(x-1, y, rows, minX, maxX, minY, maxY)
				
		#right	
		if x + 1 < maxX:
			if rows[y][x+1] not in obstacles and (rows[y][x+1] in ['|','-','.'] or rows[y][x+1] > distance):
				rows[y][x+1] = distance
				self.findPointDistances(x+1, y, rows, minX, maxX, minY, maxY)
			
		#top	
		if y >= minY:
			if rows[y-1][x] not in obstacles and (rows[y-1][x] in ['|','-','.'] or rows[y-1][x] > distance):
				rows[y-1][x] = distance
				self.findPointDistances(x, y-1, rows, minX, maxX, minY, maxY)			
			
		#bottom
		if y + 1 <  maxY:
			if rows[y+1][x] not in obstacles and (rows[y+1][x] in ['|','-','.'] or rows[y+1][x] > distance):
				rows[y+1][x] = distance
				self.findPointDistances(x, y+1, rows, minX, maxX, minY, maxY)

	def run(self):
		inputList = common.loadInput('input.txt', False) #True = split, False = string
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
