#!/usr/bin/python3

import sys
#sys.path.append('../')
import common
from collections import defaultdict, deque
import copy


class Solution(object):
	#i nputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive
	#170.115s
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
		#self.setMapDistances(rows, pointDistances)
		
		count = 0
		while True:
			#for r in rows:
			#	print(r)


			self.tick(goblins, elves, allPlayers,rows)
			#print(count)
			if len(elves) == 0 or len(goblins) == 0:
				break
			#print(count)
			count = count + 1
		#for r in rows:
		#	print(r)		
		
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
		
		self.setMapDistances(rows, allPlayers)
		
		
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
				#for r in player['distances']:
				#	print(r)
			
			closest, distance = self.findClosestEnemies((player['x'], player['y']), player['distances'], enemies, allPlayers, rows)
			#print(closest);
			if closest != None:
				#if closest isn't in range, move
				if distance > 0:
					rows[player['y']][player['x']] = '.'
					player['x'] = closest[0]
					player['y'] = closest[1]
					rows[player['y']][player['x']] = player['side']
					change = True
					
				# @TODO Fix target selection!
				#attack!
				target = None
				#top
				lowestHP = 200
				enemies = list(enemies)
				enemies.sort()
				enemies.reverse()				
				
				for e in enemies:
					ene = allPlayers[e]
					#bottom
					if player['y'] + 1 == ene['y'] and player['x'] == ene['x'] and ene['hp'] <= lowestHP:
						target = '%s,%s' % ('{0:03d}'.format(player['y']+1),'{0:03d}'.format(player['x']))
						lowestHP = ene['hp']
					
					#right
					if player['x'] + 1 == ene['x'] and player['y'] == ene['y'] and ene['hp'] <= lowestHP:
						target = '%s,%s' % ('{0:03d}'.format(player['y']),'{0:03d}'.format(player['x'] + 1))
						lowestHP = ene['hp']
						
					#left
					if player['x'] - 1 == ene['x'] and player['y'] == ene['y'] and ene['hp'] <= lowestHP:
						target = '%s,%s' % ('{0:03d}'.format(player['y']),'{0:03d}'.format(player['x']-1))
						lowestHP = ene['hp']
						
					if player['y'] - 1 == ene['y'] and player['x'] == ene['x'] and ene['hp'] <= lowestHP:
						target = '%s,%s' % ('{0:03d}'.format(player['y']-1),'{0:03d}'.format(player['x']))
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
			
			if change:
				self.setMapDistances(rows, allPlayers)
				
	#def pickDirection(choices, distances):
		
	
	def findClosestEnemies(self, playerCoords, distances, enemies, players, rows):
		obstacles = ['#', 'E', 'G', '.']
		closest = None 
		smallest = 100000
		health = 200
		
		
		enemies = list(enemies)
		enemies.sort()
		enemies.reverse()
		
		for e in enemies:
			guy = players[e]
			#guyShortest = 10000
			coords = None
			x = guy['x']
			y = guy['y']
			#distances = guy['distances']
			
			#find next too
			guyClose = list()
			if  playerCoords in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)):
				closest = playerCoords
				smallest = 0
				health = guy['hp']
				continue
			
			#no need to go further if we already know someone is touching
			if smallest == 0:
				continue
			
			#bottom
			if y + 1 <  len(rows) and (distances[y+1][x] not in obstacles) and distances[y+1][x] <= smallest:
				smallest = distances[y+1][x]
				closest = (x, y+1)				
			#right
			if x + 1 < len(rows[y]) and (distances[y][x+1] not in obstacles) and distances[y][x+1] <= smallest:
				smallest = distances[y][x+1]
				closest = (x+1, y)
			#left
			if x - 1 >= 0 and (distances[y][x-1] not in obstacles) and distances[y][x-1] <= smallest:
				smallest = distances[y][x-1]
				closest = (x-1, y)
			#top
			if y - 1 >= 0 and (distances[y-1][x] not in obstacles) and distances[y-1][x] <= smallest:
				smallest = distances[y-1][x]
				closest = (x, y-1)

		if closest is None:
			return (closest, smallest)		
			
			
		#distance = smallest
		while smallest > 1:
			x = closest[0]
			y = closest[1]
			
			if y + 1 <  len(rows) and (distances[y+1][x] not in obstacles) and distances[y+1][x] <= smallest:
				smallest = distances[y+1][x]
				closest = (x, y+1)				
			#right
			if x + 1 < len(rows[y]) and (distances[y][x+1] not in obstacles) and distances[y][x+1] <= smallest:
				smallest = distances[y][x+1]
				closest = (x+1, y)
			#left
			if x - 1 >= 0 and (distances[y][x-1] not in obstacles) and distances[y][x-1] <= smallest:
				smallest = distances[y][x-1]
				closest = (x-1, y)
			#top
			if y - 1 >= 0 and (distances[y-1][x] not in obstacles) and distances[y-1][x] <= smallest:
				smallest = distances[y-1][x]
				closest = (x, y-1)			
			#we need to walk the path to find where our player should move
			
			
		#check reading order of coords
		x = playerCoords[0]
		y = playerCoords[1]		
		
		#top	
		#if y - 1 >= 0 and (distances[y-1][x] not in obstacles) and distances[y-1][x] == smallest:
		#	smallest = distances[y-1][x]
		#	closest = (x, y-1)
		#left
		#elif x - 1 >= 0 and (distances[y][x-1] not in obstacles) and distances[y][x-1] == smallest:
		#	smallest = distances[y][x-1]
		#	closest = (x-1, y)					
		#right
		#elif x + 1 < len(rows[y]) and (distances[y][x+1] not in obstacles) and distances[y][x+1] == smallest:
		#	smallest = distances[y][x+1]
		#	closest = (x+1, y)
		#bottom
		#	smallest = distances[y+1][x]
		#	closest = (x, y+1)	

	
		
		return (closest, smallest)
			
						
	
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
			
	def setMapDistances(self, rows, players):
		for p in players:
			firstEnemyDistance = {'distance': 10000}
			
			if len(players[p]) == 0:
				continue
			
			x = players[p]['x']
			y = players[p]['y']
			workingRows = copy.deepcopy(rows)
			workingRows[y][x] = 0
			badEle = 'G'
			if players[p]['side'] == 'G':
				badEle = 'E'
		
	
			self.findPointDistances(x, y, workingRows, badEle, firstEnemyDistance)
			
			
			if (x == 16 and y == 3):
				#a = rows[c[1]][c[0]]
				test = 'here'
				#for r in rows:
				#	print(r)
					
			players[p]['distances'] = workingRows
											
	def findPointDistances2(self, x, y, rows, badEle, firstEnemyDistance):
		queue = deque();
		queue.append((x,y));
		obstacles = ['#', 'E', 'G']
		rows[y][x] = 0
		
		if (x == 16 and y == 3):
			#a = rows[c[1]][c[0]]
			test = 'here'
			for r in rows:
				print(r)		
		
		while len(queue):
			v = queue.popleft()
			coords = [(v[0]-1,v[1]),(v[0]+1,v[1]),(v[0],v[1]-1), (v[0], v[1]+1)]
			
			for c in coords:
				test1 = rows[c[1]][c[0]] not in obstacles 
				test2 = rows[c[1]][c[0]]
				test3 = rows[v[1]][v[0]]
				if rows[c[1]][c[0]] not in obstacles and (rows[c[1]][c[0]] == '.' or rows[c[1]][c[0]] > rows[v[1]][v[0]] +1):
					rows[c[1]][c[0]] = rows[v[1]][v[0]] + 1
					queue.append(c)
				
		
		return rows
		
	
	
	def findPointDistances(self, x, y, rows, badEle, firstEnemyDistance):
		distance = int(rows[y][x]) + 1
		obstacles = ['#', 'E', 'G']
		badEleFound = False
		
		if distance > firstEnemyDistance['distance']:
			return
		
		# left
		if x - 1 >= 0:
			if rows[y][x-1] not in obstacles and (rows[y][x-1] == '.' or int(rows[y][x-1]) > distance):
				rows[y][x-1] = distance
				self.findPointDistances(x-1, y, rows, badEle, firstEnemyDistance)
			elif rows[y][x-1] == badEle:
				if distance < firstEnemyDistance['distance']:
					firstEnemyDistance['distance'] = distance
				else:
					return
		
		#right	
		if x + 1 < len(rows[y]):
			if rows[y][x+1] not in obstacles and (rows[y][x+1] == '.' or rows[y][x+1] > distance):
				rows[y][x+1] = distance
				self.findPointDistances(x+1, y, rows, badEle, firstEnemyDistance)
			elif rows[y][x+1] == badEle:
				if distance < firstEnemyDistance['distance']:
					firstEnemyDistance['distance'] = distance
				else:
					return				
				
		#top	
		if y >= 0:
			if rows[y-1][x] not in obstacles and (rows[y-1][x] == '.' or rows[y-1][x] > distance):
				rows[y-1][x] = distance
				self.findPointDistances(x, y-1, rows, badEle, firstEnemyDistance)
			elif rows[y-1][x]  == badEle:
				if distance < firstEnemyDistance['distance']:
					firstEnemyDistance['distance'] = distance
				else:
					return				
			
		#bottom
		if y + 1 <  len(rows):
			if rows[y+1][x] not in obstacles and (rows[y+1][x] == '.' or rows[y+1][x] > distance):
				rows[y+1][x] = distance
				self.findPointDistances(x, y+1, rows, badEle, firstEnemyDistance)	
			elif rows[y+1][x] == badEle:
				if distance < firstEnemyDistance['distance']:
					firstEnemyDistance['distance'] = distance
				else:
					return					
		
	
	
	#def buildClosestDistances(map):

	def run(self):
		inputList = common.loadInput('testInput.txt', True) #True = split, False = string
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
