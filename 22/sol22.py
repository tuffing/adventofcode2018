#!/usr/bin/python3

import sys
from collections import defaultdict, deque
import heapq


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
        risk = 0
        
        for y in range(0, target[1] + 20):
            for x in range(0, target[0] + 30):
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
                
                if x <= target[0] and y <= target[1]:
                    risk += rtype
                    
                grid[(x,y)] = {'erosion': erosion, 'geo': geo, 'type': rtype, 'count': 100, 'tools': {'torch': 10000, 'climbing': 10000, 'neither': 10000}}
                visual[(x,y)] = rtype
        
        risk = risk - grid[(0,0)]['type'] - grid[(target[0],target[1])]['type']
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

        queue = deque([(0,0, 'torch', 0)])

        visited = self.findPointDistancesDJ(grid, 0, target[0]+30, 0, target[1]+20, target)

        return (risk, visited[(target[0], target[1], 'torch')])


    def findPointDistancesDJ(self, rows, minX, maxX, minY, maxY, target):
        queue = []
        heapq.heappush(queue, (0,0,0,'torch'))
        visited = defaultdict(int)
        
        while len(queue):
            distance, x, y, tool = heapq.heappop(queue)
            if  visited.has_key((x, y, tool)):
                continue   
            
            visited[(x, y, tool)] = distance           
            
            coords = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
            
            for c in coords:
                if c[0] < minX or c[0] >= maxX or c[1] < minY or c[1] >= maxY:
                    continue
                
                if  visited.has_key((c[0], c[1], tool)):
                    continue                
                
                newTool = self.matchTool(rows[(x,y)]['type'], rows[(c[0],c[1])]['type'], tool, (c[0],c[1]), target)
                
                if (c[0], c[1], tool) in visited:
                    continue
                
                dist = distance + 1
                if newTool != tool:
                    dist += 7
                
                heapq.heappush(queue, (dist,c[0],c[1],newTool))
            
        
        return visited

    def findPointDistancesBFS(self, x, y, currentTool, distance, rows, queue, minX, maxX, minY, maxY, target):
        current = rows[(x,y)]
        distance = distance + 1
        coords = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

        # left
        for c in coords:
            if c[0] >= minX and c[0] < maxX and c[1] >= minY and c[1] < maxY:
                mod = 0
                match = self.matchTool(current['type'], rows[(c[0],c[1])]['type'], currentTool, (c[0],c[1]), target)
                if match != currentTool:
                    mod += 7
    
                if rows[(c[0],c[1])]['tools'][match] > distance + mod:
                    rows[(c[0],c[1])]['tools'][match] = distance + mod
                    rows[(c[0],c[1])]['tool'] = match
                    queue.append((c[0], c[1], match, distance + mod))

        



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
        sol = self.solution(11820, (7,782))
        print('Advent Day: %s, %s' % sol)
        #print('Advent Day: %s' % self.solution(510, (10,10)))




if __name__ == '__main__':
    Solution().run()
