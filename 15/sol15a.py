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
			self.tick(goblins, elves, allPlayers,rows)
			print(count)
			for r in rows:
				print(r)
			
			if len(elves) == 0 or len(goblins) == 0:
				break
			
			count = count + 1
			
		
		winner = elves
		if len(goblins):
			winner = goblins
		hp = 0
		
		for w in winner:
			hp += allPlayers[w]['hp']
		
		result = hp * (count-1)
		
		print('Solution Here %s' % result)
		return result
	
	def tick(self, goblins, elves, allPlayers, rows):
		turns = list(allPlayers.keys())
		turns.sort()
		
		self.setMapDistances(rows, allPlayers)
		
		for t in turns:
			player = allPlayers[t]
			if len(player) == 0:
				continue
			del(allPlayers[t])
			
			enemies = goblins
			enemiesSym = 'G'

			if player['side'] == 'G':
				enemies = elves
				enemiesSym = 'E'
				goblins.remove(t)
			else:
				elves.remove(t)
			
			closest, distance = self.findClosestEnemies((player['x'], player['y']), enemies, allPlayers, rows)
			
			if closest != None:
				#if closest isn't in range, move
				if distance > 0:
					rows[player['y']][player['x']] = '.'
					player['x'] = closest[0]
					player['y'] = closest[1]
					rows[player['y']][player['x']] = player['side']
					
				# @TODO Fix target selection!
				#attack!
				target = None
				#top
				if player['y'] - 1 >= 0 and rows[player['y'] - 1][player['x']] == enemiesSym:
					target = '%s,%s' % ('{0:03d}'.format(player['y']-1),'{0:03d}'.format(player['x']))
				#left
				elif player['x'] - 1 >= 0 and rows[player['y']][player['x']-1] == enemiesSym:
					target = '%s,%s' % ('{0:03d}'.format(player['y']),'{0:03d}'.format(player['x']-1))
				#right
				if player['x'] + 1 < len(rows[player['y']]) and rows[player['y']][player['x'] + 1] == enemiesSym:
					target = '%s,%s' % ('{0:03d}'.format(player['y']),'{0:03d}'.format(player['x'] + 1))
				#bottom
				if player['y'] + 1 < len(rows) and rows[player['y'] + 1][player['x']] == enemiesSym:
					target = '%s,%s' % ('{0:03d}'.format(player['y']+1),'{0:03d}'.format(player['x']))
				
				if target:
					allPlayers[target]['hp'] -= 3
					if allPlayers[target]['hp'] <= 0:
						rows[allPlayers[target]['y']][allPlayers[target]['x']] = '.'
						enemies.remove(target)
						del(allPlayers[target])
			
			#update sets	
			newName = '%s,%s' % ('{0:03d}'.format(player['y']),'{0:03d}'.format(player['x']))
			allPlayers[newName] = player
			
			if player['side'] == 'G':
				goblins.add(newName)
			else:
				elves.add(newName)
			
			
			if len(goblins) == 0 or len(elves) == 0:
				break
			
			self.setMapDistances(rows, allPlayers)
				
	#def pickDirection(choices, distances):
		
	
	def findClosestEnemies(self, playerCoords, enemies, players, rows):
		obstacles = ['#', 'E', 'G', '.']
		closest = None 
		smallest = 100000
		health = 200
		enemies = list(enemies)
		enemies.sort()
		enemies.reverse()
		
		for e in enemies:
			guy = players[e]
			guyShortest = 10000
			coords = None
			x = guy['x']
			y = guy['y']
			distances = guy['distances']
			
			#find next too
			guyClose = list()
			if  playerCoords in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)) and guy['hp'] <= health:
				closest = playerCoords
				smallest = 0
				health = guy['hp']
				continue
			
			#no need to go further if we already know someone is touching
			if smallest == 0:
				continue
				
			pX = playerCoords[0]
			pY = playerCoords[1]
			
			#bottom
			if pY + 1 <  len(rows) and (distances[pY+1][pX] not in obstacles) and distances[pY+1][pX] <= guyShortest:
				guyShortest = distances[pY+1][pX]
				closest = (pX, pY+1)				
			#right
			if pX + 1 < len(rows[pY]) and (distances[pY][pX+1] not in obstacles) and distances[pY][pX+1] <= guyShortest:
				guyShortest = distances[pY][pX+1]
				closest = (pX+1, pY)
			#left
			if pX - 1 >= 0 and (distances[pY][pX-1] not in obstacles) and distances[pY][pX-1] <= guyShortest:
				guyShortest = distances[pY][pX-1]
				closest = (pX-1, pY)
			#top
			if pY - 1 >= 0 and (distances[pY-1][pX] not in obstacles) and distances[pY-1][pX] <= guyShortest:
				guyShortest = distances[pY-1][pX]
				closest = (pX, pY-1)


		
				
			
				
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
			x = players[p]['x']
			y = players[p]['y']
			workingRows = copy.deepcopy(rows)
			workingRows[y][x] = 0
			self.findPointDistances(x, y, workingRows)
			players[p]['distances'] = workingRows
											
	
	def findPointDistances(self, x, y, rows):
		distance = int(rows[y][x]) + 1
		obstacles = ['#', 'E', 'G']
		# left
		if x >= 0 and rows[y][x-1] not in obstacles and (rows[y][x-1] == '.' or int(rows[y][x-1]) > distance):
			rows[y][x-1] = distance
			self.findPointDistances(x-1, y, rows)
		
		#right	
		if x + 1 < len(rows[y]) and rows[y][x+1] not in obstacles and (rows[y][x+1] == '.' or rows[y][x+1] > distance):
			rows[y][x+1] = distance
			self.findPointDistances(x+1, y, rows)
			
		#top	
		if y >= 0 and rows[y-1][x] not in obstacles and (rows[y-1][x] == '.' or rows[y-1][x] > distance):
			rows[y-1][x] = distance
			self.findPointDistances(x, y-1, rows)
			
		#bottom
		if y + 1 <  len(rows) and rows[y+1][x] not in obstacles and (rows[y+1][x] == '.' or rows[y+1][x] > distance):
			rows[y+1][x] = distance
			self.findPointDistances(x, y+1, rows)			
		
		
	#def buildClosestDistances(map):

	def run(self):
		inputList = common.loadInput('testInput.txt', True) #True = split, False = string
		print('Advent Day: X')
		self.solution(inputList)



if __name__ == '__main__':
	Solution().run()
