#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:23:58 2024

@author: jashanjotbrar
"""

#Lets construct a program using nested conditional statements
#This time we will tell your eligibility for the program
print('Choose your course') #prompt to choose the course
print('1 = biology, 2 = math, 3= computer science') #pick a course
sub1 = '1'  #variable for string 1
sub2 = '2'  #variable for string 2
sub3 = '3'  #variable for string 3
course = input()  #variable to input the string from the user

print('Enter your scores in percentage') #prompt to enter scores
score1 = int(input()) #variable to input the scores and store in the form of int

if(course == sub3): #condition, if course chosen is computer science
    print('Great! You have versatile knowledge. But math and biology are required prerequisites.') 

elif(course == sub2 and score1>=60): #conditon, if course is math and score >= 60
    print('Its great you passed math. Biology is a mandatory prerequisite for this program.') #prompt
elif(course == sub2 and score1<60): #conditon, if course is not biology and if it is math
    print('You need to pass math as it is a prerequisite for this program.') #prompt
    
elif(course==sub1 and score1<60):#condition, if course is biology and score is less than 60
    print('We need you to retake this course to enter in the program.') #prompt   
elif(course == sub1 and score1>=60 and score1<75): #condition, if course=biology and score>=60 and<75
    print('You are suggested to take a university challenge exam.') #prompt
elif(course == sub1 and score1>=75 and score1<90): #condition, if course=biology and score>=75 and<90
    print('Enter your email. We will send you a link for a short exam.') #prompt
elif(course == sub1 and score1>=90):  #condition, if course=biology and score >=90
    print('You are invited to the university for further interview') #prompt  
    reply1 = 'yes' #variable for string 'yes'
    reply2 = 'no'  #variable for string 'no'
    print('Enter a reply as : yes or no') #prompt to ask for a reply
    rep = input()  #variable for the input string
    if(rep==reply1): #condition, if reply is yes 
        print('Thanks! Check your email shortly and reply at your earliest convenience.') #prompt
    else: #if the reply entered by user is no then below statement should be printed.
        print('We understand you are no longer interested in this program.') #prompt
        
else:  #if user entered something else than the prompt then below statement will be printed.
    print('You entered something wrong!') #prompt