#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:38:46 2024

@author: jashanjotbrar
"""


print('Please enter your name:') #prompt
name = input() #input for name from user

print('How many characters you want to print from left?') #prompt
l = len(name) #length of name
n = int(input()) #number of characters a user want to print from left
print('The', n ,'characters from left: ', name[(l-n):]) #print characters in name from left

def count_vow(s): #function is defined to count vowels with a parameter s
    count = 0  #the variable count is set to zero at first
    for letter in s: #for each letter in the word
        if(letter == 'a'): # if the letter in the loop is 'a' (condition)
            count = count+1 #make an increment in the count by 1
        elif(letter == 'e'):# otherwise if the letter in the loop is 'e' (condition)
             count = count+1 #make an increment in the count by 1
        elif(letter == 'i'): # otherwise if the letter in the loop is 'i' (condition)
             count = count+1 #make an increment in the count by 1
        elif(letter == 'o'): # otherwise if the letter in the loop is 'o' (condition)
             count = count+1 #make an increment in the count by 1
        elif(letter == 'u'): # otherwise if the letter in the loop is 'u' (condition)
             count = count+1 #make an increment in the count by 1
        else:  # if none of the above conditons match
            count = count + 0 # the count shall remain same
    return count  #return the total count value to the function

vow_num = count_vow(name) #a variable is set to store the value of the count
print('There are', vow_num, 'vowels in', name) #prompt


def rev_name_for (s): # define a function to reverse the name using for loop
    new_s = ''  #set a new_s variable to an empty string
    for letters in s: #for each letter in word
        new_s = letters +new_s   #add this letter to the empty string and loop it over
    return new_s   #return the new string formed to the function

def rev_name_while (s):  # define a function to reverse the name using while loop
    new_s = ''   #set a new_s variable to an empty string
    j = 0   #set a variable j to 0
    while (j<len(s)): #while the j is less than the length of the word
        new_s = s[j] +new_s # add the jth character to the new_s string and loop it over
        j = j+1   # make an increment to the j so that loop can iterate over all the characters
    return new_s   #return the new string formed to the function

print('The name', is reversed using for loop: ', rev_name_for(name)) #call the function and print
print('The',name,'is reversed using while loop: ', rev_name_while(name)) #call the function and print

