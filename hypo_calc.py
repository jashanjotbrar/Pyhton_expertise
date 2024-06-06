#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:28:46 2024

@author: jashanjotbrar
"""

print('Let us calculate the hypotenuse of a triangle') #prompt
print('Enter a number for the base and perpendicular') #prompt
base = float(input())  #input the float value for variable base
perp = float(input())  #input the float value for variable perpendicular

import math #import the mathe module

def calc_hypo(base1, perp1): #function is defined here
    print('The parameters in the function are: \n','base: ',base1, '\n perpendicular: ',perp1)#prompt
    bsquared = base1**2 #square of the base parameter
    print('The square of the base is: ',bsquared) #prompt
    psquared = perp1**2 #square of the perpendicular parameter
    print('The square of the perpendicular is: ',psquared) #prompt
    square_sum = bsquared + psquared  #sum of square of base and perpendicular parameters
    print('The sum of squares of the base and perpendicular is: ', square_sum) #prompt
    hypotenuse = math.sqrt(square_sum) #variable to calculate the square root of square_sum.
    print('The hypotenuse inside the function is:', hypotenuse) #prompt
    return hypotenuse #return the calculated result to the function

result = calc_hypo(base, perp) #function is called and returned value is stored in variable result
print('The calculated hypotenuse is:', result) #The variable result is printed.

