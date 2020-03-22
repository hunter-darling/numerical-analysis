# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
2020-03-18 @author: Hunter Darling

MTH 452 Homework 6 - Euler's Method Questions

Use Euler's method to approximate the solutions for the IVP """

### Exercise 5.2.1 (b) ###

#y' = 1 + (t-y)^2
#2 <= t <= 3
#y(2) = 1
#h = 0.5

def func1(t, y): 
    return (1 + (t-y)**2)

t01 = 2
y01 = 1
h1 = 0.5
tf1 = 3

temp1 = -0
    
while t01 < tf1: 
    temp1 = y01 
    y01 = y01 + h1 * func1(t01, y01) 
    t01 = t01 + h1 
 
print("Approximate solution at t = ", t01, " is ", "%.3f"% y01)

#### Approximate solution at t =  3.0  is  2.625 ####

### Exercise 5.2.2 (d) ###

#y' = \frac{1}{t^2}(sin(2t)-2ty)
#1 \leq t \leq 2
#y(1) = 2
#h = 0.25

import math
def func2(t, y): 
    return ((1/(t**2))*(math.sin(2*t)-(2*t*y)))

t02 = 1
y02 = 2
h2 = 0.25
tf2 = 2

temp2 = -0
    
while t02 < tf2: 
    temp2 = y02 
    y02 = y02 + h2 * func2(t02, y02) 
    t02 = t02 + h2
 
print("Approximate solution at t = ", t02, " is ", "%.3f"% y02)

#### Approximate solution at t =  2.0  is  0.379 ####
