#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:53:26 2020

@author: suman
"""

import numpy as np
from scipy.stats import chi2


Y1=np.array([4,10,10,13,20,18,18,11,13,14,13]) #observed count 1
Y2=np.array([3,7,11,15,19,24,21,17,13,9,5]) #observed count 2
p=np.array([4,8,12,16,20,24,20,16,12,8,4]) #expected count for getting different number

V1=np.sum((Y1-p)**2/p)
V2=np.sum((Y2-p)**2/p)

P1=1.0-chi2.cdf(V1,10.0) #probability of getting V1
P2=1.0-chi2.cdf(V2,10.0) #probability of getting V2
print(P1,P2)
