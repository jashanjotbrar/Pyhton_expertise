#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:12:04 2024

@author: jashanjotbrar
"""

def velocity(distance, time_taken):    
    vel = (distance/time_taken)       
    print(vel, 'meter/second')     
    
#input using the value
velocity(200000, 8400) #distance covered of 200Km =200000m in 140 minutes = 8400seconds

#input using the variable
dist = 81*1000  # 1 Km has 1000 m, Distance of 81 Km
time = 70*60    # 1 minute  =60 seconds, Time is 70 minutes
velocity(dist, time) #distance is in meters and the time is in seconds

#input using the expression
velocity((1091*1000),((11*3600) +(27*60))) #distance of 1091Km in 11hours and 27 minutes
                            
#use the calculated velocity to further calculate the acceleration
acceleration  = vel/time_taken  #Formula for acceleration = velocity/time_taken
print(acceleration, 'meter/second square')