#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		simplified = list(map(lambda s: s.replace('Step ','').replace(' must be finished before step', '').replace(' can begin.', '').split(' '), inputList))

		#test  = 
		#print(test)

		letters = set([s[0] for s in simplified] + [s[1] for s in simplified])
		BfollowsA = defaultdict(list)
		aNeedsB = defaultdict(list)

		for s in simplified:
			BfollowsA[s[0]].append(s[1])
			aNeedsB[s[1]].append(s[0])


		string = ''
		todo = []

		#find out starting characters - the ones with no requirements
		for l in letters:
			if l not in aNeedsB.keys():
				todo.append(l)

		todo.sort()

		lettersUsed = set()
		lettersProcessing = set()

		asciiDiff = 4
		workers = []

		for i in range(5):
			workers.append({'currentJob': None, 'timeLeft': 0 })
			if len(todo) >= 1:
				workers[i]['currentJob'] = todo[0] 
				workers[i]['timeLeft'] = ord(todo[0]) - asciiDiff 
				lettersProcessing.add(todo[0] )
				del(todo[0])


		counter = 0
		while todo or any(w['currentJob'] is not None for w in workers):
			for worker in workers:
				if worker['timeLeft'] > 0:
					worker['timeLeft'] = worker['timeLeft'] - 1

				if worker['timeLeft'] == 0 and worker['currentJob'] is not None:
					string = '%s%s' % (string, worker['currentJob'])
					lettersProcessing.remove(worker['currentJob'])
					lettersUsed.add(worker['currentJob'])	

					#update the todo list
					for c in BfollowsA[worker['currentJob']]:
						if c not in lettersUsed and c not in todo and c not in lettersProcessing:
							todo.append(c)

					worker['currentJob'] = None

					todo.sort()

				#assign a new job if there is one..
				if worker['currentJob'] is None:
					nextLetter = None
					for i,l in enumerate(todo):
						canUse = True
						for b in aNeedsB[l]:
							if b not in lettersUsed:
								canUse = False
								break

						if canUse and l:
							nextLetter = l
							del(todo[i])
							break

					worker['currentJob'] = nextLetter
					if nextLetter is not None:
						worker['timeLeft'] = ord(nextLetter) - asciiDiff
						lettersProcessing.add(nextLetter)


			counter = counter + 1


		return counter

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		print(self.solution(inputList))



if __name__ == '__main__':
	Solution().run()
