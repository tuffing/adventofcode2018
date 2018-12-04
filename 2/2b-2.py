from collections import Counter
from timeit import Timer


print("2b optimal attempt")

inputFile = open('input.txt', 'r')
inputList = inputFile.read().strip().split()
inputFile.close()

def runTestPass1():
	linelength = len(inputList[0])
	matchLength = linelength - 1
	firstCheck = 3

	rows = dict()
	for row in inputList:
		rows[row] = []


	abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	for x in range(linelength):
		letterMatches = dict()

		for l in abc:
			letterMatches[l] = []
			for r in rows.keys():
				if r[x] == l:
					letterMatches[l].append(r)
		

			for match in letterMatches[l]:
				rows[match].extend(letterMatches[l])


	for r in rows.keys():
		#print(rows[r])
		data = Counter(rows[r])
		#if data.most_common(1)[0][1] > 5:
			#print data.most_common(1)[0][1]
		
		if data.most_common(2)[1][1] == matchLength:
			print('Found %s' % data.most_common(2)[1][0])
			print('The common letters are %s' % ''.join(list(filter(lambda x:x in list(data.most_common(2)[1][0]), r))))
			break
	print('the end')

#print("2b-2\n----")
#t = Timer("runTestPass1()", "from __main__ import runTestPass1")
#print("Time: %s\n----------------" % t.timeit(number=1)) 

def runTestPass2():
	linelength = len(inputList[0])
	matchLength = linelength - 1
	firstCheck = 3

	rows = dict()
	for row in inputList:
		rows[row] = []


	abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	for x in range(linelength):
		letterMatches = dict()

		for r in rows.keys():
			if r[x] in letterMatches.keys():
				letterMatches[r[x]].append(r)
			else:
				letterMatches[r[x]] = [r]
		
		for letter in letterMatches.keys():
			for match in letterMatches[letter]:
				rows[match].extend(letterMatches[letter])


	for r in rows.keys():
		#print(rows[r])
		data = Counter(rows[r])
		#if data.most_common(1)[0][1] > 5:
			#print data.most_common(1)[0][1]
		
		if data.most_common(2)[1][1] == matchLength:
			print('Found %s' % data.most_common(2)[1][0])
			print('The common letters are %s' % ''.join(list(filter(lambda x:x in list(data.most_common(2)[1][0]), r))))

			break
	print('the end')


runTestPass1()

print("2b-2\n----")
t = Timer("runTestPass2()", "from __main__ import runTestPass2")
print("Time: %s\n----------------" % t.timeit(number=1)) 