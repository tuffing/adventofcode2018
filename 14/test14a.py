#!/usr/bin/python3

import unittest
#replace standard with day name
from sol14a import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual('5158916779', testObject.solution(9))
                
        def test_run2(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual('0124515891', testObject.solution(5))


        def test_run3(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual('9251071085', testObject.solution(18))
                
        def test_run4(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                testObject = Solution()
                self.assertEqual('5941429882', testObject.solution(2018))
if __name__ == '__main__':
        unittest.main()