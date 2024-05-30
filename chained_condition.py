#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:18:59 2024

@author: jashanjotbrar
"""

#Chained conditionals
#Let us help you choose the right program of studies.
print('Hi! We are here to help you to choose a program') #prompt to welcome
print('Choose set of courses you have studied before:') #promp to choose the courses
print('Set1 = biology, chemistry and physics') #prompt for set1 of courses
print('Set2 = biology, chemistry and psychology') #prompt for set2 of courses
print('Set3 = physics, math and  chemistry') #prompt for set3 of courses
print('Set4 = physics, math and psychology') #prompt for set4 of courses
print('Set5 = math, computer science and  physics') #prompt for set5 of courses
print('Set6 = math, computer science and psychology') #prompt for set6 of courses

set1 = 'Set1' #variable for string 'Set1'
set2 = 'Set2' #variable for string 'Set2'
set3 = 'Set3' #variable for string 'Set3'
set4 = 'Set4' #variable for string 'Set4'
set5 = 'Set5' #variable for string 'Set5'
set6 = 'Set6' #variable for string 'Set6'

subjects = input() #variable to input the entered string

if (subjects==set1): #condition, if the entered string is equal to set1
    print('You are suggested to take a medical program.') #prompt
elif (subjects==set2): #condition, if the entered string is equal to set1
    print('You are suggested to take a medical program.') #prompt
elif (subjects==set3): #condition, if the entered string is equal to set1
     print('You are suggested to take an engineering program.') #prompt 
elif (subjects==set4): #condition, if the entered string is equal to set1
     print('You are suggested to take an engineering program.') #prompt
elif (subjects==set5): #condition, if the entered string is equal to set1
     print('You are smart! you can choose either engineering or computer science program.') #prompt
elif (subjects==set6): #condition, if the entered string is equal to set1
     print('You are suggested to take a program in the field of computer science.') #prompt
else: #if none of the above conditions match, then below statement should be printed
    print('You are versatile, just a need to check other prerequisites') #prompt


