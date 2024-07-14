#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:38:46 2024

@author: jashanjotbrar
"""


sente_print = 'She sells sea shells at sea shore' # a variable holds the string value
print ('The sentence is:\n', sente_print)  # print the variable
split_sente = sente_print.split()  #the string will be split into letter using split method
print ('\nThe split sentence is:\n', split_sente) #print the split sentence

def rev_sente(x):  # function is defined with parameter x
    new_sente = []  # a new variable new_sente contains the empty list
    y = len(x)-1  # a variable y holds the length of the list -1
    while(y > -1): # while the length of the loop is greater than -1
        new_sente.append(x[y]) #the empty list is appended with the last element of the parameter list
        y = y-1    # the length of the loop decreases by 1 evrytime through the loop
    return new_sente  # return the updated list

print('The reverse of split sentence is:\n',rev_sente(split_sente)) 
# the function is called and the split_sente list is passed as argument
# the return value of the function is then printed


