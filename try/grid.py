#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:24:47 2017

@author: gps
"""

from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,6,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]
   
B = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,6,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]
   

plt.plot(A,B)

for xy in zip(A, B):                                       # <--
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

plt.grid()
plt.show()