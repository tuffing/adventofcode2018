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
		currentElement = {'value': 0}
		currentElement['next'] = currentElement
		currentElement['prev'] = currentElement

		first = currentElement

		players = defaultdict(int)
		position = 0
		count = 1
		while count <= highestMarble:
			if count % 23 == 0:
				for i in range(7):
					prev = currentElement['value']
					currentElement = currentElement['prev']



				players[(count) % playerCount] = players[(count) % playerCount] + count + currentElement['value']
			

				currentElement['next']['prev'] = currentElement['prev']
				currentElement['prev']['next'] = currentElement['next']

				currentElement = currentElement['next']


			else:
				#print('cur %s' % position)
				nextMarble = currentElement['next']


				currentElement =  {'value': count}
				currentElement['next'] = nextMarble['next']
				currentElement['prev'] = nextMarble

				nextMarble['next'] = currentElement
				currentElement['next']['prev'] = currentElement

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
