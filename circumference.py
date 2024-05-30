#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:20:07 2024

@author: jashanjotbrar
"""

#Calculate the Circumference of circle

#Let us define the function print_circum and assign a parameter named rad
def print_circum(rad):
    pi = 3.14159   # Value of pi rounded to five values
    circum = 2 * pi * rad  #Formula for the circumference of the circle
    print ('The circumference of circle is:', circum) #print the circumference of the circle
    
#Let us pass the argument as a value.    
print_circum(5)  #rvalue of the radius is 5

#Let us pass the argument in the form of a variable.
r = 10
print_circum(r) #radius is given as r and the value is 10.

#Let us pass the argument in the form of a value again.
print_circum(15) #value of the radius is 15
