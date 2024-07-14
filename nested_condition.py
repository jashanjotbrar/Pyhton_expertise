#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:13:55 2024

@author: jashanjotbrar
"""

#Lets construct a program using nested conditional statements
#This time we will tell your eligibility for the program
print('Choose your course') #prompt to choose the course
print('1 = biology, 2 = math, 3= computer science') #pick a course

sub1 = '1'  #variable for string course 1
sub2 = '2'  #variable for string course 2
sub3 = '3'  #variable for string course 3

course = input()  #variable to input the string from the user

if (course == sub1): #'if'condition to know if the chosen course by user is biology
    print('Enter your scores in percentage') #prompt to enter scores if the chosen course is 1
    score1 = int(input()) #variable to input the scores and store in the form of int
    if(score1 >= 90): #condition, if score is greater than or equal to 90
        print('You are invited to the university for further interview') #prompt for true condition
        reply1 = 'yes' #variable for string 'yes'
        reply2 = 'no'  #variable for string 'no'
        print('Enter a reply as : yes or no') #prompt to ask for a reply
        rep = input()  #variable for the input string
        if(rep==reply1): #condition, if reply is yes 
            print('Thanks! Check your email shortly and reply at your earliest convenience.') #prompt
        else: #if the reply entered by user is no then below statement should be printed.
            print('We understand you are no longer interested in this program.') #prompt
    elif(score1>=75): #condition, if score is greater than or equal to 75
        print('Enter your email. We will send you a link for a short exam.') #prompt
    elif (score1>=60): #condition, if score is greater than or equal to 60
        print('you are suggested to take a university challenge exam.') #prompt
    else: #condition, if scores entered have not met any of the conditions, then below prompt is print
        print('We need you to retake this course to enter in the program.') #prompt
        
elif(course == sub2): #conditon, if course is not biology and if it is math
    print('Enter your scores in percentage') #prompt to enter scores
    score1 = int(input()) #variable to input the scores and store in the form of int
    if(score1 >= 60): #condition, if score is greater than or equal to 90
        print('Its great you passed math. Biology is a mandatory prerequisite for this program.') #prompt
    else:
        print('You need to pass math as it is a prerequisite for this program.') #prompt
        
else: #condition, if course chosen is neither biology nor math
    print('Great! You have versatile knowledge. But math and biology are required prerequisites.')
    
    