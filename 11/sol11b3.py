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

        for y in range(1, 301):
            grid[y] = [self.calculateCoods(serial, x, y) for x in range(1, 301)]


        squares = defaultdict(int)


        for gridSize in range (1, 301):
            #print(gridSize)
            for y in range(1, 301):
                if y + gridSize > len(grid) - 1:
                    break;

                for x in range(0, 300):
                    if x + gridSize > len(grid):
                        break;



                    self.checkGrid(grid, squares, x, y, gridSize)

        #print(grid)
        v=list(squares.values())
        k=list(squares.keys())


        #print('%s %s' % (k, v))
        return k[v.index(max(v))]

        #eturn max(squares.iterkeys(), key=(lambda key: stats[key]))


    def checkGrid(self, grid, squares, x, y, gridSize):
        if y + gridSize > len(grid) - 1 or x + gridSize > len(grid):
            return;
        x = x + 1

        if gridSize > 1:
        #if lastSizeSquareName in squares.keys():
            total = 0
            if gridSize % 2 == 0:
                half = gridSize / 2
                total += squares['%d,%d,%d' % (x,y, gridSize / 2)] #top left
                total += squares['%d,%d,%d' % (x+half,y, gridSize / 2)] #top right
                total += squares['%d,%d,%d' % (x,y+half, gridSize / 2)] #bottom left
                total += squares['%d,%d,%d' % (x+half,y+half, gridSize / 2)] #bottom rightlf

            else:
                firstSize = 0
                steps = 0
                if gridSize % 3 == 0:
                    firstSize =int(gridSize - int((gridSize/3)))
                    steps = int(gridSize / 3)
                elif gridSize % 5 == 0:
                    firstSize = int(gridSize - int((gridSize/5)))
                    steps = int(gridSize / 5)				
                elif gridSize % 7 == 0:
                    firstSize = int(gridSize - int((gridSize/7)))
                    steps = int(gridSize / 7)
                else: #prime
                    lastSizeSquareName = '%d,%d,%d' % (x,y, gridSize - 1)

                    if lastSizeSquareName in squares.keys():
                        total = squares[lastSizeSquareName]

                        tempX = x - 1
                        for i in range(y, y+gridSize):
                            #print('%d,%d' % (ix,iy))
                            total += grid[i][tempX+gridSize-1]
    
    
                        for i in range(tempX, tempX+gridSize-1):
                            total += grid[y+gridSize-1][i]
    

                    else:
                        total = grid[y][x-1]


                if steps > 0:                 
                    
                    total += squares['%d,%d,%d' % (x,y, firstSize)] #top left

                    #right column
                    for newY in range(y, y+gridSize, steps):
                        total += squares['%d,%d,%d' % (x+firstSize,newY, steps)] 

                    #new row
                    for newX in range(x, x+gridSize-steps, steps):
                        total += squares['%d,%d,%d' % (newX,y+gridSize-steps, steps)] 


            lastSizeSquareName = '%d,%d,%d' % (x,y, gridSize - 1)

            #print(lastSizeSquareName)
        else:
            total = grid[y][x-1]

        squares['%d,%d,%d' % (x,y, gridSize)] = total


        if '%d,%d,%d' % (x,y, gridSize) in ['5,2,3', '5,2,25']:
            print('test %s' % total)




    def calculateCoods(self, serial, x, y):
        rackId = x + 10
        powerlevel = ((rackId * y) + serial) * rackId

        levelAsString = str(powerlevel)
        powerlevel = 0
        if (len(levelAsString) >= 3):
            powerlevel = int(levelAsString[-3])

        return powerlevel - 5


    def run(self):
        print('Advent Day: X solution: %s ' % self.solution(9798))




if __name__ == '__main__':
    Solution().run()