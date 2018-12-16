#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
import copy
from collections import deque, defaultdict

class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputList):
		commands = deque(inputList)
		total = 0
		
		while len(commands):
			#list(map(int, results))
			registers = list(map(int, commands.popleft().replace('Before: [', '').replace(']', '').split(',')))
			instruction = list(map(int, commands.popleft().split(' ')))
			expectedResult = list(map(int,commands.popleft().replace('After:  [', '').replace(']', '').split(',')))
			if len(commands):
				commands.popleft()
				
			if self.testInstruction(registers, instruction, expectedResult) >= 3:
				total += 1			
		
		#registers = [3, 2, 1, 1]
		#instruction = [9, 2, 1, 2]
		#expectedResult =  [3, 2, 2, 1]
		
		#total = 0
		#if self.testInstruction(registers, instruction, expectedResult) >= 3:
		#	total += 1
			
		return total
	
	def testInstruction(self, registers, instruction, expectedResult):
		#instruction Op A B C
		#addr
		possibleMatches = 0
		
		addr = copy.copy(registers)
		self.addr(addr, instruction)
		if (addr == expectedResult):
			print('addr')
			possibleMatches += 1
		
		#addi
		addi = copy.copy(registers)
		self.addi(addi, instruction)
		if (addi == expectedResult):
			print('addi')
			possibleMatches += 1
			
		#mulr
		mulr = copy.copy(registers)
		self.mulr(mulr, instruction)
		if (mulr == expectedResult):
			print('mulr')
			possibleMatches += 1
			
		#muli
		muli = copy.copy(registers)
		self.muli(muli, instruction)
		if (muli == expectedResult):
			print('muli')
			possibleMatches += 1
			
		#banr
		banr = copy.copy(registers)
		self.banr(banr, instruction)
		if (banr == expectedResult):
			print('banr')
			possibleMatches += 1
			
		#bani
		bani = copy.copy(registers)
		self.bani(bani, instruction)
		if (bani == expectedResult):
			print('bani')
			possibleMatches += 1
		
		#borr
		borr = copy.copy(registers)
		self.borr(borr, instruction)
		if (borr == expectedResult):
			print('borr')
			possibleMatches += 1
			
		#bori
		bori = copy.copy(registers)
		self.bori(bori, instruction)
		if (bori == expectedResult):
			print('bori')
			possibleMatches += 1
		
		#setr
		setr = copy.copy(registers)
		self.setr(setr, instruction)
		if (setr == expectedResult):
			print('setr')
			possibleMatches += 1
			
		#seti
		seti = copy.copy(registers)
		self.seti(seti, instruction)
		if (seti == expectedResult):
			print('seti')
			possibleMatches += 1
			
		#gtir
		gtir = copy.copy(registers)
		self.gtir(gtir, instruction)
		if (gtir == expectedResult):
			print('gtir')
			possibleMatches += 1
			
		#gtri
		gtri = copy.copy(registers)
		self.gtri(gtri, instruction)
		if (gtri == expectedResult):
			print('gtri')
			possibleMatches += 1
			
		#gtrr
		gtrr = copy.copy(registers)
		self.gtrr(gtrr, instruction)
		if (gtrr == expectedResult):
			print('gtrr')
			possibleMatches += 1
			
		#eqir
		eqir = copy.copy(registers)
		self.eqir(eqir, instruction)
		if (eqir == expectedResult):
			print('eqir')
			possibleMatches += 1
			
		#eqri
		eqri = copy.copy(registers)
		self.eqri(eqri, instruction)
		if (eqri == expectedResult):
			print('eqri')
			possibleMatches += 1
			
		#eqrr
		eqrr = copy.copy(registers)
		self.eqrr(eqrr, instruction)
		if (eqrr == expectedResult):
			print('eqrr')
			possibleMatches += 1
		
		return possibleMatches
	
	def addr(self, registers, instruction):
		#addr (add register) stores into register C the result of adding register A and register B.
		if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
			return
		
		registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]
		
	def addi(self, registers, instruction):
		#addi (add immediate) stores into register C the result of adding register A and value B.
		if instruction[1] > 3  or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]] + instruction[2]
		
	def mulr(self, registers, instruction):
		#mulr (multiply register) stores into register C the result of multiplying register A and register B.
		if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]
	
	def muli(self, registers, instruction):
		#muli (multiply immediate) stores into register C the result of multiplying register A and value B.
		if instruction[1] > 3  or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]] * instruction[2]		

	def banr(self, registers, instruction):
		#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
		if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]
	
	def bani(self, registers, instruction):
		#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
		if instruction[1] > 3  or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]] & instruction[2]
		
	def borr(self, registers, instruction):
		#borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
		if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]
	
	def bori(self, registers, instruction):
		#bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
		if instruction[1] > 3  or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]] | instruction[2]
	
			
	def setr(self, registers, instruction):
		#setr (set register) copies the contents of register A into register C. (Input B is ignored.)
		if instruction[1] > 3  or instruction[3] > 3:
			return	
		registers[instruction[3]] = registers[instruction[1]]
	
	def seti(self, registers, instruction):
		#seti (set immediate) stores value A into register C. (Input B is ignored.)	
		if instruction[1] > 3  or instruction[3] > 3:
			return	
		registers[instruction[3]] = instruction[1]
		
	def gtir(self, registers, instruction):
		#gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
		if instruction[1] > 3  or instruction[3] > 3:
			return
		
		if instruction[1] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def gtri(self, registers, instruction):
		#gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
		
		if instruction[1] > 3  or instruction[3] > 3:
			return
		
		if registers[instruction[1]] >  instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def gtrr(self, registers, instruction):
		#gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.

		if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
			return	
		
		if registers[instruction[1]] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0

	def eqir(self, registers, instruction):
		#eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
		if instruction[1] > 3  or instruction[3] > 3:
			return
		
		if instruction[1] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def eqri(self, registers, instruction):
		#eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
		
		if instruction[1] > 3  or instruction[3] > 3:
			return
		
		if registers[instruction[1]] ==  instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def eqrr(self, registers, instruction):
		#eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.

		if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
			return	
		
		if registers[instruction[1]] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0


	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: %s' % self.solution(inputList))
		



if __name__ == '__main__':
	Solution().run()
