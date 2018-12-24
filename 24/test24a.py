#!/usr/bin/python3

import unittest
#replace standard with day name
from sol24a import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
        
                inputImmune = common.loadInput('testimmune.txt', True) #True = split, False = string
                inputInfection = common.loadInput('testinfection.txt', True) #True = split, False = string
                testObject = Solution()
                self.assertEqual(5216, testObject.solution(inputImmune, inputInfection))


if __name__ == '__main__':
        unittest.main()