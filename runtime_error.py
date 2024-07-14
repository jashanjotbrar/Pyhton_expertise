#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:45:23 2024

@author: jashanjotbrar
"""

print('Enter two numbers') #prompt for user to ask for two numbers
x = float(input())  #Variable to enter the first number
y = float(input())  #Variable to enter the second number

if (y==0): #condition, if divisor is zero
    print('You are trying to divide a number by zero which is not allowed.') #prompt
    print('Following error message will appear in python') #prompt
    print('Runtime error: ZeroDivisionError: division by zero') #prompt for error
else:  #condition, if divisor is a non-zero number
    z = (x/y) #variable for the result of the division 
    print(z) #print the result
    
    