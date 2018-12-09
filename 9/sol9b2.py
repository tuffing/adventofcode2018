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

		count = 1
		while count <= highestMarble:
			if count % 23 == 0:
				circle.rotate(7)
				players[(count) % playerCount] = players[(count) % playerCount] + count + circle.pop()
				circle.rotate(-1)
			
			else:
				circle.rotate(-1)
				circle.append(count)

			count = count + 1

		#print(players)
		result = max(players.values())
		print('Solution Here: %d' % result)
		return result

	def run(self):
		#inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		self.solution(430, 71588*100)



if __name__ == '__main__':
	Solution().run()
