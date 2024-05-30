#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 01:03:35 2024

@author: jashanjotbrar
"""

def head_foot(x):  # function name head_foot is defined with a parameter x
    print(x)       #head_foot function basically performs the task of printing.
    
head_foot('Online Store') #To print a header we passed an argument named 'Online Store'
head_foot('-' * 30)       #To print a separating line, we used hyphen mark 30 times.

def catalog(name, value): #function named catalog is defined with parameters name and value
    print(name, ' '*(50 - len(name)), value) #print the both parameters with equal spacing.
    
catalog('Products(s)', 'Price')  #function is called to print Product(s) and Price
catalog('Item1', float(200))    #function is called to print Item1 with a price of 200
catalog('Item2', float(400))    #function is called to print Item2 with a price of 400
catalog('Item3', float(600))    #function is called to print Item3 with a price of 600
catalog('Combo 1 (Item 1 + 2)', float(540))   #function is called to print Combo 1 and its price
catalog('Combo 2 (Item 2 + 3)', float(900))   #function is called to print Combo 2 and its price
catalog('Combo 3 (Item 1 + 3)', float(720))   #function is called to print Combo 3 and its price
catalog('Combo 4 (Item 1 + 2 + 3)', float(900))  #function is called to print Combo 4 and its price
        

head_foot('_'*30)     #To print a separating line, call the head_foot function again
head_foot('For Delivery contact: 98764678899')  #Call the head_foot function to print the contact
                                                #in the footer

