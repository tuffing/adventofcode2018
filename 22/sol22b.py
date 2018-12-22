#!/usr/bin/python3

import sys
#sys.path.append('../')
#from scaffolding import common
from collections import defaultdict, deque

class Solution(object):
    #inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

    def __init__(self):
        pass


    #The region at 0,0 (the mouth of the cave) has a geologic index of 0.
    #The region at the coordinates of the target has a geologic index of 0.
    #If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
    #If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
    #Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.
    #A region's erosion level is its geologic index plus the cave system's depth, all modulo 20183. Then:

    #If the erosion level modulo 3 is 0, the region's type is rocky.
    #If the erosion level modulo 3 is 1, the region's type is wet.
    #If the erosion level modulo 3 is 2, the region's type is narrow.
    def solution(self, depth, target):
        print('Solution Here')
        sys.setrecursionlimit(80000)

        grid = defaultdict(dict)
        visual = defaultdict(int)

        for y in range(0, target[1] + 100):
            for x in range(0, target[0] + 100):
                geo = 0

                if x == 0 and y == 0:
                    geo = 0 
                elif x == target[0] and y == target[1]:
                    geo = 0                                
                elif x == 0:
                    geo = y * 48271
                elif y == 0:
                    geo = x * 16807
                else:
                    geo = grid[(x-1,y)]['erosion'] * grid[(x,y-1)]['erosion']

                erosion = (geo + depth) % 20183
                rtype = erosion % 3
                grid[(x,y)] = {'erosion': erosion, 'geo': geo, 'type': rtype, 'count': 100, 'tools': {'torch': 10000, 'climbing': 10000, 'neither': 10000}}
                visual[(x,y)] = rtype

        #Moving to an adjacent region takes one minute.
        #(For example, if you have the torch equipped, you can move between rocky 
            #and narrow regions, but cannot enter wet regions.)

        #You can change your currently equipped tool or put both away 
        #if your new equipment would be valid for your current region. Switching to using the climbing gear, torch, 
        #or neither always takes seven minutes,	
        targ = grid[target]
        grid[(0,0)]['tools']['torch'] = 0
        grid[target]['type'] = 0
        grid[(0,0)]['tool'] = 'torch'

        for y in range(0, target[1] + 100):
            s = ''
            for x in range(0, target[0] + 100):
                sym = '.'
                if grid[(x,y)]['type'] == 1:
                    sym = '='
                if grid[(x,y)]['type'] == 2:
                    sym = '|'                                
                s += sym
            #print(s)


        queue = deque([(0,0, 'torch', 0)])

        while len(queue):
            xy = queue.popleft()

            self.findPointDistances(xy[0],xy[1], xy[2], xy[3], grid, queue, 0, target[0]+100, 0, target[1]+100, target)


        targ = grid[target]


        for k,v in targ['tools'].items():
            if k != 'torch':
                targ['tools'][k] += 7              

        return min(targ['tools'].values())


    def findPointDistances(self, x, y, currentTool, distance, rows, queue, minX, maxX, minY, maxY, target):
       # if (x,y) != (0,0) and rows[(x,y)]['distance'] < distance:
        #    return               

        current = rows[(x,y)]
        distance = distance + 1


        # left
        if x - 1 >= minX:
            mod = 0
            match = self.matchTool(current['type'], rows[(x-1,y)]['type'], currentTool, (x-1,y), target)
            if match != currentTool:
                mod += 7

            if rows[(x-1,y)]['tools'][match] > distance + mod:
                rows[(x-1,y)]['tools'][match] = distance + mod
                rows[(x-1,y)]['tool'] = match
                queue.append((x-1, y, match, distance + mod))

        #right	
        if x + 1 < maxX:
            mod = 0
            test = rows[(x+1,y)]
            match = self.matchTool(current['type'], rows[(x+1,y)]['type'], currentTool, (x+1,y), target) 
            if match != currentTool:
                mod += 7			

            if rows[(x+1,y)]['tools'][match] > distance + mod:
                rows[(x+1,y)]['tools'][match] = distance + mod
                rows[(x+1,y)]['tool'] = match
                queue.append((x+1, y, match,  distance + mod))

        #top	
        if y - 1 >= minY:
            mod = 0
            match = self.matchTool(current['type'], rows[(x,y-1)]['type'], currentTool, (x,y-1), target) 
            if match != currentTool:
                mod += 7			

            if rows[(x, y-1)]['tools'][match] > distance + mod:
                rows[(x, y-1)]['tools'][match] = distance + mod
                rows[(x, y-1)]['tool'] = match
                queue.append((x, y-1, match,  distance + mod))

        #bottom
        if y + 1 <  maxY:
            mod = 0
            match = self.matchTool(current['type'], rows[(x,y+1)]['type'], currentTool, (x,y+1), target)
            if match != currentTool:
                mod += 7			
            test = rows[(x-1,y)]
            if rows[(x, y+1)]['tools'][match] > distance + mod:
                rows[(x, y+1)]['tools'][match] = distance + mod
                rows[(x, y+1)]['tool'] = match
                queue.append((x, y+1, match,  distance + mod))



    def matchTool(self, t1, t2, currentTool, xy, target):
        #In rocky regions, you can use the climbing gear or the torch. 
            #You cannot use neither (you'll likely slip and fall).
        #In wet regions, you can use the climbing gear or neither tool. 
            #You cannot use the torch (if it gets wet, you won't have a light source).
        #In narrow regions, you can use the torch or neither tool. 
            #You cannot use the climbing gear (it's too bulky to fit).


        if t1 == 0:
            if xy == target and currentTool != 'torch':
                return 'torch'

            if t2 == 0:
                return currentTool
            if t2 == 1:
                return 'climbing'
            if t2 == 2:
                return 'torch'

        if t1 == 1:
            if t2 == 0:
                return 'climbing'
            if t2 == 1:
                return currentTool
            if t2 == 2:
                return 'neither'

        if t1 == 2:
            if t2 == 0:
                return 'torch'
            if t2 == 1:
                return 'neither'
            if t2 == 2:
                return currentTool

    def run(self):
        #print('Advent Day: %s' % self.solution(11820, (7,782)))
        print('Advent Day: %s' % self.solution(510, (10,10)))




if __name__ == '__main__':
    Solution().run()
