#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 2020

@author: hunterdarling
"""

# MTH452 - Homework 9

# Use Algorithm 12.1 to approximate the solutions to the elliptic partial differential equation. 
#  Compare to actual solution.

import numpy.linalg as ge
import numpy as np

# Exercise 12.1.1
#  d2u/dx2 + d2u/dy2 = 4, 0 < x < 1, 0 < y < 2
#  u(x,0) = x^2, u(x,2) = (x-2)^2, 0 <= x <= 1
#  u(0,y) = y^2, u(1,y) = (y-1)^2, 0 <= y <= 2
#  Use h = k = 1/2
#  Actual solution: u(x,y) = (x-y)^2

x10 = 0.0
x1_lst = []
y10 = 0.0
y1_lst = []

# Lists for mesh points:
for i in range(0,1):
    x10 = x10 + .5
    x1_lst.append(x10)

for i in range(0,3):
    y10 = y10 + .5
    y1_lst.append(y10)
    
#print(x1_lst, y1_lst)

# Centered diff:
#  d2u/dx2 = 4[u(x_i+1,y_j)-2u(x_i,y_j)+u(x_i-1,y_j)]
#  d2u/dy2 = 4[u(x_i,y_j+1)-2u(x_i,y_j)+u(x_i,y_j-1)]

# Boundary cond:
#  w_(0,j) = u(x_0,y_j) = (y_j)^2, w_(1,j) = u(x_n,y_j) = (y_j-1)^2, for each j = 1,2,3
#  w_(i,0) = u(x_i,y_0) = (x_i)^2, w_(i,2) = u(x_i,y_n) = (x_i-2)^2, for each i = 1

# Finite diff method:
#  4w_(i,j) - (w_(i+1,j) + w_(i-1,j)) - (w_(i,j+1) + w_(i,j-1)) = -1


A1 = [[4, -1, 0],[-1, 4, -1],[0, -1, 4]]
b1 = [-1/4, 0, 15/4]

w1 = ge.solve(A1,b1)

print("Approximate Solutions: ", w1)

actual1 = [(x1_lst[0]-y1_lst[i])**2 for i in range(0,3)]

print("Exact Solutions: ", actual1)

error1 = [(w1[i]-actual1[i]) for i in range(0,3)]

print("Error: ", error1)

print()

# Exercise 12.1.2
#  d2u/dx2 + d2u/dy2 = 0, 1 < x < 2, 0 < y < 1
#  u(x,0) = 2ln(x), u(x,1) = ln(x^2 + 1), 1 <= x <= 2
#  u(1,y) = ln(y^2 + 1), u(2,y) = ln(y^2 + 4), 0 <= y <= 1
#  Use h = k = 1/3
#  Actual solution: u(x,y) = ln(x^2 - y^2)

x20 = 1.0
x2_lst = []
y20 = 0.0
y2_lst = []

# Lists for mesh points:
for i in range(0,3):
    x20 = x20 + 1/3
    x2_lst.append(x20)

for i in range(0,3):
    y20 = y20 + 1/3
    y2_lst.append(y20)
    
#print(x2_lst, y2_lst)

# Centered diff:
#  d2u/dx2 = 9[u(x_i+1,y_j)-2u(x_i,y_j)+u(x_i-1,y_j)]
#  d2u/dy2 = 9[u(x_i,y_j+1)-2u(x_i,y_j)+u(x_i,y_j-1)]

# Boundary cond:
#  w_(0,j) = u(x_0,y_j) = ln(y_j^2 + 1), 
#   w_(3,j) = u(x_3,y_j) = ln(y_j-1^2 + 4), for each j = 1,2,3
#  w_(i,0) = u(x_i,y_0) = 2ln(x_i), 
#   w_(i,3) = u(x_i,y_3) = ln(x_i^2 + 1), for each i = 1,2

# Finite diff method:
#  4w_(i,j) - (w_(i+1,j) + w_(i-1,j)) - (w_(i,j+1) + w_(i,j-1)) = 0


A2 = [[4, -1, -1, 0],[-1, 4, 0, -1],[-1, 0, 4, -1],[0, -1, -1, 4]]
b2 = [np.log(160/81), np.log(325/81), np.log(925/81), np.log(1360/81)]

w2 = ge.solve(A2,b2)

print("Approximate Solutions: ", w2)

actual2 = []
for i in range(0,2):
    for j in range(0,2):
        actual2.append(np.log(x2_lst[i]**2 + y2_lst[j]**2))

print("Exact Solutions: ", actual2)

error2 = [(w2[i]-actual2[i]) for i in range(0,4)]

print("Error: ", error2)