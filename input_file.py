#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:21:07 2024

@author: jashanjotbrar
"""

in_file = '/Users/Jashanjotbrar/Downloads/Vegan_dictionary.txt'
out_file = '/Users/Jashanjotbrar/Downloads/Vegan_dictionary_output.txt'

with open(in_file, 'r') as fin: # dictionary from the file
    lines = fin.readlines() # read the lines from the file

dict_ionary = {}  # create an empty dictionary

for line in lines:  # for line in  lines of the file
    keys,value = line.strip().split(':') # split the keys and values from the text file
    dict_ionary[keys.strip()] = value.strip() # dictionary stores the values of keys and values
    
print('The original dictionary from text file:\n', dict_ionary) #print the original dictionary

def print_dict(d1): # a function to print the dictionary items in an order
    for keys, values in d1.items():  # for each key and value in the dictionary
        print(keys, values) #print the keys and the values

print('\nThe original dictionary is:') #prompt
print_dict(dict_ionary) #function is called to print the dictionary


def invert_dict(d):  # function is defined to invert the dictionary with the parameter d
    inverse_dict = dict()  # an empty dictionary is created
    for key in d:  #for key in dictionary
        val = d[key]  #values are stored in the variable val
        if val not in inverse_dict:  # if the value is not in the inverse dictionary
            inverse_dict[val] = [key]  #make the keys the value
        else:
            inverse_dict[val].append(key)  #otherwise add the key to the list
    return inverse_dict  #return the inverse_dict to the function


new_dict = invert_dict(dict_ionary)  # variable new_dict contains the return value of the function called
print('\nThe inverted dictionary')  #prompt
print_dict(new_dict)  # function is called to print the inverted dictionaery

#Write the inverted dictionary to the output file
with open(out_file, 'w') as fout:
    for key, value in new_dict.items():
        fout.write(f'{key}:{value}\n')
   
   
   