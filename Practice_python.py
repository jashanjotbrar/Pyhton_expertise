# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=42
print(n)

42==n
print(n)

x=y=1
print(x,y)

print('The time runs fast so we need to calculate it which can be done as;');



#Let us calculate the volume of a sphere.
radius = 5
pi = 3.141
Volume = (4/3)*pi*(radius**3)
print(Volume)

#Let us caluclate the price of the 60 books
Cover_price = 24.95
wholesale_price = (24.95)-(24.95)*0.4  #After 40% discount
Ship_price1 = 3
Ship_price2 = 0.75
Totol_cost = (wholesale_price*60) + (Ship_price1+Ship_price2*59)
print('The total wholesale cost of 60 books is' , Totol_cost)

#Let us calculate the time to get back home
run1 = 8.15*1  #minutes
run2 =  7.12*3  #minutes
Total_time  = (run1 +run2 + run1) #minutes
print('Total time',Total_time, 'minutes')
Total_time  = (run1 +run2 + run1)/60 #hours
print('Total time',Total_time, 'hours')
time_in_hours = Total_time + (6+ (52/60)) #hours
hours = round(time_in_hours)             # hours
minutes = round((time_in_hours - hours)*60) #minutes
print(minutes)
print('I finish my run at', hours, minutes, 'am')



def right_justify(word):
    space = ' '
    give_space = space * 69
    more_space = give_space + word
    print(len(more_space))
    print(more_space)

right_justify('s')

    

def do_twice(x , y):
    print(x)
    print(y)
  
def print_spam():
    print('spam' , 'bram')
    
def print_twice(bruce):
    print(bruce)
    print(bruce)
    
do_twice(print_twice('spam'),'l')
    
percentage= (60.0*100.0)/55.0
print(percentage)
    
    
# Let us create a function to calculate the velocity.

def velocity(distance, time_taken):    
    vel = (distance/time_taken)       
    print(vel)     

dist = 81*1000
time = 70*60
velocity(dist, time) #distance is in meters and the time is in seconds
                                    


















