#from datetime import datetime
import re
import sys
sys.path.append('../')
from scaffolding import common

print("Advent 4.a")

inputList = common.loadInput('input.txt')
#numberList = common.pullNumbersFromList(inputList)

def processInput():
	actions = dict()
	for row in inputList:
		m = re.search('[^\[]+(?=\])', row)
		date = m.group(0).strip()	

		m = re.search('\](.*)', row)
		action = m.group(0)[1:].strip()

		actions[date] = action

	return actions

def processGuards(actions):
	guards = dict()
	currentGuard = 0;
	timeAsleep = None

	dates = list(actions.keys())
	dates.sort()
	#print(actions.keys())

	for date in dates:
		action = actions[date]
		m = re.search('([0-9])\w+', action)

		if (m is not None):
			currentGuard = m.group(0)
			if (currentGuard not in guards.keys()):
				guards[currentGuard] = {'asleep': 0, 'actions': dict(), 'sleepTimes': dict()}
			timeAsleep = None
		elif(currentGuard != 0) :
			guards[currentGuard]['actions'][date] = action

		if action == 'falls asleep' and timeAsleep == None:
			timeAsleep = date.split(':')[1]

		if action == 'wakes up' and timeAsleep != None:
			sleepTime = int(date.split(':')[1]) - int(timeAsleep) 
			guards[currentGuard]['asleep'] = guards[currentGuard]['asleep'] + sleepTime
			findTimesAlseep(guards[currentGuard], int(timeAsleep), int(date.split(':')[1]))

			timeAsleep = None

	return guards

def findGuardMostASleep(guards):
	mostSleepTime = 0
	mostASleepGuard = None

	for id,guard in guards.items():
		if guard['asleep'] > mostSleepTime:
			mostASleepGuard = id
			mostSleepTime = guard['asleep']

	return mostASleepGuard



def findTimesAlseep(guard, timeAsleep, awakeTime):
	for i in range(timeAsleep, awakeTime):
		if i not in guard['sleepTimes'].keys():
			guard['sleepTimes'][i] = 1
		else:
		 	guard['sleepTimes'][i] = guard['sleepTimes'][i] + 1

def findTimeGuardIsMostAsleep(guard):
	mostSleepTime = 0
	highestCount = 0

	for minute,count in guard['sleepTimes'].items():
		if count > highestCount:
			mostSleepTime = minute
			highestCount = count

	return mostSleepTime



def run():
	actions = processInput()
	guards = processGuards(actions)
	guardAsleep = findGuardMostASleep(guards)
	timeMostLikelyAsleep = findTimeGuardIsMostAsleep(guards[guardAsleep])

	print('Guard is #%s who is asleep for %i multipled that is %i' % (guardAsleep, timeMostLikelyAsleep, int(guardAsleep) * timeMostLikelyAsleep))


run()
#def updateGuard(guard, action)