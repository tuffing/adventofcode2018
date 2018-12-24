#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
#import operator
from collections import defaultdict, deque
import heapq
import math



class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass
	
	def parseData(self, inputImmune, inputInfection, modifier):
		immuneQueue = deque(inputImmune)
		infectQueue = deque(inputInfection)
		immuneSystem = []
		
		while len(immuneQueue):
			unit = self.buildGroup('immune', immuneQueue.pop(), modifier)
			immuneSystem.append(unit)
		
		infectionSystem = []
		while len(infectQueue):
			unit = self.buildGroup('infection', infectQueue.pop(), 0)
			infectionSystem.append(unit)
			
		return (immuneSystem, infectionSystem)
	
	def buildGroup(self, army, row, modifier):
		split = row.split(',')
		stats = deque(row.split(','))
		count = int(stats.popleft())
		hp = int(stats.popleft())
		immune = list()
		weak = list()
		aType = None
		attack = 0
		
		while len(stats):
			i = stats.popleft()
			if i.startswith('attack'):
				aStats = i.split(' ')
				aType = aStats[1]
				attack = int(aStats[2])
				break
			if i.startswith('weak:'):
				i = i.replace('weak:', '')
				weak.append(i)
				
			if i.startswith('immune:'):
				i = i.replace('immune:', '')
				immune.append(i)			
		
		ini = int(stats.popleft())
		return {'army': army,'size': count, 'hp': hp, 'immune': immune, 'weak': weak, 'type': aType, 'attack': attack + modifier, 'ini': ini}
		
	
	def solution(self, inputImmune, inputInfection):
		
		lastWin = 0
		lastSize = 0
		currentMod = 0

		while True:
			#this is a hack.. these trigger infinite loops. @todo Fix that.
			if currentMod in [44, 45, 46, 47, 48]:
				success = False
			else:
				size, success = self.attempt(inputImmune, inputInfection, currentMod)

			
			if success:
				lastWin = currentMod
				lastSize = size
				break

			currentMod += 1

		
		print('Solution Here %s %s' % (lastWin, lastSize))
		return lastSize

	def attempt(self, inputImmune, inputInfection, modifier):
		immune, infect = self.parseData(inputImmune,inputInfection, modifier)
		while True:
			#target selection
			turns = self.assignTargetingTurns(immune, infect)
			targets = list()
			targetOrder = []
			while len(turns):
				v, group = heapq.heappop(turns)
				enemy = infect
				if group['army'] == 'infection':
					enemy = immune
				
				baseDamage = group['size'] * group['attack']
				target = None
				damage = 0
				for i in enemy:
					if i in targets:
						continue
					
					targetDamage = baseDamage

					if group['type'] in i['weak']:
						targetDamage *= 2
					if group['type'] in i['immune']:
						targetDamage = 0
						continue
					if target == None or targetDamage > damage:
						target = i
						damage = targetDamage
					elif targetDamage == damage:
						te = target['size'] * target['attack'] 
						ie = i['size'] * i['attack']
						if (ie > te):
							target = i
							damage = targetDamage
						elif (te == ie and i['ini'] > target['ini']):
							target = i
							damage = targetDamage
				
				if target:
					targets.append(target)
					heapq.heappush(targetOrder, (-group['ini'], group, target))
			
			while len(targetOrder):
				ini, attacker, defender = heapq.heappop(targetOrder)
				if attacker['size'] == 0 or defender['size'] == 0:
					continue
				
				attack = attacker['size'] * attacker['attack']
				if attacker['type'] in defender['weak']:
					attack *= 2
					
				hp = defender['size'] * defender['hp']
				hp -= attack
				
				if hp <= 0:
					defender['size'] = 0
					continue
				
				
				newSize = math.ceil(hp / defender['hp'])
				defender['size'] = newSize
				test = 'a'
						
			for i in immune:
				if i['size'] == 0:
					immune.remove(i)
					
			for i in infect:
				if i['size'] == 0:
					infect.remove(i)		
			
			if len(infect) == 0 or len(immune) == 0:
				break
		
		winner = immune
		immuneWin = True
		if len(infect):
			winner = infect
			immuneWin = False
			
		size = 0
		for i in winner:
			size += i['size']
			
		return size, immuneWin

	def assignTargetingTurns(self, immune, infect):
		turns = []
		
		for im in immune:
			heapq.heappush(turns, ((-100 * im['size'] * im['attack']) - im['ini'], im))
			
		for inf in infect:
			heapq.heappush(turns, ((-100 * inf['size'] * inf['attack']) - inf['ini'], inf))
		
		return turns
		

	def run(self):
		inputImmune = common.loadInput('immune.txt', True) 
		inputInfection = common.loadInput('infection.txt', True)
		print('Advent Day: %s' % self.solution(inputImmune, inputInfection))
		



if __name__ == '__main__':
	Solution().run()
