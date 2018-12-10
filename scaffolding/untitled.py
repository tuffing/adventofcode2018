	inputFile = open(filename, 'r')
	text = inputFile.read().strip().text.split('\n')
	inputFile.close()


	if len(text) == 0:
		return