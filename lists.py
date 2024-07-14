#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:31:23 2024

@author: jashanjotbrar
"""

#Let us check if the two objects are identical or equivalent
x = ['fine', 'Thank you', 'It was great', 12] #Object x is defined to which value is assigned
y = ['fine', 'Thank you', 'It was great', 12] #Object y is defined to which value is assigned
print('x is y : ', x is y)  # Use the is operator to check if both objects refers to the same value
# a new object z is defined
z = x #Object z is assigned the object x, so both have the same reference
print('x is z : ', x is z)  # Use the is operator to check if both objects refers to the same value


year1= [2020, 2021, 2022, 2023, 2024]
year2= year1
print ('\nyear1 are:', year1)
print ('year2 are:', year2)
print ('year2 is year1:', year2 is year1)

year2[0] = (2020 - 5)
print ('\nyear1 are:', year1)
print ('year2 are:', year2)
print ('year2 is year1:', year2 is year1)

year2 = [1990, 1991, 1992, 1993, 1994]
print ('\nyear1 are:', year1)
print ('year2 are:', year2)
print ('year2 is year1:', year2 is year1)


