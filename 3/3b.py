import re

print("Advent 3.b")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split('\n')
inputFile.close()


def buildGrid():
	n = 1300
	m = 1300
	a = [[''] * m for i in range(n)]

	return a

def processRow(row):
	m = re.search('[^\@]+(?=\:)', row)
	leftTop = m.group(0).strip().split(',')
	

	m = re.search('\:(.*)', row)
	widthHeight = m.group(0)[1:].strip().split('x')

	m = re.search('(.*)\@', row)
	id = m.group(0)[:-1]

	return {"id": id,"left": int(leftTop[0]), "top": int(leftTop[1]), "width": int(widthHeight[0]), "height": int(widthHeight[1]), "overlapped": False}

def layoutRectangles(block, grid, blocks):
	y = block['top']
	for y in range(block['top'], block['top'] + block['height']):
		for x in range(block['left'], block['left'] + block['width']):
			if grid[x][y] == '':
				grid[x][y] = block['id']
			else:
				if grid[x][y] == '#297' or block['id'] == '#297':
					print('its a di')
				blocks[grid[x][y]]['overlapped'] = True
				block['overlapped'] = True


def process():
	grid = buildGrid()
	blocks = {}
	overlapCount = 0

	for row in inputList:
		block = processRow(row)
		blocks[block['id']] = block
		layoutRectangles(block, grid, blocks)

	print('non overlap is %s' % next(filter(lambda x: x['overlapped'] == False,  blocks.values())))

process()