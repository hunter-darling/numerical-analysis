#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 2020

@author: hunterdarling
"""

# MTH452 - Homework 9

# Approximate the solution to the following partial differential equation using
#  the Crank-Nicolson Algorithm.

# Exercise 12.2.4

import math
import numpy.linalg as ge
import numpy as np

alpha  = .25
a = 0
b = 1
m = 3
T = 0.1
N = 2
h = (b-a)/m
k = T/N
lam = ((alpha**2)*k)/(h**2)

def f(x):
    return 2 * math.sin(2 * math.pi * x)

def factual(x,t):
    return 2*math.exp((-(math.pi**2)*t)/4)*math.sin(2*math.pi*x)

x_lst = []
for i in range(1,m):
    x_lst.append(i*h)

t_lst = []
for j in range(1,N+1):
    t_lst.append(j*k)
    
w_dict = new_dict = {new_list: [] for new_list in range(m+1)}
for i in range(1,m):
    w_dict[i].append(f(x_lst[i-1]))
for i in range(1,N+1):
    w_dict[0].append(0)
    w_dict[3].append(0)    

# print(x_lst)
# print()
# print(t_lst)
# print()
# print(w_dict)
# print()

A1 = [[0 for i in range(1,m)] for i in range(1,m)]
B1 = [[0 for i in range(1,m)] for i in range(1,m)]
for i in range(0,m-1):
    for j in range(0,m-1):
        if i==j:
            A1[i][j] = 1 + lam
            B1[i][j] = 1 - lam
        elif (j==i+1 and i<=1) or (j==i-1 and i>=1 and i<=2):
            A1[i][j] = -lam/2
            B1[i][j] = lam/2
        else:
            A1[i][j] = 0
            B1[i][j] = 0
A = np.array(A1)
B = np.array(B1)
# print(A)
# print(B)

w0 = np.array([w_dict[i] for i in range(1,m)])
# print(w0)

b_v = np.matmul(B,w0)

w1 = ge.solve(A,b_v)
# print(w1)

w2 = ge.solve(A,w1)
# print(w2)

actuals = {}
for j in range(0,N):
    actuals[j+1] = [factual(x_lst[i],t_lst[j]) for i in range(0,m-1)]
    
#print(actuals)
    
errors = {}
for j in range(1,N+1):
    if j == 1:
        w_lst = w1
    else:
        w_lst = w2
    errors[j] = [abs(actuals[j][i]-w_lst[i]) for i in range(0,m-1)]

for j in range(1,m):
    if j == 1:
        w_lst = w1
    else:
        w_lst = w2
    for i in range(1,m):
        print(" i: ", i, " j: ", j, " x: ", x_lst[i-1], 
              " t: ", t_lst[j-1], " w: ", w_lst[i-1], 
              " u: ", actuals[j][i-1],
              " err: ", errors[j][i-1])