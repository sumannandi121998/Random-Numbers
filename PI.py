#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:05:03 2020

@author: suman
"""

import numpy as np
from scipy.optimize import minimize
import emcee
import corner
import matplotlib.pyplot as plt

x= np.loadtxt("b.txt",delimiter='&',usecols=[1]) #importing x data from text file
y= np.loadtxt("b.txt",delimiter='&',usecols=[2]) #importing y data from text file
yerr= np.loadtxt("b.txt",delimiter='&',usecols=[3]) #importing uncertainty in y data from text file


def log_likelihood(params, x, y, yerr): #log of likelihood
    a,b,c = params #parameters in the model
    model = a*x*x + b*x+c #our model which have to fit in given data
    sigma2 = yerr**2 #sigma^2 of given y data
    return 0.5 * np.sum((y - model) ** 2 / sigma2 +np.log(2 * np.pi * sigma2))

def log_prior(params): #log of prior
    a,b,c = params #parameters in the model
    if -500.0 < a < 500 and -500.0 < b < 500.0 and -500.0 < c < 500.0:
        return 0.0 #choosing uniform prior
    return -np.inf

def log_probability(params, x, y, yerr): #posterior PDF
    l = log_prior(params)
    if not np.isfinite(l):
        return -np.inf
    return l - log_likelihood(params, x, y, yerr)

guess = (1.0, 1.0,1.0) #initial guess of parameters
soln = minimize(log_likelihood,guess,args=(x, y, yerr)) #minimum value of log of likelihood

chain=50 #no of Marcov Chains
n =3
pos = soln.x + 1e-4 * np.random.randn(chain, n) #initialising each of marcov chains near optimum value

sampler = emcee.EnsembleSampler(chain,n,log_probability,args=(x, y, yerr))
sampler.run_mcmc(pos, 4000) #doing MCMC for 4000 steps
samples = sampler.get_chain()

plt.plot(samples[:, :, 0]) # plotting the chains for a 
plt.ylim(-0.014,-0.002)
plt.title('Marcov Chain for a') #title of the graph
plt.xlabel('step', fontsize=13) #label of x axis
plt.ylabel('a', fontsize=13) #label of y axis
plt.show()
plt.plot(samples[:, :, 1]) # plotting the chains for b 
plt.ylim(1.5,6)
plt.title('Marcov Chain for b') #title of the graph
plt.xlabel('step', fontsize=13) #label of x axis
plt.ylabel('b', fontsize=13) #label of y axis
plt.show()
plt.plot(samples[:, :, 2]) # plotting the chains for c 
plt.ylim(-150,200)
plt.title('Marcov Chain for c') #title of the graph
plt.xlabel('step', fontsize=13) #label of x axis
plt.ylabel('c', fontsize=13) #label of y axis
plt.show()

s=samples.reshape((4000*50, 3))
fig = corner.corner(s,labels=['a','b','c'],quantiles=[0.16,0.5, 0.84],show_titles=True) #joint and marginalised posterior PDF
plt.show() 

medians=np.median(samples,axis=0)
k=np.random.randint(4000, size=200) #200 integer random no between 0 and 4000
a=np.average(medians[:,0]) #best fit value of a
b=np.average(medians[:,1]) #best fit value of b
c=np.average(medians[:,2]) #best fit value of c

z=np.linspace(0,300,10000) #10000 points between 0 and 300
plt.errorbar(x,y,yerr,fmt='o') #plotting given data with errorbar
for i in range(200):
    plt.plot(z,samples[k[i],0,0]*z*z+samples[k[i],0,1]*z+samples[k[i],0,2],color='y',alpha=0.2) #plotting randomly choosen model
plt.plot(z,a*z*z+b*z+c,color='r',label='best fit') #plotting best fit model
plt.xlim(0,300)
plt.title('data with best fit model') #title of the graph
plt.xlabel('x', fontsize=13) #label of x axis
plt.ylabel('y', fontsize=13) #label of y axis
plt.legend(fontsize=7,loc='upper left')
plt.show()