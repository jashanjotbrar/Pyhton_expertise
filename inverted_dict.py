#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:42:32 2024

@author: jashanjotbrar
"""

def print_dict(d1): # a function to print the dictionary items in an order
    for keys, values in d1.items():  # for each key and value in the dictionary
        print(keys, values) #print the keys and the values

dict_ionary = {'Stud1': ['CS1101','CS2402','CS2001'], 
               'Stud2': ['CS2402','CS2001','CS1102'], 
               'Stud3': ['CS1101','CS2002','CS2402'],
               'Stud4': ['CS2401','CS2001','CS1101'],
               'Stud5': ['CS2401','CS2002','CS1101'] }  # dictionary of students and courses

print('The original dictionary is:') #prompt
print_dict(dict_ionary) #function is called to print the dictionary


def invert_dict(d):  # function is defined to invert the dictionary with the parameter d
    inverse_dict = {}  # an empty dictionary is created
    for keys, values in d.items():  # for each key and value in th dictionary
        for val in values:   # for each value in values
            if val not in inverse_dict:  # if the value is not in the inverse_dict
                inverse_dict[val] = [keys]  # make the key of the dictionary a value of the inverse_dict
            else:    #else
                inverse_dict[val].append(keys)  # otherwise add a key to the inverse dictionary
    return inverse_dict  #return the inverse_dict to the function


new_dict = invert_dict(dict_ionary)  # variable new_dict contains the return value of the function called
print('\nThe inverted dictionary')  #prompt
print_dict(new_dict)  # function is called to print the inverted dictionaery