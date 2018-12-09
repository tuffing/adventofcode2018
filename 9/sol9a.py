#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict, deque


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, playerCount, highestMarble):
		circle = deque()
		circle.append(0)
		players = defaultdict(int)
		position = 0
		count = 1
		while count <= highestMarble:
			if count % 23 == 0:
				#print ('old %s count %s' % (position, count))
				position = (position - 7) % len(circle) 
				#print ('new %s' % position)

				#print('%s%s' % (len(circle), circle[position]))
				#if (count == highestMarble):
				#	count == highestMarble * 100

				players[(count) % playerCount] = players[(count) % playerCount] + count + circle[position]
				#print( count + circle[position])
				del(circle[position])

				#if position > len(circle):
				#	position = 0

			else:
				#print('cur %s' % position)
				position = (position + 1) % len(circle) + 1

				circle.insert(position, count)

			#if count < 26:
			#	print(circle[position])
			#	print(circle)
			count = count + 1

		#print(players)
		result = max(players.values())
		print('Solution Here: %d' % result)
		return result

	def run(self):
		#inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		self.solution(430, 71588)



if __name__ == '__main__':
	Solution().run()
