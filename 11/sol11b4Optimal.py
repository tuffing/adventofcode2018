#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict



class Solution(object):
    #inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

    def __init__(self):
        pass

    def solution(self, serial):
        grid = defaultdict(list)

        for x in range(0, 300):
            [self.calculateCell(serial, grid, x, y) for y in range(0, 300)]


        #for x in range(0, 300):
        #    [self.calculateCellSummedAreaTable(grid, x, y) for y in range(0, 300)]

        highestTotal = -100000
        coordsOfHighest = 0
        for gridSize in range (0, 300):
            for y in range(0, 300):
                if y + gridSize > len(grid) - 1:
                    break;

                for x in range(0, 300):
                    if x + gridSize > len(grid) - 1:
                        break;


                    value = self.checkGrid(grid, x, y, gridSize)
                    if value > highestTotal:
                        highestTotal = value
                        coordsOfHighest = '%s,%s,%s' % (x+1,y+1,gridSize)

        return coordsOfHighest
        
    def calculateCell(self, serial, grid, x, y):
        self.calculateCoods(grid, serial, x, y)
        self.calculateCellSummedAreaTable(grid, x, y)
    
    def calculateCellSummedAreaTable(self, grid, x,  y):
        value = grid[x][y]
        
        if y - 1 >= 0:
            value += grid[x][y-1]
            
        if x - 1 >= 0:
            value += grid[x-1][y]
            
        if y - 1 >= 0 and x - 1 > 0:
            value -= grid[x-1][y-1]
            
        grid[x][y] = value
        

    def checkGrid(self, grid, x, y, gridSize):
        a = grid[x][y]
        b = grid[x+gridSize][y]
        c = grid[x][y+gridSize]
        d = grid[x+gridSize][y+gridSize]
        
        return d + a - b - c 
        



    def calculateCoods(self, grid, serial, x, y):
        rackId = x + 10
        powerlevel = ((rackId * y) + serial) * rackId

        levelAsString = str(powerlevel)
        powerlevel = 0
        if (len(levelAsString) >= 3):
            powerlevel = int(levelAsString[-3])

        grid[x].append(powerlevel - 5)


    def run(self):
        print('Advent Day: X solution: %s ' % self.solution(9798))




if __name__ == '__main__':
    Solution().run()