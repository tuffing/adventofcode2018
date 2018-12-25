#!/usr/bin/python3

import unittest
#replace standard with day name
from sol25a2 import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput.txt', True) 
                testObject = Solution()
                self.assertEqual(2, testObject.solution(inputList))

        def test_run2(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput2.txt', True) 
                testObject = Solution()
                self.assertEqual(4, testObject.solution(inputList))
                
        def test_run3(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput3.txt', True) 
                testObject = Solution()
                self.assertEqual(3, testObject.solution(inputList))
                
        def test_run4(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput4.txt', True) 
                testObject = Solution()
                self.assertEqual(8, testObject.solution(inputList))

        def test_run5(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('input.txt', True) 
                testObject = Solution()
                self.assertEqual(388, testObject.solution(inputList))

if __name__ == '__main__':
        unittest.main()