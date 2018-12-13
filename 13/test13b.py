#!/usr/bin/python3

import unittest
#replace standard with day name
from sol13b import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                #inputList = common.loadInput('testInput.txt', True) 
                testObject = Solution()
                self.assertEqual('6,4', testObject.solution('testInput2.txt'))


if __name__ == '__main__':
        unittest.main()