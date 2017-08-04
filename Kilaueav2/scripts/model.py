#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the MODEL Class
"""

# Moduls imported
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

from scripts.calendar import Calendar
cal = Calendar("calendar")
from scripts.annex import Annex
annex = Annex("annex")


def fun(x, t, y):
    """
    x: vector of parameters (b, a0, a1)
        b: slope
        a0 and a1: intercept
    t: time in absciss
    y: observations 
    """
    
    fun = []
    for i in range(len(t)):
        value = x[0] * t[i] + x[1]
        fun.append(value)
        if (t[i] >= cal.jdyTOmjd(137, 2015)):
            fun[i] += x[2]
    res = []
    for i in range(len(y)):
        value = y[i] - fun[i][0]
        res.append(value)
    return(res)

    
class Model():
    
    def __init__(self, name, t_bef_step, t_aft_step):
        self.name = name
        self.t_bef_step = cal.jdyTOmjd(133, 2015)
        self.t_aft_step = cal.jdyTOmjd(137, 2015)
        
    def generate_data(self, t, b, a0, a1):
        
        y = []
        for i in range(len(t)):
            value = b * t[i] + a0
            y.append(value)
            if (t[i] >= self.t_aft_step):
                y[i] += a1
        return y
    
    
    def robust_step(self, data_t, data_y, t_bef_step, t_aft_step):
      
        y = data_y
        where_are_NaNs = np.isnan(y)
        y[where_are_NaNs] = 0
         
        t = data_t
                
        x0 = np.zeros(3)
        
        res_lsq = least_squares(fun, x0, args=(t, y))
        
        y_lsq = Model.generate_data(self, t, *res_lsq.x)
        
        plt.plot(t, y, '+', label='data')
        
        #t1 = int(self.t_bef_step)

        plt.plot(t, y_lsq, label='lsq')
        
        
        plt.xlabel('$t$')
        plt.ylabel('$y$')
        plt.legend()
        
        plt.show()
                
        bhat = res_lsq.x[0]
        a0hat = res_lsq.x[1]
        a1hat = res_lsq.x[2]
        
        # Standard error deviation 
        errD = np.std(y_lsq-y)
        # Standard error on coefficients 
        err = errD / np.sqrt(len(y))
        
        #err = stats.sem(res_lsq.x[2], axis=None)
        #err = np.sqrt(sum((y_lsq-y)**2)/len(y))
        
        return ([bhat, a0hat, a1hat, err])