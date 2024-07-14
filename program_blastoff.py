#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:26:31 2024

@author: jashanjotbrar
"""

print('Enter an integer it could be negative, positive or zero') #prompt to enter an integer
num = int(input()) #variable num to input an integer


def countdown(n):  #define a function named countdown with a parameter n
     if n == 0:   #condition, if n is equal to zero
          print('Blastoff!')  #prompt
     else:     #condition, if n is not equal to zero
          print(n)   #prompt
          countdown(n-1)  #call the function with a decrement in the value

def countup(n):  #define a function named countup with a decrement in the value of parameter n
     if n == 0:  #condition, if n is equal to zero
          print('Blastoff!')  #prompt
     else:      #condition if n is not equal to zero
          print(n)  #prompt
          countup(n+1)  #call the function countup with an increment in the value of parameter n


if (num>0):  #condition, if value entered is greater than 0
    countdown(num-1)  #call the function countdown with a decrement in the value of the argument
elif(num<0):  #condition, if value entered is less than 0
    countup(num+1)  #call the function countdown with an increment in the value of the argument
else:         #condition, if the number entered is zero
    print('blastoff!') #prompt

