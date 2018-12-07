#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict,deque


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		simplified = list(map(lambda s: s.replace('Step ','').replace(' must be finished before step', '').replace(' can begin.', '').split(' '), inputList))
		letters = set()
		BfollowsA = defaultdict(list)
		aNeedsB = defaultdict(list)

		for s in simplified:
			letters.add(s[0])
			letters.add(s[1])
			BfollowsA[s[0]].append(s[1])
			aNeedsB[s[1]].append(s[0])


		#find the last value
		string = ''
		todo = []

		for l in letters:
			if l not in aNeedsB.keys():
				todo.append(l)

		todo.sort()
		string = todo[0]
		del(todo[0])

		lettersUsed = set()
		nextLetter = string

		while (True):
			lettersUsed.add(nextLetter)			

			for c in BfollowsA[nextLetter]:
				if c not in lettersUsed and c not in todo:
					todo.append(c)
			
			todo.sort()

			if len(todo) == 0:
				break

			for i,l in enumerate(todo):
				canUse = True
				for a in aNeedsB[l]:
					if a not in lettersUsed:
						canUse = False
						break

				if canUse and l:
					nextLetter = l
					del(todo[i])
					break

			string = '%s%s' % (string, nextLetter)


		return string

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		print(self.solution(inputList))



if __name__ == '__main__':
	Solution().run()
