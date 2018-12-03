import re

print("Advent 3.a")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split('\n')
inputFile.close()


def buildGrid():
	n = 1300
	m = 1300
	a = [[0] * m for i in range(n)]

	return a

def processRow(row):
	m = re.search('[^\@]+(?=\:)', row)
	leftTop = m.group(0).strip().split(',')
	

	m = re.search('\:(.*)', row)
	widthHeight = m.group(0)[1:].strip().split('x')

	return {"left": int(leftTop[0]), "top": int(leftTop[1]), "width": int(widthHeight[0]), "height": int(widthHeight[1])}

def layoutRectangles(block, grid):
	count = 0
	y = block['top']
	for y in range(block['top'], block['top'] + block['height']):
		for x in range(block['left'], block['left'] + block['width']):
			grid[x][y] = grid[x][y] + 1
			if grid[x][y] == 2:
				count = count + 1


	return count

def process():
	grid = buildGrid()
	overlapCount = 0

	for row in inputList:
		block = processRow(row)
		overlapCount = overlapCount + layoutRectangles(block, grid)

	print('Count is %d' % overlapCount)

process()