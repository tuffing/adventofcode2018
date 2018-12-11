#!/usr/bin/python3

import unittest
#replace standard with day name
from sol11a import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

	# Fuel cell at  122,79, grid serial number 57: power level -5.
	# Fuel cell at 217,196, grid serial number 39: power level  0.
	# Fuel cell at 101,153, grid serial number 71: power level  4.

	def test_run1(self):
		testObject = Solution()
		self.assertEqual(4, testObject.calculateCoods(8, 3, 5))

	def test_run2(self):
		testObject = Solution()
		self.assertEqual(-5, testObject.calculateCoods(57, 122, 79))

	def test_run3(self):
		testObject = Solution()
		self.assertEqual(0, testObject.calculateCoods(39, 217, 196))

	def test_run4(self):
		testObject = Solution()
		self.assertEqual(4, testObject.calculateCoods(71, 101, 153))

	def test_full_solution(self):
		testObject = Solution()
		self.assertEqual('33,45', testObject.solution(18))


if __name__ == '__main__':
    unittest.main()