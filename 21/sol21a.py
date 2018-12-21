#!/usr/bin/python3

import sys
#sys.path.append('../')
#from scaffolding import common
import copy
from collections import deque, defaultdict, Counter

class Solution(object):
	def __init__(self):
		pass

	def solution(self, initial, programList):
		commands = list()
		for p in programList:
			instructions = p.split(' ')
			command = [instructions.pop(0)]
			command.extend(map(int, instructions))
			commands.append(command)
			
		
		reg = [8224964,0,0,0,0,0]
		bound = initial
		pointer = 0
		count = 0
		results = set()
		last = 0
		while pointer >= 0 and pointer < len(commands):
			reg[bound] = pointer
			#print('\033c')
			#print(pointer)
			instruction = commands[pointer]
			
			if instruction[0] == 'eqrr':
				if reg[5] in results:
					print("Last entry %s" % last)
					break
				else:
					last = reg[5]
					results.add(reg[5])
			
			#print(instruction)
			getattr(self, instruction[0])(reg, instruction)
			#print(reg)
			pointer = reg[bound]
			pointer += 1
			#count += 1
			#print(count)
			
		print('Final Registry:')
		print(reg)
		
		return last
		#return total
	
	def addr(self, registers, instruction):
		#addr (add register) stores into register C the result of adding register A and register B.
		#if instruction[1] > 5 or instruction[2] > 5 or instruction[3] > 5:
		#	return
		
		registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]
		
	def addi(self, registers, instruction):
		#addi (add immediate) stores into register C the result of adding register A and value B.
		#if instruction[1] > 5  or instruction[3] > 5:
		#	return	
		registers[instruction[3]] = registers[instruction[1]] + instruction[2]
		
	def mulr(self, registers, instruction):
		#mulr (multiply register) stores into register C the result of multiplying register A and register B.
		#if instruction[1] > 5 or instruction[2] > 5 or instruction[3] > 5:
		#	return	
		registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]
	
	def muli(self, registers, instruction):
		#muli (multiply immediate) stores into register C the result of multiplying register A and value B.
		#if instruction[1] > 5  or instruction[3] > 5:
		#	return	
		registers[instruction[3]] = registers[instruction[1]] * instruction[2]		

	def banr(self, registers, instruction):
		#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
		#if instruction[1] > 5 or instruction[2] > 5 or instruction[3] > 5:
		#	return	
		registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]
	
	def bani(self, registers, instruction):
		#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
		registers[instruction[3]] = registers[instruction[1]] & instruction[2]
		
	def borr(self, registers, instruction):
		#borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
		#if instruction[1] > 5 or instruction[2] > 5 or instruction[3] > 5:
		#	return	
		registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]
	
	def bori(self, registers, instruction):
		#bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
		if instruction[1] > 5  or instruction[3] > 5:
			return	
		registers[instruction[3]] = registers[instruction[1]] | instruction[2]
	
			
	def setr(self, registers, instruction):
		#setr (set register) copies the contents of register A into register C. (Input B is ignored.)
		#if instruction[1] > 5  or instruction[3] > 5:
		#	return	
		registers[instruction[3]] = registers[instruction[1]]
	
	def seti(self, registers, instruction):
		#seti (set immediate) stores value A into register C. (Input B is ignored.)	
		#if instruction[3] > 5:
		#	return	
		registers[instruction[3]] = instruction[1]
		
	def gtir(self, registers, instruction):
		#gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
		#if instruction[1] > 5  or instruction[3] > 5:
		#	return
		
		if instruction[1] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def gtri(self, registers, instruction):
		#gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
		
		#if instruction[1] > 5  or instruction[3] > 5:
		#	return
		
		if registers[instruction[1]] >  instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def gtrr(self, registers, instruction):
		#gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B.
		#Otherwise, register C is set to 0.

		#if instruction[1] > 5 or instruction[2] > 5 or instruction[3] > 5:
		#	return	
		
		if registers[instruction[1]] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0

	def eqir(self, registers, instruction):
		#eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
		#if instruction[1] > 5  or instruction[3] > 5:
		#	return
		
		if instruction[1] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def eqri(self, registers, instruction):
		#eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
		
		#if instruction[1] > 5  or instruction[3] > 5:
		#	return
		
		if registers[instruction[1]] ==  instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
			
	def eqrr(self, registers, instruction):
		#eqrr (equal register/register) sets register C to 1 if register A is equal to register B. 
		#Otherwise, register C is set to 0.

		#if instruction[1] > 5 or instruction[2] > 5 or instruction[3] > 5:
		#	return	
		print(registers[5])
		if registers[instruction[1]] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0


	def run(self):
		inputFile = open('input.txt', 'r')
		inputList = inputFile.read().strip().split('\n')
		inputFile.close()		
		print('Advent Day: %s' % self.solution(1, inputList))
		



if __name__ == '__main__':
	Solution().run()
