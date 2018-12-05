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

Something a lot of people did was to use a dictionary instead of a 2d array. The key would just a be a string 'x,y'. in terms of time not much lost, theortically a little more efficient

##4 https://adventofcode.com/2018/day/4
### pt a 
Find the guard that sleeps the most 

###pt b 
Of all guards, which guard is most frequently asleep on the same minute?

###neat tricks i found / saw people doing
This would of been perfect for defaultDict. Would of saved a heap of time finding the maxes as i could of used either lambdas or Counter with it. To do list for the weekend, go over this library, get it's syntax down pat! I'll no doubt have use for these libraries a lot before the challenge is over. 

Example here would have been to use a counter instead of having to run the findTimesAlseep function

##5 https://adventofcode.com/2018/day/5
### pt a 
How many units remain after fully reacting the polymer you scanned? 

###pt b 
What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?

###neat tricks i found / saw people doing
First time most solutions were similar to mine. Essentially treating this problem the same way you match parenthesis - using a stack and looping through the text only once. There were some people who used stirng replace over and over but that appears to be significantly slower than this approach 

Also string.ascii_lowercase is a short cut for the alphabet

