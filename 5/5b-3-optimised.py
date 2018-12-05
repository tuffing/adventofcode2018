import sys
sys.path.append('../')
from scaffolding import common
from collections import deque
from timeit import Timer


inputFile = open('input.txt', 'r')
mainText = inputFile.read().strip()
inputFile.close()

print("Advent 5b. optimised")


def react(text):
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

	return checked


def run():
	abc = 'abcdefghijklmnopqrstuvwxyz'
	smallestLetter = None
	smallestNumber = -1

	startText = "".join(react(mainText))

	for l in abc:
		newText = startText.replace('%s' % (l), '').replace('%s' % (l.upper()), '')

		count = len(react(newText))

		if smallestNumber == -1 or  count < smallestNumber:
			smallestNumber = count
			smallestLetter = l

		

	print("lengtha %s %s" % (smallestNumber, smallestLetter))


print("5b optimised by reacting the original string and using the result for all checks from then on\n----")
t = Timer("run()", "from __main__ import run")
print("Time: %s\n----------------" % t.timeit(number=1)) #about 77 milliseconds


