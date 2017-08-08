#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Okada Program
Run in Terminal
"""


# Moduls imported
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy import optimize


# Get all the files in the current working directory: optionnal, just to check if the directory is the good one 
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))


# Import of extern moduls 
"""
import main 
"""
from scripts_okada import okadadc3d
from scripts_okada import test_okada


# Choose the path to access data 
path = "/gps/Bruce/Kilaueav2"

# Load dataForOkada
from data import dataForOkada





#--------------------------------------------------------------------------
# Fit an Okada : surface deformation due to a finite rectangular source.
#--------------------------------------------------------------------------


# Okada parameters
upper_boundsA = dataForOkada.okada_initial_params[0]
okada_startA  = dataForOkada.okada_initial_params[1]
lower_boundsA = dataForOkada.okada_initial_params[2]
len_bounds = len(okada_startA)
upper_bounds = np.zeros((1, len_bounds))
okada_start = np.zeros((1, len_bounds))
lower_bounds = np.zeros((1, len_bounds))
for i in range(len_bounds):
    upper_bounds[0][i] = upper_boundsA[i]
    okada_start[0][i] = okada_startA[i]
    lower_bounds[0][i] = lower_boundsA[i]

"""
# Create a sample fault and print out some information about it: use of CLAWPACK version for Okada.
fault, subfault = okaC.set_params(okada_start)
print ("This sample fault has %s meter of slip over a %s by %s km patch" % (subfault.slip,subfault.length/1e3,subfault.width/1e3))
print ("With shear modulus %4.1e Pa the seismic moment is %4.1e" % (subfault.mu, subfault.Mo()))
print ("   corresponding to an earthquake with moment magnitude %s" % fault.Mw())
print ("The depth at the top edge of the fault plane is %s km" % (subfault.depth/1e3)) 
"""

# Fit an okada to the data
result = np.zeros((len_bounds, 4))
#[okada_params, fval, exit_flag, num_func]
for i in range(len_bounds):
    [okada_params, fval, exit_flag, num_func] = scipy.optimize.fminbound(okadadc3d.okada_SWZR_fit(), lower_bounds[0][i], upper_bounds[0][i])
    [okada_params, fval, exit_flag, num_func] = scipy.optimize.fminbound(test_okada.test_dc3d(), lower_bounds[0][i], upper_bounds[0][i])
    
    result[i][0] = okada_params
    result[i][1] = fval
    result[i][2] = exit_flag
    result[i][3] = num_func
    

"""
#[okada_params,resnorm,residual,exitflag] =  lsqnonlin('okada_SWRZ_fit',okada_start,lower_bounds,upper_bounds);
options = optimset('fminsearch');
[okada_params,resnorm,exitflag,output] =  fminsearchbnd('okada_SWRZ_fit',okada_start,lower_bounds,upper_bounds,options);
"""

site_neu_posn = np.zeros((3, 15))

site_neu_posnX = open(path+"/data/site_neu/site_neu_posnX.dat", "r")
for i in range(15):
    site_neu_posn[0][i] = site_neu_posnX.readline()
site_neu_posnX.close()
site_neu_posnY = open(path+"/data/site_neu/site_neu_posnY.dat", "r")
for i in range(15):
    site_neu_posn[1][i] = site_neu_posnY.readline()
site_neu_posnY.close()
site_neu_posnZ = open(path+"/data/site_neu/site_neu_posnZ.dat", "r")
for i in range(15):
    site_neu_posn[2][i] = site_neu_posnZ.readline()
site_neu_posnZ.close()


nsite = len(15)
calc_slip = np.zeros((1, nsite))
for isite in range(nsite):
    site_slip = okadadc3d.calc_SWZR_okada(okada_params, site_neu_posn)
    calc_slip[0][isite] = site_slip
         

"""
h_okada_vert=quiver(sitex-x0,sitey-y0,0*stepE',calc_slip(3,:)',1)
h_okada_horiz=quiver(sitex-x0,sitey-y0,calc_slip(2,:)',calc_slip(1,:)',1)
set(h_okada_horiz,'Color','k')
set(h_okada_vert,'Color',[.7 .7 .7])
"""
 





