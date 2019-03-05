#!/usr/bin/python3

import unittest
#replace standard with day name
from sol22 import *

sys.path.append('../')
import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                #inputList = common.loadInput('testInput.txt', True) 
                testObject = Solution()
                self.assertEqual((6318,1075), testObject.solution(11820, (7,782)))


if __name__ == '__main__':
        unittest.main()
