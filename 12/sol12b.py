#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import deque

class Solution(object):
        #inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

        def __init__(self):
                pass

        def solution(self, inputList, initialState):
                changes = self.parseInput(inputList)
                print(changes)
                print('Solution Here')
                currentState = deque(initialState)
                offset = 0
                
                for i in range(3000):#50000000000
                        offset, currentState = self.runGeneration(changes, currentState, offset)
                        if (i%1500 == 0):
                                print(i)
                        #print(''.join(currentState))
                
                plantScore = self.calculatePlants(currentState, offset)
                print(plantScore)
                
                return plantScore
        
        def runGeneration(self, changes, currentState, currentOffset):
                #currentState = '...%s...' % currentState
                newState = deque()
                count = 0
                finalCount = 0
                testString = '.....'
                
                newOffset = currentOffset
                endOffset = False
                
                while True:
                        if len(currentState) > 0:
                                testString = '%s%s' % (testString[1:], currentState.popleft())
                        else:
                                testString = '%s.' % (testString[1:])
                               
                        if testString in changes:
                                if currentOffset == newOffset and count <= 1:
                                        newOffset += 2 - count
                                
                                if finalCount == 3 and not endOffset:
                                        newState.append('.')
                                elif finalCount == 2:
                                        endOffset == True
                                
                                newState.append('#')
                                        
                        else:
                                if count > 1 or newOffset != currentOffset and finalCount < 2:
                                        newState.append('.')
                                        
                        if len(currentState) == 0:
                                finalCount += 1
                                if finalCount == 4:
                                        break
                        count += 1
                        
                return (newOffset, newState)
                        
        def calculatePlants(self, state, offset):
                offset *= -1
                score = 0
                while len(state):
                        if state.popleft() == '#':
                                score += offset
                        offset += 1
                
                return score
                
        
        def parseInput(self, inputList):
                conversions = set()
                
                for i in inputList:
                        parts = i.split(' => ')
                        if (parts[1]) == '#':
                                conversions.add(parts[0])
                        
                return conversions


        def run(self):
                inputList = common.loadInput('input.txt', True) #True = split, False = string
                print('Advent Day: X')
                self.solution(inputList, '.#####.##.#.##...#.#.###..#.#..#..#.....#..####.#.##.#######..#...##.#..#.#######...#.#.#..##..#.#.#')



if __name__ == '__main__':
        Solution().run()
