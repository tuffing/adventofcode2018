#!/usr/bin/python3

import unittest
#replace standard with day name
from sol11b4Optimal import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):


    def test_full_solution(self):
        #remember to set the assert to the known examples and place the example test into testInput.txt!
        testObject = Solution()
        self.assertEqual('90,269,16', testObject.solution(18))


if __name__ == '__main__':
    unittest.main()