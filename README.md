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

### neat tricks i found / saw people doing / notes

The most effiecient solutions I saw in python used scientific libraries like numpy. 
One of my challenges is to solve these with out 3rd party plugins. 

Solb2 was extremely inefficient as it did 0 partial sums. So in solb2 I tried using the sum of the previous size and adding to it.
This speed things up but it's still pretty bad ~5 minutes or so. 

Solb3, i realised that as long as the size of the grid isn't a prime, i can build the total from all the smaller sizes that came before it.
Prime numbers will still need the solb2 solution but otherwise this gave a substationial improvement. Down to about 55 seconds. 
I could probably get a tiny little more time by filling in prime numbers with lots of smaller squares, 
theortically I could half the number of iterations needed to build the prime totals. 

Made solution 4  use this: https://en.wikipedia.org/wiki/Summed-area_table It is substationally faster than my previous fasted at about 14 seconds. 

## 12 https://adventofcode.com/2018/day/12

### pt a 

Given some plants in a row and some rules, After 20 generations, what is the sum of the numbers of all pots which contain a plant?

### pt b 

Repeat for 50000000000 generations

### neat tricks i found / saw people doing / notes

Another one where many of the solutions are common. main difference was how the end ranges were managed. Mix of appending 2 dots or 4 etc. 

Attempted to come up with a more effiecient solution to calculate this, but the timing worked out the same to my original attempt. 
After much too long i decided to review the states for the first 1000 rows. Turns out there's a pattern. Once i did this i just needed to 
look until the pattern was hit and from there we can just calculate the score using math. Turns out this is what most others did too

## 13 https://adventofcode.com/2018/day/13

### pt a 

Find the first collision in a track of carts

### pt b 

If carts are removed of a crash, what is the coords of the last remaining cart

### neat tricks i found / saw people doing / notes

Funnist one yet, I want to turn this into an animation

Many solutions to this, a few used my approach of hard coding the directions. Same reason as me (sanity). A few used vectors which i might also do an implementation with at some point.

Found a very clever solution using math! Complex numbers particlarly. I want to do an implementation using this concept at some point:
https://www.reddit.com/r/adventofcode/comments/a5qd71/2018_day_13_solutions/ebolyq6/

His explanation:
>> Really liked this one. I solved it with complex numbers, which is a trick I learned from earlier years. Instead of storing x and y, store position = x + y * i (written y * 1j in python).
>>
>> The best part about this is that directions are just one of the numbers +1, +1j, -1, -1j and changing a direction is as simple as multiplying it by either +1j (clockwise turn) or -1j (counterclockwise turn).
>>
>> Note that since the Y axis is flipped (positive = down), you flip the imaginary part compared to what you'd do in usual mathematics (therefore, multiplying by +1j is CW ⭮, not CCW ⭯).

## 14 https://adventofcode.com/2018/day/14

### pt a 

following the pattern up to x, What are the scores of the ten recipes immediately after the number of recipes in your puzzle input?

### pt b 

Given the input, how many elements before it in the pattern

### neat tricks i found / saw people doing / notes
Most solutions roughly use the same concept this time round. I am beginning to notice that python might be quite slow to some of the other languages :p


The method of circling around on the list can also be done with pythons divmod tool. May or may not be a nicer way of doing it?

Some solutions involved just doing a string compare on the last 10 digits rather than have a string moving along. In retrospect i probobly could of just extracted the last x strings and did something similar (but the last 6 and 7 instead).

One solution just generated the first 500000 and then searched the results for the first appearance of the string.


## 15 https://adventofcode.com/2018/day/15

### pt a 

Given the someone intricate rules what is the result of the combat (answer is rounds * hp remaining)

### pt b 

What is the minimum attack power needed for all of the elves to survice

### neat tricks i found / saw people doing / notes
From the solutions a good santity saver here are python dataclasses

Looking at the score board and reddit this might be the most universally most difficult puzzle to get right.

This was an unsual puzzle in which most of the solutions users gave don't actually work for inputs.
The person solving it just got very lucky they didn't get some of the more suble and annoying edge cases

My choice of Dijkstra's algorithm  may have been over kill :p A lot of people used a breadth first search to find the closest accessible 
person. I might reimplment using that approach later down the track as it seems very fast here. I've always wanted to take a shot at a Dijkstra's algorithm. 

