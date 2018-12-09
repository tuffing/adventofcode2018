#!/usr/bin/python3

import unittest
#replace standard with day name
from sol9b2 import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

# 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# 17 players; last marble is worth 1104 points: high score is 2764
# 21 players; last marble is worth 6111 points: high score is 54718
# 30 players; last marble is worth 5807 points: high score is 37305
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

	def test_run7(self):
	 	testObject = Solution()
	 	self.assertEqual(32, testObject.solution(5, 25))


	def test_run8(self):
	 	testObject = Solution()
	 	self.assertEqual(3412522480, testObject.solution(430, 71588*100))

if __name__ == '__main__':
    unittest.main()