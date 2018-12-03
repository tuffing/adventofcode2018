# advent of code 2018

https://adventofcode.com/

##1: https://adventofcode.com/2018/day/1
###pt a:
Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

###pt b:
What is the first frequency your device reaches twice? (input loops infinitely)

### simple tricks i saw other people use that i liked
	print(sum(map(int, lines))) #one liner (excluding lines import) for the first part

	there is a native python library called itertools. it's got a number of useful array functions like cycle which could remove the while(true). No specific gain but would reduce line count

##2: https://adventofcode.com/2018/day/2
### pt a:
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

### pt b
find the closest matching sum

### useful tricks I found doing this / read other people do
discovered the collections library while doing pt b. made use of the deque collection. Very fast queue.

Someone else used the Counter collection for the first part which would of significantly simplied the function.

Loops in python support enumerate, which allows you to get a counter for the current progress through the loop

Occured to me afterwards, rather than use the levenshtein distance an easy way to score it manually would be to loop through each character and for each non match, add one. As the strings are all the same length.

I notice a lots of solutions assume the lowest score will be 1 - which the text never explicitly says. Making this assumption does remove a significant amount of code however

##3 https://adventofcode.com/2018/day/3
### pt a
Find the points on the grid being overlapped

### pt b
Find the one rectangle that isn't overlapping anything

###neat tricks i found / saw people doing
A nice simple way to parse the data was this:
map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

Pretty much exploitng map and all the values we needed were numbers. Clever. I see being able to use this a lot in this challenge

Should play with the map function more often actually..