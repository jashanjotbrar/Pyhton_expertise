#!/usr/bin/env python3
# -*- coding: utf-28 -*-
"""
Created on Thu May  2 16:34:37 2024

@author: jashanjotbrar
"""


#Let us calculate the exponential of a number
#We need a base and an exponent

def expon(x, n):    # define a function with an input of two parameters x for base and n for power
    print('The value of the parameters:', x, n)
    if n == 0:     # if the power of a base is zero, the output is 1
        return 1   # return 1
    else:          # else perform the exponential of a base
        out_put = x**n  # The computation of the exponential.
        rec = expon(x, n-1) # Recurse the expon function by decrement of 1 until the power becomes 0.
        #print('The calculated output in the function is', out_put)#print the output of the calculation.
        return out_put  # return the computed output
    
base = 2 # variable to take an input for base
power = -2  # variable to take an input for power
print('The arguments we will pass are:', base, power)       # print the value of the base and power 
result = expon(base, power) # Let us call the function and store the output in the variable - result
print(result)               #print the resulth

#precondition: the number entered for the base and power should not be a string
#postcondition: calculate the exponential and return the float value.

