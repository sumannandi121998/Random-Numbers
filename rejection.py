#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:46:42 2020

@author: suman
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x): #given PDF function
    return np.sqrt(2/np.pi)*np.exp(-x*x/2)
def g(x): #envelop function
    return 1.5*np.exp(-x)

x=np.random.rand(100000) #100000 random numbers between 0 and 1
x=-np.log(x)
y=np.random.rand(100000)*g(x) #for each x , y is uniformly random between 0 and g(x)
z=np.linspace(0,10,100) #100 points between 0 and 10
x1=x[y<f(x)] #x co-ordinates of the points under the gaussian curve
y1=y[y<f(x)] #y co-ordinates of the points under the gaussian curve

plt.hist(x1, range=(0.0,10.0), density=True,label='density histogram') #plotting histogram
plt.plot(z,f(z),linewidth=4,label='gaussian PDF function') #plotting given PDF function

plt.xlim(0,10) #range of x axis
plt.ylim(0,1) #range of y axis
plt.title('x vs PDF') #title of the graph
plt.xlabel('x', fontsize=13) #label of x axis
plt.ylabel('PDF', fontsize=13) #label of y axis
plt.legend(fontsize=7,loc='upper left')
plt.show()