I noticed one advantage of using this algorithm though is selecting the direction to go based on the rules was always trivial - 
a lot of solutions got stuck on this step (though a lot of people got lucky and the're inputs worked anyway).
Unfortunately I got stuck on other bug bears.

I'm not happy with the speed, should eventually come back and optimise. Current solution is about 1 minute for part 1 and 4-5 for part 2. 
My Dijkstra's algorithm is no doubt what's causing the slow down here. Even with it terminating roughly as soon as it finds the shortest path

## 16 https://adventofcode.com/2018/day/16

### pt a 

Given a list of opcode commands and the registry before and after, find out how many opcodes are valid for each

### pt b 

deduct what each opcode does then run the program

### neat tricks i found / saw people doing / notes
Edit: Implemented this, took less than 10 minutes given my current code :p
One my todo list is to redo this one but entirely automated. Including deducting down the opcodes - this would be an easy step 
from where i am in sol16b as i've already done he hard part. 

I was sneaky and did the deduction step by hand - it didnt take long 5-10 minutes. 

One solution i liked was loading functions into a list and once the op codes had been deducted, trigger the function by calling that list item

When I implement deduction I might copy this

p.s forgetting to remove a deque.pop() only needed in the previous part can be a massive time suck when your answers are mysteriously way off correct. 

## 17 https://adventofcode.com/2018/day/17

### pt a 

Given the map of clay etc How many tiles can the water reach within the range of y values in your scan?

### pt b 

how many were full

### neat tricks i found / saw people doing / notes

This is officially my favourite one so far, very fun. Left the visualisation in becaue it was cool. 

This time round part b is in part a as it only was a line or two to add.

Quite a few recursive solutions. I avoided it here as Python sucks with recursion and has a surprisingly small limit. Some people had success though.



## 18 https://adventofcode.com/2018/day/18

### pt a 

What will the total resource value of the lumber collection area be after 10 minutes?


### pt b 

1000000000

### neat tricks i found / saw people doing / notes

After solving the first one there wasn't a whole lot left to solve for number two. it was watch the pattern for a few hundred ticks
and then the same numbers started rotating through every 28. from there getting the number for 1000000000 trivial with out needing
any programming: Once the pattern starts find the mod of each value as it repeats and check if it has the same mod as our big number ( -1 as list starts at 0..).


A challenge at some point will be to code this but I doubt it'll be hard. Just monitor for when the pattern kicks in then do the math there.

The following from someone elses solution i thought was a nice way of getting the surrounding cells:
``` 
neighbors = ''.join(get(y+a, x+b) for (a, b) in
                                [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                                 (0, 1), (1, -1), (1, 0), (1, 1)])
```


## 19 https://adventofcode.com/2018/day/19

### pt a 

What value is left in register 0 when the background process halts?

### pt b 

A new background process immediately spins up in its place. It appears identical, but on closer inspection, you notice that this time, register 0 started with the value 1.

What value is left in register 0 when this new background process halts?

### neat tricks i found / saw people doing / notes

Part a was a simple modification of day 16. Part 2 was a nightmare. I eventually solved it by finding the factorixation of 
one of the values in my registry.. using google. A proper solution would be to sit down and properly understand what the input is doing
and right a more efficient version of the same code.

## 20 https://adventofcode.com/2018/day/20

### pt a 

Build the map and find the shortest distance

### pt b 

count all rooms in which you go through over 1000 doors

### neat tricks i found / saw people doing / notes

My Dijkstra algorithm from day 15 made the second part of this trivial. First half i did via just using queues and recursion for the brackets.

If I were to optimise this the first step would be to remove all the doors. Could probably not even bother with the walls.
This wouldn't improve the primary 

There was a very nice short and sweet python solution using the networkX library. 

Very jealous it's a third party library, but stuff like this makes me want to come back and do some of these using third parties.

## 21 https://adventofcode.com/2018/day/21

### pt a 

Use my day 16/19 code again against the given program. Find the value to start reg 0 with to halt the program asap.

### pt b 

Find the number to put in reg[0] that will make the program run the longest with out 

### neat tricks i found / saw people doing / notes

Part a was trivial, there was only one input entry that ever used reg 0 so i simply monitored that command and checked what it was expecting.

Part 2, I needed to go to the movies very soon, so I just put the input to run until it found a repeat. As long as it was done by the time
i got back i was happy :p

This is when i discovered that if i ran it using pypy instead id have gotten the answer with in a minute or two.

Alterntive solution to part 2 would be to reverse engineer the input program and write my own version of it's calculations. Which I might do at some point.


## 22 https://adventofcode.com/2018/day/22

### pt a 

What is the total risk level for the smallest rectangle that includes 0,0 and the target's coordinates?

### pt b 

What is the fewest number of minutes you can take to reach the target?

### neat tricks i found / saw people doing / notes

I want to come back and redo this one with an optimal solution. currently it's a 3d Dijkstra.

I suspect either A* or another trick will be effective. 

Also intend to go through and reduce my code a bit. the entire positional selection stuff can be reduced quite a bit