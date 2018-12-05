import re

def loadInput(filename):
	inputFile = open(filename, 'r')
	return inputFile.read().strip().split('\n')
	inputFile.close()

def pullNumbersFromList(data, includeSigns = True):
	reg = r'\d+'
	if (includeSigns):
		reg = r'-?\d+'

	return list(map(lambda s: list(map(int, re.findall(reg, s))), data))[0]