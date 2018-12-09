#!/usr/bin/python3

import unittest
#replace standard with day name
from sol9a import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):


	def test_run1(self):
		testObject = Solution()
		self.assertEqual(8317, testObject.solution(10, 1618))

	def test_run2(self):
		testObject = Solution()
		self.assertEqual(146373, testObject.solution(13, 7999))

	def test_run3(self):
		testObject = Solution()
		self.assertEqual(2764, testObject.solution(17, 1104))

	def test_run4(self):
		testObject = Solution()
		self.assertEqual(54718, testObject.solution(21, 6111))

	def test_run5(self):
		testObject = Solution()
		self.assertEqual(37305, testObject.solution(39, 5807))

	def test_run6(self):
		testObject = Solution()
		self.assertEqual(95, testObject.solution(1, 48))

if __name__ == '__main__':
    unittest.main()