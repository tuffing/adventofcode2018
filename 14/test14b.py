#!/usr/bin/python3

import unittest
#replace standard with day name
from sol14b import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual(9, testObject.solution('51589'))
                
        def test_run1(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual(5, testObject.solution('01245'))
                
        def test_run2(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual(18, testObject.solution('92510'))
                
        def test_run3(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual(2018, testObject.solution('59414'))


if __name__ == '__main__':
        unittest.main()