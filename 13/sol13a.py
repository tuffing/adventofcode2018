#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
from collections import defaultdict

class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, fileName):
		inputFile = open(fileName, 'r')
		rows = inputFile.read().split('\n')
		inputFile.close()
		
		corners = ['/', '\\']
		straights = ['-', '|']
		interchange = ['+']
		
		players = defaultdict(dict)
		self.findPlayers(players, rows)
		#print(players)
		
		
		turn = False
		while turn is False:
			turn = self.takeTurn(players, rows)
		
		result = ('%d,%d' % (turn[1], turn[0]))
		print(result)
		return result
	
	def findPlayers(self, players, rows):
		previousElement = ''
		playerSymbols = ['v', '<', '>', '^']
		
		for y, row in enumerate(rows):
			for x, ele in enumerate(row):
				if ele in playerSymbols:
					players['%s,%s' % ('{0:03d}'.format(y),'{0:03d}'.format(x))] = {'dir': ele, 'turn': 0 }
					if ele in '^v':
						rows[y] = rows[y][:x] + '|' + rows[y][x + 1:]
					else:
						rows[y] = rows[y][:x] + '-' + rows[y][x + 1:]
	
					
	def takeTurn(self, players, rows):
		order = list(players.keys())
		order.sort()
		positions = ['^','>','v','<']
		
		for coords in order:
			player = players[coords]

			del(players[coords])
			#print(player)
			coords = coords.split(',')
			coords[0] = int(coords[0])
			coords[1] = int(coords[1])
			
			if player['dir'] == '^':
				coords[0] -= 1
			elif player['dir'] == 'v':
				coords[0] += 1
			elif player['dir'] == '>':
				coords[1] += 1	
			elif player['dir'] == '<':
				coords[1] -= 1
			
			newCoords = '%s,%s' % ('{0:03d}'.format(coords[0]),'{0:03d}'.format(coords[1]))
			if newCoords in players.keys():
				#theres a collision
				return coords
			
			#if coords[1] == 12:
			 #   print(player)
			
			if rows[coords[0]][coords[1]] == '/':
				if player['dir'] == '^':
					player['dir'] = '>'
				elif player['dir'] == 'v':
					player['dir'] = '<'
				elif player['dir'] == '>':
					player['dir'] = '^'
				elif player['dir'] == '<':
					player['dir'] = 'v'				
			elif rows[coords[0]][coords[1]] == '\\':
				if player['dir'] == '^':
					player['dir'] = '<'
				elif player['dir'] == 'v':
					player['dir'] = '>'
				elif player['dir'] == '>':
					player['dir'] = 'v'
				elif player['dir'] == '<':
					player['dir'] = '^'
			elif rows[coords[0]][coords[1]] == '+':			
				if player['turn'] == 0:
					#turn left
					index = positions.index(player['dir']) - 1
					if index == -1:
						index = 3
					
					player['dir'] = positions[index]
				elif player['turn'] == 2:
					index = positions.index(player['dir']) + 1
					if index == 4:
						index = 0
					
					player['dir'] = positions[index]
				
				player['turn'] += 1
				if player['turn'] == 3:
					player['turn'] = 0				
			#print(player)	
			players[newCoords] = player
		
		
		return False		
				
			

	def run(self):
		#inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		self.solution('input.txt')



if __name__ == '__main__':
	Solution().run()
