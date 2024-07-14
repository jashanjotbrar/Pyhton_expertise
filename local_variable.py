#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:08:00 2024

@author: jashanjotbrar
"""

# Let us calculate the work done.
# The formula for the work is force * distance
def work (force, distance):  #force and distance are the parameters to calculate work
    work_calc = force*distance  #Force is given in newton and distance is given in meters.
    print (work_calc, 'Joules of work is done.')
    
work(50, 17)

#Let us caculate the power
#Formula for power is Work/Time taken
work_calc = 513 #Joules
Time =20 * 60   # 20 minutes = 20*60 seconds
Power = work_calc/Time
print('Power is ', Power, 'Joule/second')