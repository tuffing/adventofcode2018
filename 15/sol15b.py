#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict
import copy


class Solution(object):
	#i nputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputFile):
		rowsOriginal = list()
		for i in inputFile:
			rowsOriginal.append(list(i))
		
		
		goblinsOriginal = set()
		elvesOriginal = set()
		allPlayersOriginal = defaultdict(dict)
		count = 0
		lowestAttack = 200
		lowestAttackCount = 0
		winningElves = None
		self.pullOutPlayers(rowsOriginal, goblinsOriginal, elvesOriginal, allPlayersOriginal)
		trys = set()
		attackPower = 200
		nextStep = 200
		while True:
			print(attackPower)
			count = 0
			rows = copy.deepcopy(rowsOriginal)
			goblins = copy.deepcopy(goblinsOriginal)
			elves = copy.deepcopy(elvesOriginal)
			allPlayers = copy.deepcopy(allPlayersOriginal)
			while True:
				self.tick(goblins, elves, allPlayers,rows, attackPower)
				#print(count)
				#for r in rows:
				#	print(r)
				count = count + 1
				if len(elves) == 0 or len(goblins) == 0:
					break
				
				
			if len(elves) == len(elvesOriginal) and attackPower < lowestAttack:
				lowestAttackCount = count
				lowestAttack = attackPower
				winningElves = allPlayers
			
			#if nextStep == 1:
			#	break
			
			trys.add(lowestAttack)
			
			if nextStep // 2 == 0:
				nextStep = 1
			else:
				nextStep = nextStep//2

			
			if len(elves) == len(elvesOriginal):
				attackPower -= nextStep
			else:
				attackPower += nextStep
			
			if attackPower in trys:
				break
			

		#for r in rows:
		#	print(r)		
		
		hp = 0
		
		for w in winningElves:
			hp += winningElves[w]['hp']
		
		result = hp * (lowestAttackCount)
		print(hp * (lowestAttackCount-1))
		
		print('Solution Here %s' % result)
		return result
	
	def tick(self, goblins, elves, allPlayers, rows, attackPower):
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
					if player['side'] == 'E':
						allPlayers[target]['hp'] -= attackPower
					else:
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
						if target in turns:
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
			players[p]['distances'] = workingRows
											
	
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
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
