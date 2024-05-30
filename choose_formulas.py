#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:04:19 2024

@author: jashanjotbrar
"""

names = ['Aman', 'Raman', 'Jashan', 'Gagan', 'Magan', 'Sivan', 'Taman', 'Saman', 'Rohan', 'Robin']
sublist1 = names[:5] #object names1 split the first five names
sublist2 = names[5:] #object names2 split the last five names
print(sublist1)
print(sublist2)

sublist2.append('Kriti Brown') #a new name is added to the sublist2 
print('sublist2 : ', sublist2)

del sublist1[1]  #delete the second name from the sublist1
print('sublist1 : ', sublist1)


sublist1.extend(sublist2) #merged the two lists 
print ('The merged sublists: \n', sublist1)

salaryList = [6000, 3200, 5000, 7000, 4000, 2500, 2000, 3500, 3000, 2500] #object has a salary list
print('\nThe salary of the employees:\n', salaryList)   #print the salary list

#function is defined to raise the salary
def raise_salary(x): # function gets the parameter
    new_salary = []  # new object new_salary with an empty list is created
    for salary in range(len(x)):  # for each salary in the salary list
        new_salary.append(x[salary]*(1+0.04)) #new_salary appends with a raise in salary
    return(new_salary) #new_salary list is returned to the function

new_salaryList = raise_salary(salaryList) #object is updated with a function call
print('\nThe rise in salary by 4%:\n',new_salaryList) #print the new_salaryList

new_salaryList.sort() #sort the new_salaryList
print('\nThe top three salaries are:', new_salaryList[7:]) #print the sorted list with top 3 salaries


