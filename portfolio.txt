#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:00:33 2024

@author: jashanjotbrar
"""

#Choose the groceries and print the reciept

print('Welcome to Malhi Grocery store.') #prompt
print('You will get the lowest price today.') #prompt

def food(z): #define a function for food values with input parameter z
    value1 = 5      #value is set for first item in the food list
    value2 = 3.7    #value is set for second item in the food list
    value3 = 4.5    #value is set for third item in the food list
    value4 = 3      #value is set for fourth item in the food list
    value5 = 7      #value is set for fifth item in the food list
    value6 = 5.6    #value is set for sixth item in the food list
    value7 = 6.7    #value is set for seventh item in the food list
    value8 = 5      #value is set for eighth item in the food list
    value9 = 4.5    #value is set for nineth item in the food list
    value10 = 6.5   #value is set for tenth item in the food list
    value11 = 3.5   #value is set for eleventh item in the food list
    value12 = 4     #value is set for twelveth item in the food list
    value13 = 5     #value is set for thirteenth item in the food list
    value14 = 0     #value is set to zero if a user enter something wrong
    if(z == 'x1'):  # if the string input entered by the user is 'x1'
        print('2 packs of bread', ' '*(50 - len('2 packs of bread')), value1) #prompt
        return value1 #return the price of this item
    elif(z == 'x2'):  # if the string input entered by the user is 'x2'
        print('peanut butter', ' '*(50 - len('peanut butter')), value2) #prompt
        return value2 #return the price of this item
    elif(z=='x3'):   # if the string input entered by the user is 'x3'
        print('Cereal', ' '*(50 - len('Cereal')), value3) #prompt
        return value3 #return the price of this item
    elif(z=='x4'):   # if the string input entered by the user is 'x4'
        print('Pasta', ' '*(50 - len('Pasta')), value4) #prompt
        return value4 #return the price of this item
    elif(z=='x5'):   # if the string input entered by the user is 'x5'
        print('Rice', ' '*(50 - len('Rice')), value5) #prompt
        return value5 #return the price of this item
    elif(z=='x6'):   # if the string input entered by the user is 'x6'
        print('Lettuce', ' '*(50 - len('Lettuce')), value6) #prompt
        return value6 #return the price of this item
    elif(z=='x7'):   # if the string input entered by the user is 'x7'
        print('Butter', ' '*(50 - len('Butter')), value7) #prompt
        return value7 #return the price of this item
    elif(z=='x8'):   # if the string input entered by the user is 'x8'
        print('Beans', ' '*(50 - len('Butter')), value8) #prompt
        return value8 #return the price of this item
    elif(z== 'x9'):  # if the string input entered by the user is 'x9'
        print('Onion', ' '*(50 - len('Onion')), value9) #prompt
        return value9 #return the price of this item
    elif(z=='x10'):   # if the string input entered by the user is 'x10'
        print('Avocadoes', ' '*(50 - len('Avocadoes')), value10) #prompt
        return value10 #return the price of this item
    elif(z=='x11'):    # if the string input entered by the user is 'x11'
        print('Salt', ' '*(50 - len('Salt')), value11) #prompt
        return value11 #return the price of this item
    elif(z=='x12'):   # if the string input entered by the user is 'x12'
        print('Pepper', ' '*(50 - len('Pepper')), value12) #prompt
        return value12 #return the price of this item
    elif(z=='x13'):   # if the string input entered by the user is 'x13'
        print('Cheese', ' '*(50 - len('Cheese')), value13) #prompt
        return value13 #return the price of this item
    else:
        print('You entered something wrong', ' '*(50 - len('You entered something wrong')), value14) #prompt
        return 0  #return zero when a user entered the wrong input 

def food_value():  #define a function to calculate the total price of the 
    print('Choose 5 items from food:') #prompt
    print(' x1 2 packs of Bread\n x2 Peanut Butter\n x3 Cereal\n x4 Pasta\n x5 Rice\n x6 Lettuce') #prompt
    print(' x7 Butter\n x8 Beans\n x9 Onions\n x10 Avocadoes\n x11 Salt\n x12 Pepper\n x13 Cheese\n') #prompt
    print('Food Items', ' '*(50 - len('Food Items')), 'Price') #prompt
    food1 = food(input()) #input by the user
    food2 = food(input()) #input by the user
    food3 = food(input()) #input by the user
    food4 = food(input()) #input by the user
    food5 = food(input()) #input by the user
    Food_value = food1+food2+food3+food4+food5 #sum of all the prices of food
    print('-'*(60))
    print('Total of food', ' '*(50 - len('Total of food')) , Food_value) #prompt
    print('-'*(60))
    return Food_value #return the price of this item

def beverage(z): #define a function for beverage values with input parameter z
    value1 = 12   #value is set for first item in the food list 
    value2 = 3.5   #value is set for second item in the food list 
    value3 = 4   #value is set for third item in the food list 
    value4 = 7.5    #value is set for fourth item in the food list 
    value5 = 6.7   #value is set for fifth item in the food list 
    value6 = 4.3   #value is set for sixth item in the food list 
    value7 = 4.3   #value is set for seventh item in the food list 
    value8 = 2   #value is set for eighth item in the food list 
    value9 = 2   #value is set for nineth item in the food list 
    value10 = 2.5   #value is set for tenth item in the food list 
    value11 = 0   #value is set for eleventh item in the food list 
    if(z == 'x1'): # if the string input entered by the user is 'x1'
        print('2 cartons of milk', ' '*(50 - len('2 cartons of milk')), value1) #prompt
        return value1 #return the price of this item
    elif(z == 'x2'): # if the string input entered by the user is 'x2'
        print('Apple juice', ' '*(50 - len('Apple juice')), value2) #prompt
        return value2 #return the price of this item
    elif(z=='x3'): # if the string input entered by the user is 'x3'
        print('Orange Juice', ' '*(50 - len('Orange Juice')), value3) #prompt
        return value3 #return the price of this item
    elif(z=='x4'): # if the string input entered by the user is 'x4'
        print('Whipping cream', ' '*(50 - len('Whipping cream')), value4) #prompt
        return value4 #return the price of this item
    elif(z=='x5'): # if the string input entered by the user is 'x5'
        print('Half n Half', ' '*(50 - len('Half n Half')), value5) #prompt
        return value5 #return the price of this item
    elif(z=='x6'): # if the string input entered by the user is 'x6'
        print('Coconut milk', ' '*(50 - len('coconut milk')), value6) #prompt
        return value6 #return the price of this item
    elif(z=='x7'): # if the string input entered by the user is 'x7'
        print('Soy milk', ' '*(50 - len('Soy milk')), value7) #prompt
        return value7 #return the price of this item
    elif(z=='x8'): # if the string input entered by the user is 'x8'
        print('Sprite', ' '*(50 - len('Sprite')), value8) #prompt
        return value8 #return the price of this item
    elif(z== 'x9'): # if the string input entered by the user is 'x9'
        print('Coke', ' '*(50 - len('Coke')), value9) #prompt
        return value9 #return the price of this item
    elif(z=='x10'): # if the string input entered by the user is 'x10'
        print('Dr. Pepper', ' '*(50 - len('Dr. Pepper')), value10) #prompt
        return value10 #return the price of this item
    else:  #otherwise print and return zero
        print('You entered something wrong', ' '*(50 - len('You entered something wrong')), value11) #prompt
        return 0 #return zero when a user entered the wrong input 

def beverages_value(): #define a function to calculate the sum of the prices of the beverages
    print('\nChoose 3 items from beverages:') #prompt
    print(' x1 2 cartons of milk\n x2 Apple juice\n x3 Orange Juice\n x4 Whipping cream')  #prompt
    print(' x5 Half n Half\n x6 Coconut milk\n x7 Soy milk\n x8 Sprite\n x9 Coke\n x10 Dr. Pepper\n') #prompt
    print('Beverages', ' '*(50 - len('Beverages')), 'Price') #prompt
    beverage1 = beverage(input()) #input by the user
    beverage2 = beverage(input()) #input by the user
    beverage3 = beverage(input()) #input by the user
    Beverage_value = beverage1+beverage2+beverage3 #sum of all the prices of beverages
    print('-'*(60))
    print('Total of beverages', ' '*(50 - len('Total of beverages')) , Beverage_value) #prompt
    print('-'*(60))
    return Beverage_value #return the price of this item

def house_sup(z):  #define a function for household values with input parameter z
    value1 = 19   #value is set for first item in the food list 
    value2 = 9   #value is set for second item in the food list 
    value3 = 12    #value is set for third item in the food list 
    value4 = 10   #value is set for fourth item in the food list 
    value5 = 7.5   #value is set for fifth item in the food list 
    value6 = 5   #value is set for sixth item in the food list 
    value7 = 6.7   #value is set for seventh item in the food list 
    value8 = 6.7   #value is set for eighth item in the food list 
    value9 = 4.5   #value is set for nineth item in the food list 
    value10 = 0   #value is set for tenth item in the food list 
    if(z == 'x1'): # if the string input entered by the user is 'x1'
        print('Laundary Detergent', ' '*(50 - len('Laundary Detergent')), value1) #prompt
        return value1 #return the price of this item
    elif(z == 'x2'): # if the string input entered by the user is 'x2'
        print('Dish Soap', ' '*(50 - len('Dish Soap')), value2) #prompt
        return value2 #return the price of this item
    elif(z=='x3'): # if the string input entered by the user is 'x3'
        print('Paper Towel', ' '*(50 - len('Paper Towel')), value3) #prompt
        return value3 #return the price of this item
    elif(z=='x4'): # if the string input entered by the user is 'x4'
        print('Toilet paper', ' '*(50 - len('Toilet paper')), value4) #prompt
        return value4 #return the price of this item
    elif(z=='x5'): # if the string input entered by the user is 'x5'
        print('Floor Cleaner', ' '*(50 - len('Floor Cleaner')), value5) #prompt
        return value5 #return the price of this item
    elif(z=='x6'): # if the string input entered by the user is 'x6'
        print('Body wash', ' '*(50 - len('Body wash')), value6) #prompt
        return value6 #return the price of this item
    elif(z=='x7'): # if the string input entered by the user is 'x7'
        print('Shampoo', ' '*(50 - len('Shampoo')), value7) #prompt
        return value7 #return the price of this item
    elif(z=='x8'): # if the string input entered by the user is 'x8'
        print('Conditioner', ' '*(50 - len('Conditioner')), value8) #prompt
        return value8 #return the price of this item
    elif(z== 'x9'): # if the string input entered by the user is 'x9'
        print('Garbage bags', ' '*(50 - len('Garbage bags')), value9) #prompt
        return value9 #return the price of this item
    else:
        print('You entered something wrong', ' '*(50 - len('You entered something wrong')), value10) #prompt
        return 0 #return zero when a user entered the wrong input 

def house_sup_value(): #define a function to calculate the sum of the prices of the household supplies
    print('\nChoose 4 items from household supplies:') #prompt
    print(' x1 Laundary Detergent\n x2 Dish Soap\n x3 Paper Towel\n x4 Toilet paper') #prompt
    print(' x5 Floor Cleaner\n x6 Body wash\n x7 Shampoo\n x8 Conditioner\n x9 Garbage Bags\n')  #prompt
    print('Household supplies', ' '*(50 - len('Household supplies')), 'Price') #prompt
    house_sup1 = house_sup(input()) #input by the user
    house_sup2 = house_sup(input()) #input by the user
    house_sup3 = house_sup(input()) #input by the user
    house_sup4 = house_sup(input()) #input by the user
    House_sup_value = house_sup1+house_sup2+house_sup3+house_sup4 #sum of all the prices of household
    print('-'*(60))
    print('Total of household supplies', ' '*(50 - len('Total of bhousehold supplies')), House_sup_value) #prompt
    print('-'*(60))
    return House_sup_value #return the price of this item

Total_value = food_value() + beverages_value() + house_sup_value()
print('\n Thank you! for shopping with us today. We promise you the best rates and quality everyday.\n') #prompt
print('*'*(60))
print('\n Total of your shopping comes to:  $', Total_value,'\n' ) #prompt
print('*'*(60))



