#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the Okada Data
You will have to change the PATHS to data (excel or txt) !  
"""


# Moduls imported
import numpy as np


path = "/gps/Bruce/Kilaueav2/data/dataForOkada"



okada_initial_params = np.zeros((3, 11))

okada_start = open(path+"/okada_start.txt", "r")
for i in range(11):
    okada_initial_params[1][i] = okada_start.readline()
okada_start.close()

upper_bounds = open(path+"/upper_bounds.txt", "r")
for i in range(11):
    okada_initial_params[0][i] = upper_bounds.readline()
upper_bounds.close()

lower_bounds = open(path+"/lower_bounds.txt", "r")
for i in range(11):
    okada_initial_params[2][i] = lower_bounds.readline()
lower_bounds.close()