# advent of code 2018

https://adventofcode.com/

Faster implementations are marked as optimal.. at least until i find a more optimal solution


## 1: https://adventofcode.com/2018/day/1

### pt a:

Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

### pt b:

What is the first frequency your device reaches twice? (input loops infinitely)

### simple tricks i saw other people use that i liked
print(sum(map(int, lines))) #one liner (excluding lines import) for the first part
There is a native python library called itertools. it's got a number of useful array functions like cycle which could remove the while(true). No specific gain but would reduce line count

## 2: https://adventofcode.com/2018/day/2

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

## 3 https://adventofcode.com/2018/day/3

### pt a

Find the points on the grid being overlapped

### pt b

Find the one rectangle that isn't overlapping anything

### neat tricks i found / saw people doing

A nice simple way to parse the data was this:
map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

Pretty much exploitng map and all the values we needed were numbers. Clever. I see being able to use this a lot in this challenge

Something a lot of people did was to use a dictionary instead of a 2d array. The key would just a be a string 'x,y'. in terms of time not much lost, theortically a little more efficient

## 4 https://adventofcode.com/2018/day/4

### pt a 

Find the guard that sleeps the most 

### pt b 

Of all guards, which guard is most frequently asleep on the same minute?

### neat tricks i found / saw people doing

This would of been perfect for defaultDict. Would of saved a heap of time finding the maxes as i could of used either lambdas or Counter with it.  

Example here would have been to use a counter instead of having to run the findTimesAlseep function

someone suggested this algorithm could be adapted: https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/ should check it out and play with it

## 5 https://adventofcode.com/2018/day/5

### pt a 

How many units remain after fully reacting the polymer you scanned? 

### pt b 

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?

### neat tricks i found / saw people doing

First time most solutions were similar to mine. Essentially treating this problem the same way you match parenthesis - using a stack and looping through the text only once. There were some people who used stirng replace over and over but that appears to be significantly slower than this approach 

Also string.ascii_lowercase is a short cut for the alphabet

## 6 https://adventofcode.com/2018/day/6

### pt a 

Given a bunch of points on a grid, based on the closest points to each area what is the size of the largest area that isn't infinite (it's range doesn't touch the border)? Use Manhattan distance

### pt b 

Find the size of the area in which every spot on the grid is less than 10000 steps away from every point

### neat tricks i found / saw people doing

Had to read up on the Manhattan distance, also known as Taxicab geometry. It's calculated via the equation abs(x1 - x2) + abs(y1 - y2)

Investigate solving this with https://en.wikipedia.org/wiki/K-d_tree or using voronoi as an approach https://stackoverflow.com/questions/973094/easiest-algorithm-of-voronoi-diagram-to-implement

## 7 https://adventofcode.com/2018/day/7

### pt a 

"In what order should the steps in your instructions be completed?" based on a list of steps with requirements with text like "Step K must be finished before step Y can begin."

### pt b 

With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps? E.g the first step now takes time but also has multiple processes

### neat tricks i found / saw people doing

Nice way of merging a list of list down into one list
``` set([s[0] for s in simplified] + [s[1] for s in simplified])
```

Same solution used this to grab the next steps. I thought it was a clever one liner though in practice id rarely use something like this, i try to keep one liners simpler.

```[s for s in steps if all(b != s for (_, b) in l)]```



## 8 https://adventofcode.com/2018/day/8

### pt a 

Given a string of numbers, use it to build a tree based on some rules and then What is the sum of all metadata entries?

### pt b 

the meta values are now indexes if the current node has children. What is the value of the root node?

### neat tricks i found / saw people doing

Noticed most people used recursion in much the same way i did this time. Saw some very elegant uses of lambdas in sums and pythons list slicing abilities using ':'


## 9 https://adventofcode.com/2018/day/9

### pt a 

What is the winning Elf's score?

### pt b 

times the number of marbles by 100 and then find the highest score

### neat tricks i found / saw people doing

Come part 2 it was obvious i needed a faster way of doing it so used a linked list. My instinct was that deque was a linked list (which it was) but my bad research showed that i couldn't rotate through it easily. So i implemented my own linked list. Significant speed improvement on part 1 though.

Of course as soon as i look at other peoples solutions the first one is using deque, exactly in the way i guessed it could be used.. grrrr. Should of taken more time to research. Redid 9 ptb again to make use of this knowledge. Halved the time again

## 10 https://adventofcode.com/2018/day/10

### pt a 

What is the word that appears when the points come together on the grid

### pt b 

how many seconds did this take

### neat tricks i found / saw people doing

The final solution i made for this solution would only actually work on bigger data sets as long as the veliocity's are pretty high and the word not too long. It actually fails on the HI example. My previous solution was to wait until the difference in width was below a threshold and then wait for user input to progress, a better solution would of actually used the height - as the highest possible character is 10


## 11 https://adventofcode.com/2018/day/11

### pt a 

What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with the largest total power?

### pt b 

What is the X,Y,size identifier of the square with the largest total power?

### neat tricks i found / saw people doing

The final solution i made for this solution would only actually work on bigger data sets as long as the veliocity's are pretty high and the word not too long. It actually fails on the HI example. My previous solution was to wait until the difference in width was below a threshold and then wait for user input to progress, a better solution would of actually used the height - as the highest possible character is 10