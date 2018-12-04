#from datetime import datetime
import re


print("Advent 4.a")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split('\n')
inputFile.close()


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

			#if (currentGuard == '211'):
			#	print('here')

			timeAsleep = None

	return guards

def findGuardMostASleep(guards):
	mostSleepCount = 0
	mostASleepGuard = None

	for id,guard in guards.items():
		if guard['minuteMostAsleepCount'] > mostSleepCount:
			mostASleepGuard = id
			mostSleepCount = guard['minuteMostAsleepCount']

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
	print(guard['sleepTimes'])
	for minute,count in guard['sleepTimes'].items():
		if count > highestCount:
			mostSleepTime = minute
			highestCount = count

	guard['minuteMostAsleep'] = mostSleepTime
	guard['minuteMostAsleepCount'] = highestCount


def processGuardsMostSleptAtMinute(guards):
	for g in guards:
		findTimeGuardIsMostAsleep(g)

def run():
	actions = processInput()
	guards = processGuards(actions)
	processGuardsMostSleptAtMinute(guards)
	guardAsleep = findGuardMostASleep(guards)
	guard = guards[guardAsleep]
	#timeMostLikelyAsleep = findTimeGuardIsMostAsleep(guards[guardAsleep])


	print('Guard is #%s who is most asleep %i times at %i multipled that is %i' % (guardAsleep, guard['minuteMostAsleepCount'], guard['minuteMostAsleep'],guard['minuteMostAsleepCount'] * guard['minuteMostAsleep']))


run()
#def updateGuard(guard, action)