#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:48:10 2020

@author: suman
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x): #given curve
    return np.sqrt(1-x*x)

n = 10000
z=np.linspace(0,1,100) #100 points between 0 and 1
x = np.random.rand(n) #n random numbers between 0 and 1
y = np.random.rand(n) #n random numbers between 0 and 1

plt.scatter(x,y,s=1,c='r',label='random points') #plotting the points
plt.plot(z,f(z),linewidth=4,label='circle of radius 1') #plotting the circle in first quadrant

plt.xlim(0,1) #range of x axis
plt.ylim(0,1) #range of y axis
plt.title('x vs y') #title of the graph
plt.xlabel('x', fontsize=13) #label of x axis
plt.ylabel('y', fontsize=13) #label of y axis
plt.legend(fontsize=7,loc='upper right')
plt.show()

k = 0
for i in range(n):
    if y[i] < f(x[i]):
        k += 1 #counting the no of points inside the curve
a=k/n #area of a part of that circle which is in first quadrant 
print('Area of the circle =',4*a) #Total area of the circle will be 4 times of a

#volume of 10 dimensional unit sphere
def g(x):
    return sum(x**2)

n = 1000000
x=np.zeros((10,n))
for i in range(10):
    x[i]=np.random.rand(n) #n random numbers between 0 and 1
k=0
for i in range(n):
    if g(x[:,i])<=1:
        k+=1 #counting the no of points inside the sphere
a=(2**10)*k/n #volume of 10 D unit sphere
print('Volume of 10D unit sphere=',a) #printing the result
