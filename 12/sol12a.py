#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict

class Solution(object):
        #inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

        def __init__(self):
                pass

        def solution(self, inputList, initialState):
                changes = self.parseInput(inputList)
                print(changes)
                print('Solution Here')
                currentState = initialState
                offset = 0
                
                for i in range(20):
                        offset, currentState = self.runGeneration(changes, currentState, offset)
                        #print(currentState)
                
                plantScore = self.calculatePlants(currentState, offset)
                print(plantScore)
                
                return plantScore
        
        def runGeneration(self, changes, currentState, currentOffset):
                currentState = '..%s..' % currentState
                newState = ''
                newOffset = currentOffset
                
                for s in range(len(currentState)):
                        testString = ''
                        if s <= 1:
                                testString = '..%s' % currentState[s:3+s]
                        elif s >= len(currentState) - 2:
                                testString = '%s..' % currentState[s-2:s+1]
                        else:
                                testString = currentState[s-2:s+3]

                        plant = '.'
                        if testString in changes.keys() and changes[testString] == '#':
                                plant = '#'
                        
                        if s > 1 or plant == '#':
                                newState = '%s%s' % (newState, plant)

                                if currentOffset == newOffset and s <= 1:
                                        newOffset += 2 - s                                
            
                if newState[-2:] == '..':
                        newState = newState[:-2]
                        
                return (newOffset, newState)
                        
        def calculatePlants(self, state, offset):
                offset *= -1
                score = 0
                for p in state:
                        if p == '#':
                                score += offset
                        offset += 1
                
                return score
                
        
        def parseInput(self, inputList):
                conversions = defaultdict(str)
                
                for i in inputList:
                        parts = i.split(' => ')
                        conversions[parts[0]] = parts[1]
                        
                return conversions


        def run(self):
                inputList = common.loadInput('input.txt', True) #True = split, False = string
                print('Advent Day: X')
                self.solution(inputList, '.#####.##.#.##...#.#.###..#.#..#..#.....#..####.#.##.#######..#...##.#..#.#######...#.#.#..##..#.#.#')



if __name__ == '__main__':
        Solution().run()
