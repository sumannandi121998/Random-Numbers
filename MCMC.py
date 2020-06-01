#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:42:50 2020

@author: suman
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x): #given PDF function according to which we have to sample random numbers
    if 3<x<7:
        return 1
    else:
        return 0
def g(x):
    return 0.25+0*x #normalised PDF function

n = 10000 #total no of steps
theta = 3.01 #initial value
samples = np.zeros(n+1)
samples[0] = theta
for i in range(n):
    theta_prime = theta + np.random.standard_normal() #new theta from proposal PDF
    r = np.random.rand() #a random number between 0 and 1
    if f(theta_prime)/f(theta) > r: #metropolis algorithm
        theta = theta_prime #updated theta value
    samples[i+1] = theta #array of sample points

plt.hist(samples, range=(3,7), density=True,label='density histogram') #plotting histogram
x=np.linspace(3,7,1000) #1000 points between 3 and 7
plt.plot(x,g(x),linewidth=4,label='normalised uniform PDF function') #plotting given PDF function
plt.xlim(3,7) #range of x axis
plt.ylim(0,0.3) #range of y axis
plt.title('x vs PDF') #title of the graph
plt.xlabel('x', fontsize=13) #label of x axis
plt.ylabel('PDF', fontsize=13) #label of y axis
plt.legend(fontsize=7,loc='upper left')
plt.show()

m=np.arange(0,n+1)
plt.plot(m,samples)#showing marcov Chain
plt.ylim(0,10)
plt.title('Marcov Chain') #title of the graph
plt.xlabel('step', fontsize=13) #label of x axis
plt.ylabel('Theta', fontsize=13) #label of y axis
plt.show()