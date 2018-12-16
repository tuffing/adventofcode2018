#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common
import copy
from collections import deque, defaultdict, Counter

class Solution(object):
    #inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

    def __init__(self):
        pass

    def solution(self, inputList):
        commands = deque(inputList)
        reg = [0,0,0,0]
        while len(commands):
            instruction = list(map(int, commands.popleft().split(' ')))

            if instruction[0] == 0:
                #BORR	0
                self.borr(reg, instruction)
            elif instruction[0] == 1:
                #ADDR	1
                self.addr(reg, instruction)
            elif instruction[0] == 2:
                #EQRR	2
                self.eqrr(reg, instruction)
            elif instruction[0] == 3:
                #ADDI	3
                self.addi(reg, instruction)
            elif instruction[0] == 4:
                #EQRI	4
                self.eqri(reg, instruction)
            elif instruction[0] == 5:
                 #EQIR	5
                self.eqir(reg, instruction)
            elif instruction[0] == 6:
                #GTRI	6
                self.gtri(reg, instruction)
            elif instruction[0] == 7:
                #MULR	7
                self.mulr(reg, instruction)
            elif instruction[0] == 8:
                #SETR	8
                self.setr(reg, instruction)
            elif instruction[0] == 9:
                #GTIR	9
                self.gtir(reg, instruction)
            elif instruction[0] == 10:
                #MULI	10
                self.muli(reg, instruction)
            elif instruction[0] == 11:
                #BANR	11
                self.banr(reg, instruction)
            elif instruction[0] == 12:
                #SETI	12
                self.seti(reg, instruction)
            elif instruction[0] == 13:
                #GTRR	13
                self.gtrr(reg, instruction)
            elif instruction[0] == 14:
                #BANI	14
                self.bani(reg, instruction)
            elif instruction[0] == 15:
                #BORI	15
                self.bori(reg, instruction)
            print(reg)
            
			
        print(reg[0])
                    
        #print(reg)
        #return total


    def addr(self, registers, instruction):
        #addr (add register) stores into register C the result of adding register A and register B.
        if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
            print('invalid')
            
            return

        registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]

    def addi(self, registers, instruction):
        #addi (add immediate) stores into register C the result of adding register A and value B.
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]] + instruction[2]

    def mulr(self, registers, instruction):
        #mulr (multiply register) stores into register C the result of multiplying register A and register B.
        if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]

    def muli(self, registers, instruction):
        #muli (multiply immediate) stores into register C the result of multiplying register A and value B.
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]] * instruction[2]		

    def banr(self, registers, instruction):
        #banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
        if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]

    def bani(self, registers, instruction):
        #bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]] & instruction[2]

    def borr(self, registers, instruction):
        #borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
        if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]

    def bori(self, registers, instruction):
        #bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]] | instruction[2]


    def setr(self, registers, instruction):
        #setr (set register) copies the contents of register A into register C. (Input B is ignored.)
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            
            return	
        registers[instruction[3]] = registers[instruction[1]]

    def seti(self, registers, instruction):
        #seti (set immediate) stores value A into register C. (Input B is ignored.)	
        
   
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')    
            return
        
        
        registers[instruction[3]] = instruction[1]

    def gtir(self, registers, instruction):
        #gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            
            return

        if instruction[1] > registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0

    def gtri(self, registers, instruction):
        #gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.

        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            
            return

        if registers[instruction[1]] >  instruction[2]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0

    def gtrr(self, registers, instruction):
        #gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.

        if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
            print('invalid')
            return	

        if registers[instruction[1]] > registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0

    def eqir(self, registers, instruction):
        #eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            return

        if instruction[1] == registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0

    def eqri(self, registers, instruction):
        #eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.

        if instruction[1] > 3  or instruction[3] > 3:
            print('invalid')
            return

        if registers[instruction[1]] ==  instruction[2]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0

    def eqrr(self, registers, instruction):
        #eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.

        if instruction[1] > 3 or instruction[2] > 3 or instruction[3] > 3:
            print('invalid')
            return	

        if registers[instruction[1]] == registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0


    def run(self):
        inputList = common.loadInput('input2.txt', True) #True = split, False = string
        print('Advent Day: %s' % self.solution(inputList))




if __name__ == '__main__':
    Solution().run()
