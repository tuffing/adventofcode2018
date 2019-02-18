#!/usr/bin/python3

import sys
#sys.path.append('../')
import common
from collections import defaultdict, deque
import copy


class Solution(object):
	# 6.292s

	def __init__(self):
		pass

	def solution(self, inputFile):
		rows = list()
		for i in inputFile:
			rows.append(list(i))
		
		pointDistances = defaultdict(list)
		
		goblins = set()
		elves = set()
		allPlayers = defaultdict(dict)
		count = 0
		
		self.pullOutPlayers(rows, goblins, elves, allPlayers)
		
		count = 0
		while True:
			self.tick(goblins, elves, allPlayers,rows)

			if len(elves) == 0 or len(goblins) == 0:
				break

			count = count + 1

		winner = elves
		if len(goblins):
			winner = goblins
		hp = 0
		
		for w in winner:
			hp += allPlayers[w]['hp']
		
		result = hp * (count)
		
		print('Solution Here %s' % result)
		return result
	
	def tick(self, goblins, elves, allPlayers, rows):
		turns = list(allPlayers.keys())
		turns.sort()
		
		for t in turns:
			if t == None:
				continue
			
			change = False
			player = allPlayers[t]
			
			del(allPlayers[t])
			
			if len(player) == 0:
				continue			
			
			enemies = goblins
			enemiesSym = 'G'

			if player['side'] == 'G':
				enemies = elves
				enemiesSym = 'E'
				goblins.remove(t)
			else:
				elves.remove(t)
			
			self.setPlayerDistances(rows, player)
			#findCorrectPath(self, playerCoords, distances, closest, distance):
			closest, distance = self.findCorrectPath(rows, (player['x'], player['y']), player['distances'], player['closest'], player['dist'])

			if closest != None:
				#if closest isn't in range, move
				if distance is not None and distance > 0:
					rows[player['y']][player['x']] = '.'
					player['x'] = closest[0]
					player['y'] = closest[1]
					rows[player['y']][player['x']] = player['side']
					change = True
					

				target = None
				lowestHP = 200
				enemies = list(enemies)
				enemies.sort()
				enemies.reverse()
				
				#bottom, right, left, top (reverse)
				coords = [(player['x'],player['y'] + 1),(player['x']+1,player['y']),(player['x']-1,player['y']), (player['x'],player['y']-1)]
				
				for e in enemies:
					ene = allPlayers[e]
					#bottom
					for c in coords:
						if c[1] == ene['y'] and c[0] == ene['x'] and ene['hp'] <= lowestHP:
							target = '%s,%s' % ('{0:03d}'.format(c[1]),'{0:03d}'.format(c[0]))
							lowestHP = ene['hp']

				
				if target:
					allPlayers[target]['hp'] -= 3
					if allPlayers[target]['hp'] <= 0:
						rows[allPlayers[target]['y']][allPlayers[target]['x']] = '.'
						enemies.remove(target)
						del(allPlayers[target])
						if player['side'] == 'G':
							elves.remove(target)
						else:
							goblins.remove(target)
						change = True
						turns[turns.index(target)] = None
							
			
			#update sets	
			newName = '%s,%s' % ('{0:03d}'.format(player['y']),'{0:03d}'.format(player['x']))
			allPlayers[newName] = player
			
			if player['side'] == 'G':
				goblins.add(newName)
			else:
				elves.add(newName)
			
			
			if len(goblins) == 0 or len(elves) == 0:
				break
			
		
	
	def findCorrectPath(self, rows, playerCoords, distances, closest, distance):
		obstacles = ['#', 'E', 'G', '.']

		if closest is None:
			return (closest, distance)		
			
			
		#distance = smallest
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
			
						
	
	def pullOutPlayers(self, rows, goblins, elves, allPlayers):
		playerSymbols = ['G', 'E']
	
		for y, row in enumerate(rows):
			for x, ele in enumerate(row):
				if ele in playerSymbols:
					if ele == 'G':
						goblins.add('%s,%s' % ('{0:03d}'.format(y),'{0:03d}'.format(x)))
					else:
						elves.add('%s,%s' % ('{0:03d}'.format(y),'{0:03d}'.format(x)))
						
					allPlayers['%s,%s' % ('{0:03d}'.format(y),'{0:03d}'.format(x))] = { 'side': ele, 'hp': 200, 'x': x, 'y': y} 						
					#rows[y][x] = '.'
			
			
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
				
			for c in coords:
				if rows[c[1]][c[0]] not in obstacles and (rows[c[1]][c[0]] == '.' or rows[c[1]][c[0]] > rows[v[1]][v[0]] +1):
					rows[c[1]][c[0]] = rows[v[1]][v[0]] + 1
					queue.append(c)
		

		if closest == 10000:
			closest = None
			closestCoords = None
			
		return (closestCoords, closest)
		
	

	def run(self):
		inputList = common.loadInput('testInput.txt', True)
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
