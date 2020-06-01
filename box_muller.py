#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:24:01 2020

@author: suman
"""

import numpy as np
import matplotlib.pyplot as plt

#x1 and x2 are two uniform deviates
x1 = np.random.rand(10000) #10000 random numbers between 0 and 1
x2 = np.random.rand(10000) #10000 random numbers between 0 and 1

#y1 and y2 are two transformation of x1 and x2
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.hist(y2,range=(-5.0,5.0),density=True,label='density histogram') #plotting histogram
x=np.linspace(-5,5,100) #100 points between -5 and 5
plt.plot(x,(1/np.sqrt(2*np.pi))*np.exp(-x*x/2),linewidth=4,label='gaussian PDF function') #plotting gaussian PDF function
plt.xlim(-5,5) #range of x axis
plt.title('x vs PDF') #title of the graph
plt.xlabel('x', fontsize=13) #label of x axis
plt.ylabel('PDF', fontsize=13) #label of y axis
plt.legend(fontsize=7,loc='upper left')
plt.show()