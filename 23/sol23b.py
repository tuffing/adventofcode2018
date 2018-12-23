#!/usr/bin/python3

import sys
#sys.path.append('../')
#from scaffolding import common
import operator
import re

class Solution(object):
    #inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

    def __init__(self):
        pass

    def solution(self, inputList):
        inputNumbers = self.pullNumbersFromList(inputList, True)
        #mr = max(inputNumbers, key=operator.itemgetter(3))
        
        xAxis = (min(inputNumbers, key=operator.itemgetter(0))[0], max(inputNumbers, key=operator.itemgetter(0))[0])
        yAxis = (min(inputNumbers, key=operator.itemgetter(1))[1], max(inputNumbers, key=operator.itemgetter(1))[1])
        zAxis = (min(inputNumbers, key=operator.itemgetter(2))[2], max(inputNumbers, key=operator.itemgetter(2))[2])

        #results = list(filter(lambda x: abs(x[0]-mr[0]) + abs(x[1]-mr[1]) + abs(x[2]-mr[2]) <= mr[3], inputNumbers))
        steps = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]
        
        #stepbest = (0,0,0)
        dist = 0
        
        for s in steps:
            best = None
            bestCount = 0
            
            for x in range (xAxis[0], xAxis[1] + 1, s):
                for y in range (yAxis[0], yAxis[1] + 1, s):
                    for z in range (zAxis[0], zAxis[1] + 1, s):
                        count = 0
                        for i in inputNumbers:
                            distance = abs(x-i[0]) + abs(y-i[1]) + abs(z-i[2])
                            if  (distance - i[3]) // s <= 0:
                                count += 1
                            #if  abs(x-i[0]) + abs(y-i[1]) + abs(z-i[2]) <= i[3]:
                                
                        if count > bestCount or (count == bestCount and abs(x-0) + abs(y-0) + abs(z-0) < dist):
                            best = (x,y,z)
                            bestCount = count
                            dist = abs(x-0) + abs(y-0) + abs(z-0)
            
            xAxis = (best[0] - int(s), best[0] + int(s))
            yAxis = (best[1] - int(s), best[1] + int(s))
            zAxis = (best[2] - int(s), best[2] + int(s))
                
            
        
        #test = list(filter(lambda x: x[0] >= 0, inputNumbers))
        solut = abs(best[0]) + abs(best[1]) + abs(best[2])
        print('Solution Here')
        return solut

    def loadInput(self, filename, splitIntoArray=True):
        inputFile = open(filename, 'r')
        text = inputFile.read().strip()
        inputFile.close()
    
        if (splitIntoArray):
            return text.split('\n')
    
        return text
    
    def pullNumbersFromList(self, data, includeSigns = True, listOfLists = True):
        reg = r'\d+'
        if (includeSigns):
            reg = r'-?\d+'
    
        if listOfLists:
            return list(map(lambda s: list(map(int, re.findall(reg, s))), data))
        else:
            return list(re.findall(reg, data))

    def run(self):
        inputList = self.loadInput('input.txt', True) #True = split, False = string
        print('Advent Day: %s' % self.solution(inputList))




if __name__ == '__main__':
    Solution().run()
