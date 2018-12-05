import re

def loadInput(filename, splitIntoArray=True):
	inputFile = open(filename, 'r')
	text = inputFile.read().strip()
	if (splitIntoArray):
		return text.split('\n')

	return text
	
	inputFile.close()

def pullNumbersFromList(data, includeSigns = True):
	reg = r'\d+'
	if (includeSigns):
		reg = r'-?\d+'

	return list(map(lambda s: list(map(int, re.findall(reg, s))), data))[0]