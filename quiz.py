#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:47:23 2024

@author: jashanjotbrar
"""

mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
print(" ".join(mylist[1::2]))

print ('Unit 6'[-1])

my_list = [3, 2, 1]
print(my_list)

index = "Ability is a poor man's wealth".find("W")
print(index)

mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 8:
    print(mylist[a],)
    a = a + 2
    
mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
total = 0
for sublist in mylist:
    total += sum(sublist)
print(total) 

fruit = "banana"
letter = fruit[1]
print (letter)

mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
a=0
total = 0
while a < 3:
    b = 0
    while b < 2:
        print (total)
        total += mylist[a][b]
        b += 1
    a += 1
print(total)

n = 10
while n != 1:
    print(n,)
    if n % 2 == 0: # n is even
        n = n / 2
    else: # n is odd
        n = n * 3 + 1
        
def is_divisible(x, y):

    return (x % y) == 0

print(is_divisible(23, 2))


n = 10000
count = 0
while n:
    count = count + 1
    n = n / 10
    n=int(n)
print(count)

word = 'bAnana'

index = word.find('a')
print(index)

pi = float(3.14159)
print (pi)

x=1
y=2
if x == y:
    print (x, "and", y, "are equal")
else:
    if x < y:
        print (x, "is less than", y)
    else:
        print (x, "is greater than", y)
        
x = 5
if x % 2 == 0:
    print (x)
else:
    print (x, x%2)
    
    
def function2(param):
    print (param, param)
def function1(part1, part2):
    cat = part1 + part2
    function2(cat)
chant1 = "See You"
chant2 = "See Me"
function1(chant1, chant2)


percentage = float ( 60 * 100) / 55
print (percentage)


if "Ni!":
    print ('We are the Knights who say, "Ni!"')
else:
    print ("Stop it! No more of this!")
    
    
print(isinstance(10.001, float))



a = 
b = 
a is b