#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:31:23 2024

@author: jashanjotbrar
"""

#We will make a program to make a table of any number

#Define a function
def make_table(x,n): #function is defined with parameters x and n 
    num1 = 1    # a variable num1 is defined and set to value 1
    for nums in range(len(x)):  #for each number in the range of the length of the list
        num1 = x[nums] * n  #num1 updates by multiplying each number of the list to the n
        print (num1)   #print num1

print('Please enter a number to see the table') #prompt to enter the number
num = int(input())  #variable num stores the input of the user as an integer
list_table = [2,3,4,5,6,7,8,9,10]  # object list_table holds the e
make_table(list_table, num)   #function call



numb = [1, 2, 3] # a new object is made with a list

numb[1] = numb[1] * 2  # an operation is made on object numb

numb1 = numb    # object numb1 refers to the same list as object numb

numb1[1] = -1   # one of the element of the object numb1 is updated to -1

positive = numb  # numb has only positive integers so refers to  a new object positive
negative = numb1  # numb1 may have negative numbers so refers to a new object negative
print('Positive number list: ', positive, 'negative number list:', negative) #print both objects



