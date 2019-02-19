#!/usr/bin/python3

import sys
#sys.path.append('../')
import common
from collections import defaultdict, deque
import copy
import heapq

class Solution(object):
	# 6.292s, 7.5

	def __init__(self):
		pass

	def solution(self, inputFile):
		rows = list()
		for i in inputFile:
			rows.append(list(i))
		
		pointDistances = defaultdict(list)
		
		goblins = list()
		elves = list()
		count = 0
		
		allPlayers = self.pullOutPlayers(rows, goblins, elves)
		
		count = 0
		while True:
			allPlayers = self.tick(goblins, elves, allPlayers,rows)
						
			if len(elves) == 0 or len(goblins) == 0:
				break
			
			count = count + 1

		winner = elves
		if len(goblins):
			winner = goblins
		hp = 0
		
		for w in winner:
			hp += w['hp']
		
		result = hp * (count)
		
		print('Solution Here %s' % result)
		return result
	
	def tick(self, goblins, elves, allPlayers, rows):
		newPlayerList = []
		
		while len(allPlayers):
			y, x, player = heapq.heappop(allPlayers)

			if len(player) == 0 or player['hp'] <= 0:
				continue			
			
			enemies = goblins
			enemiesSym = 'G'

			if player['side'] == 'G':
				enemies = elves
				enemiesSym = 'E'

			self.setPlayerDistances(rows, player)
			
			closest, distance = self.findCorrectPath(rows, (player['x'], player['y']), player['distances'], player['closest'], player['dist'])

			if closest != None:
				#if closest isn't in range, move
				if distance is not None and distance > 0:
					rows[player['y']][player['x']] = '.'
					player['x'] = closest[0]
					player['y'] = closest[1]
					rows[player['y']][player['x']] = player['side']
					

				target = None
				lowestHP = 201
				
				enemies.sort(key=lambda x: (x['y'], x['x']), reverse=True)
				
				#bottom, right, left, top (reverse)
				#coords = [(player['x'],player['y'] + 1),(player['x']+1,player['y']),(player['x']-1,player['y']), (player['x'],player['y']-1)]
				coords = [(player['x'],player['y'] - 1),(player['x']-1,player['y']),(player['x']+1,player['y']), (player['x'],player['y']+1)]
				#coords = [(player['x'],player['y'] - 1),(player['x'],player['y']+1),(player['x']-1,player['y']), (player['x']+1,player['y'])]
				#coords = [(player['x']+1,player['y']),(player['x']-1,player['y']),(player['x'],player['y']+1), (player['x'],player['y']-1)]
				possibles = []
					
				for c in coords:
					match = None
					for ene in enemies:
						if c == (ene['x'], ene['y']):
							match = ene
							break
					possibles.append(match)
				
				for p in possibles:
					if p is not None and p['hp'] < lowestHP and p['hp'] > 0:
						target = p
						lowestHP = p['hp']
				
				if target:
					target['hp'] -= 3
					if target['hp'] <= 0:
						rows[target['y']][target['x']] = '.'
						enemies.remove(target)

			heapq.heappush(newPlayerList, (player['y'],player['x'],player))
			
			
			if len(goblins) == 0 or len(elves) == 0:
				break
		
		return newPlayerList
		
	
	def findCorrectPath(self, rows, playerCoords, distances, closest, distance):
		obstacles = ['#', 'E', 'G', '.']

		if closest is None:
			return (closest, distance)		
			
		while distance > 1:
			x = closest[0]
			y = closest[1]
			
			coords = [(x,y+1),(x+1,y),(x-1,y), (x,y-1)]
			
			for c in coords:
				if c[1] <  len(rows) and (distances[c[1]][c[0]] not in obstacles) and distances[c[1]][c[0]] <= distance:
					distance = distances[c[1]][c[0]]
					closest = (c[0], c[1])				
			
		#check reading order of coords
		x = playerCoords[0]
		y = playerCoords[1]		
	
		
		return (closest, distance)
			
						
	
	def pullOutPlayers(self, rows, goblins, elves):
		playerSymbols = ['G', 'E']
		allPlayers = []
		for y, row in enumerate(rows):
			for x, ele in enumerate(row):
				if ele in playerSymbols:
					player = { 'side': ele, 'hp': 200, 'x': x, 'y': y}
					if ele == 'G':
						goblins.append(player)
					else:
						elves.append(player)
					
					heapq.heappush(allPlayers, (y,x,player))
					
		return allPlayers
			
	def setPlayerDistances(self, rows, player):	
		x = player['x']
		y = player['y']
		workingRows = copy.deepcopy(rows)
		workingRows[y][x] = 0
		badEle = 'G'
		if player['side'] == 'G':
			badEle = 'E'
			
		closest = self.findPointDistances(x, y, workingRows, badEle)
		player['distances'] = workingRows
		player['closest'] = closest[0]
		player['dist'] = closest[1]
											
	def findPointDistances(self, x, y, rows, badEle):
		queue = deque();
		queue.append((x,y));
		obstacles = ['#', 'E', 'G']
		rows[y][x] = 0
		closest = 10000
		closestCoords = (1000,1000)			
		
		while len(queue):
			v = queue.popleft()
			
			if (rows[v[1]][v[0]] > closest):
				continue
			
			coords = [(v[0]-1,v[1]),(v[0]+1,v[1]),(v[0],v[1]-1), (v[0], v[1]+1)]
			badFound = False						
				
			for c in coords:
				if rows[c[1]][c[0]] == badEle and rows[v[1]][v[0]] <= closest:
					badFound = True
					closest = rows[v[1]][v[0]]

					if v[1] < closestCoords[1]:
						closestCoords = v
					elif v[1] == closestCoords[1] and v[0] < closestCoords[0]:
						closestCoords = v				
				
				if badFound:
					continue
				
				if rows[c[1]][c[0]] not in obstacles and (rows[c[1]][c[0]] == '.' or rows[c[1]][c[0]] > rows[v[1]][v[0]] +1):
					rows[c[1]][c[0]] = rows[v[1]][v[0]] + 1
					queue.append(c)
		

		if closest == 10000:
			closest = None
			closestCoords = None
			
		return (closestCoords, closest)
		
	

	def run(self):
		inputList = common.loadInput('input.txt', True)
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
