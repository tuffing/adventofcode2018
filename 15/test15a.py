#!/usr/bin/python3

import unittest
#replace standard with day name
from sol15a import *

sys.path.append('../')
import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput.txt', True) 
                testObject = Solution()
                self.assertEqual(18740, testObject.solution(inputList))
                
        def test_run2(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput2.txt', True) 
                testObject = Solution()
                self.assertEqual(28944, testObject.solution(inputList))        
                
        def test_run3(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput3.txt', True) 
                testObject = Solution()
                self.assertEqual(27755, testObject.solution(inputList))        

        def test_run4(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput4.txt', True) 
                testObject = Solution()
                self.assertEqual(36334, testObject.solution(inputList))
                
        def test_run5(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput5.txt', True) 
                testObject = Solution()
                self.assertEqual(39514, testObject.solution(inputList)) 

        def test_run6(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('input.txt', True) 
                testObject = Solution()
                self.assertEqual(228730, testObject.solution(inputList))
                

        def test_run7(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                inputList = common.loadInput('testInput10.txt', True) 
                testObject = Solution()
                self.assertEqual(181522, testObject.solution(inputList))
                
        #def test_run8(self):
        #        #This may cover an edge case BUT the expected answer is unconfirmed.
        #        inputList = common.loadInput('testInput11.txt', True) 
        #        testObject = Solution()
        #        self.assertEqual(261855, testObject.solution(inputList))  

        def test_run9(self):
                inputList = common.loadInput('testInput14.txt', True) 
                testObject = Solution()
                self.assertEqual(248848, testObject.solution(inputList))         
        
        def test_run10(self):
                inputList = common.loadInput('testInput15.txt', True) 
                testObject = Solution()
                self.assertEqual(201638, testObject.solution(inputList))          
        
        #def test_run11(self):
        #        #This may cover an edge case BUT the expected answer is unconfirmed.
        #        inputList = common.loadInput('testInput11.txt', True) 
        #        testObject = Solution()
        #        self.assertEqual(232110, testObject.solution(inputList))    
        
        def test_run12(self):
                inputList = common.loadInput('testInput13.txt', True) 
                testObject = Solution()
                self.assertEqual(346574, testObject.solution(inputList))         
                
        def test_run13(self):
                inputList = common.loadInput('testInput16.txt', True) 
                testObject = Solution()
                self.assertEqual(195774, testObject.solution(inputList))     
                
        def test_run14(self):
                inputList = common.loadInput('testInput17.txt', True) 
                testObject = Solution()
                self.assertEqual(206720, testObject.solution(inputList))
                
        #def test_run15(self):
        #        #This may cover an edge case BUT the expected answer is unconfirmed.
        #        inputList = common.loadInput('testInput18.txt', True) 
        #        testObject = Solution()
        #        self.assertEqual(190012, testObject.solution(inputList))  


if __name__ == '__main__':
        unittest.main()