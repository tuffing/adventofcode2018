#!/usr/bin/python3

import unittest
#replace standard with day name
from sol7b import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

	def test_run(self):
		inputList = common.loadInput('input.txt', True) 
		self.assertEqual(896, Solution.solution(self, inputList))


if __name__ == '__main__':
    unittest.main()