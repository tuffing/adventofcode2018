import sys
sys.path.append('../')
from scaffolding import common
from collections import deque

inputFile = open('input.txt', 'r')
text = inputFile.read().strip()
inputFile.close()

print("Advent 5a.")


checked = deque()

for t in text:
	if len(checked) == 0:
		checked.append(t)
		continue

	previous = checked[len(checked) - 1]
	if (previous.islower() and previous.upper() == t) or (previous.isupper() and previous.lower() == t):
		checked.pop()
		continue

	checked.append(t)



print("length %s" % len(checked))





