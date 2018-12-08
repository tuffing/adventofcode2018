#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import deque


class Solution(object):
	def __init__(self):
		pass

	def solution(self, inputList):
		inputNumbers = deque(common.pullNumbersFromList(inputList, True, False)) #True = include signs, False: all numbers are positive

		tree = {'meta': list(), 'children': list()}

		self.processNode(tree, inputNumbers)
		tree = tree['children'][0]

		total = self.findRootTotal(tree)

		print('Solution Here %d' % total)
		return total

	def processNode(self, tree, inputNumbers):
		node = {'meta': list(), 'children': list()}
		childrenCount = int(inputNumbers.popleft())
		metaCount = int(inputNumbers.popleft())

		total = 0


		for r in range(childrenCount):
				total = total + self.processNode(node, inputNumbers)

		for r in range(metaCount):
			meta = int(inputNumbers.popleft())
			total = total + meta
			node['meta'].append(meta)


		tree['children'].append(node)
		
		return total


	def findRootTotal(self, node):
		if len(node['children']) == 0:
			return sum(node['meta'])

		total = 0
		for m in node['meta']:
			if len(node['children']) > m - 1:
				total = total + self.findRootTotal(node['children'][m -1])

		return total

	def run(self):
		inputList = common.loadInput('input.txt', False) #True = split, False = string
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
