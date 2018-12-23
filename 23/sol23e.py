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

        inputNumbers.append((0,0,0,0))
        xAxis = (min(inputNumbers + [(0,0,0,0)], key=operator.itemgetter(0))[0], max(inputNumbers, key=operator.itemgetter(0))[0])
        yAxis = (min(inputNumbers + [(0,0,0,0)], key=operator.itemgetter(1))[1], max(inputNumbers, key=operator.itemgetter(1))[1])
        zAxis = (min(inputNumbers + [(0,0,0,0)], key=operator.itemgetter(2))[2], max(inputNumbers, key=operator.itemgetter(2))[2])

        steps = 100000000

        dist = 0

        while True:
            best = None
            bestCount = 0            
            for x in range (xAxis[0], xAxis[1] + 1, steps):
                for y in range (yAxis[0], yAxis[1] + 1, steps):
                    for z in range (zAxis[0], zAxis[1] + 1, steps):
                        count = 0
                        for ix, iy, iz, ir in inputNumbers:
                            distance = abs(x-ix) + abs(y-iy) + abs(z-iz)
                            if  (ix, iz, iz) != (0,0,0,0) and (distance - ir) // steps <= 0:
                                count += 1
                        if count > bestCount or (count == bestCount and abs(x-0) + abs(y-0) + abs(z-0) < dist):
                            best = (x,y,z)
                            if count > bestCount:
                                bestCount = count
                            dist = abs(x-0) + abs(y-0) + abs(z-0)
                       
            if steps == 1:
                solut = abs(best[0]) + abs(best[1]) + abs(best[2])
                print('Solution Here')
                return solut
        
            xAxis = (best[0] - steps, best[0] + steps)
            yAxis = (best[1] - steps, best[1] + steps)
            zAxis = (best[2] - steps, best[2] + steps)
            steps = steps // 2
            
        


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
