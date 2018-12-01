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