# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:22:21 2022

@author: MY PC
"""

"""
1.What are the two values of the Boolean data type? How do you write them?
The 2 values of BOOLEAN are True and False
2. What are the three different types of Boolean operators?
and, or, not
3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
True	and	True	True
True	and	False	False
False	and	True	False
False	and	False	False
True	or	True	True
True	or	False	True
False	or	True	True
False	or	False	False
not	True	False
not	False	True
4. What are the values of the following expressions?
(5 > 4) and (3 == 5) -- False
not (5 > 4) --False
(5 > 4) or (3 == 5) -- True
not ((5 > 4) or (3 == 5)) -- False
(True and True) and (True == False) -- False
(not False) or (not True) -- True
5. What are the six comparison operators?
>,<,>=,<=,==,!=
6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
= is an assignment operator, whereas == is a comparison operator.
a=10 means the value of a is 10
a==10 returns a boolean output based on wether the value of 1 is 10 or not.
7. Identify the three blocks in this code:
spam = 0   -- block 1
if spam == 10:  -- block 2
print('eggs')
if spam > 5:    -- block 3
print('bacon')
else:
print('ham')
print('spam')
print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam= int(input())
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings!")
9.If your programme is stuck in an endless loop, what keys you’ll press?
CTRL+c
10. How can you tell the difference between break and continue?
Break is used ot break out of a loop, 
wheras continue is used to skip the current loop(ignoring the rest of the code in the current loop) and move on to the next iteration.
11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
All the 3 return the same result. However, they are different in terms of execution.
range(10)- it will begin from 0 as default till the iteration reaches 10
range(0, 10) - it will begin with 0 and end with 10 with default jumps of 1 in every iteration
range(0, 10, 1) - it will begin with 0 and end with 10 with jump of 1 mentioned in the third argument.
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1,11):
    print(i)
i=1
while i<11:
    print(i)
    i=i+1
13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()
"""


    