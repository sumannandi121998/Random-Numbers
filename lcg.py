#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:51:12 2020

@author: suman
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    return 1+0*x #uniform PDF function

z=np.linspace(0,1,100)
a = 1664525 #multiplier
c = 1013904223 #increment
m = 4294967296 #modulus
x = 0 #seed
n = 10000
results = np.array(0)
start = time.time()
for i in range(n-1):
    x = (a*x+c)%m #linear congruential random no generator
    results=np.append(results,x) #appending each random number to a array
y=results/np.amax(results) #deviding each number by maximum random no
t1=time.time() - start #time taken for generating 10000 random no
print('Time taken =',t1) #printing the result

plt.hist(y,range=(0.0,1.0),density=True,label='density histogram') #plotting histogram
plt.plot(z,f(z),linewidth=4,label='uniform PDF function') #plotting uniform PDF function

plt.xlim(0,1) #range of x axis
plt.ylim(0,1.3) #range of y axis
plt.title('x vs PDF') #title of the graph
plt.xlabel('x', fontsize=13) #label of x axis
plt.ylabel('PDF', fontsize=13) #label of y axis
plt.legend(fontsize=7,loc='upper left')
plt.show()