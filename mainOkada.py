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
print(scipy.__version__)
from scipy import optimize
from scipy.optimize import minimize


# Get all the files in the current working directory: optionnal, just to check if the directory is the good one 
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))


# Import of extern moduls 
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

upper_bounds = np.zeros(len_bounds)
okada_start = np.zeros(len_bounds)
lower_bounds = np.zeros(len_bounds)

for i in range(len_bounds):
    upper_bounds[i] = upper_boundsA[i]
    okada_start[i] = okada_startA[i]
    lower_bounds[i] = lower_boundsA[i]

"""
# Create a sample fault and print out some information about it: use of CLAWPACK version for Okada.
fault, subfault = okaC.set_params(okada_start)
print ("This sample fault has %s meter of slip over a %s by %s km patch" % (subfault.slip,subfault.length/1e3,subfault.width/1e3))
print ("With shear modulus %4.1e Pa the seismic moment is %4.1e" % (subfault.mu, subfault.Mo()))
print ("   corresponding to an earthquake with moment magnitude %s" % fault.Mw())
print ("The depth at the top edge of the fault plane is %s km" % (subfault.depth/1e3)) 
"""


# Fit an okada to the data

fun = okadadc3d.okada_SWZR_fit()

pmin = lower_bounds # mimimum bounds
pmax = upper_bounds # maximum bounds
p_guess = (pmin + pmax)/2  
bounds = np.c_[pmin, pmax]  # [[pmin[0],pmax[0]], [pmin[1],pmax[1]]]

sol = scipy.optimize.minimize(fun, p_guess, args=(), bounds=bounds)   
    
if not sol.success:
    raise RuntimeError("Failed to solve")
okada_params = sol.x   




"""   
okada_params = scipy.optimize.fminbound(okadadc3d.okada_SWZR_fit(), lower_bounds[0][i], upper_bounds[0][i])
#[okada_params, fval, exit_flag, num_func] = scipy.optimize.fminbound(test_okada.test_dc3d(), lower_bounds[0][i], upper_bounds[0][i])
"""






x = np.array([[ 1247.04,  1274.9 ,  1277.81,  1259.51,  1246.06,  1230.2 ,
     1207.37,  1192.  ,  1180.84,  1182.76,  1194.76,  1222.65],
   [  589.  ,   581.29,   576.1 ,   570.28,   566.45,   575.99,
      601.1 ,   620.6 ,   637.04,   631.68,   611.79,   599.19]])

y = np.array([ 1872.81,  1875.41,  1871.43,  1865.94,  1854.8 ,  1839.2 ,
    1827.82,  1831.73,  1846.68,  1856.56,  1861.02,  1867.15])

"""
fp   = lambda p, x: p[0]*x[0]+p[1]*x[1]
e    = lambda p, x, y: ((fp(p,x)-y)**2).sum()
pmin = np.array([0.5,0.5]) # mimimum bounds
pmax = np.array([1.5,1.5]) # maximum bounds
popt = sciopt.fminbound(e, pmin, pmax, args=(x,y))
"""
"""
fp   = lambda p, x: p[0]*x[0]+p[1]*x[1]
e    = lambda p, x, y: ((fp(p,x)-y)**2).sum()
pmin = np.array([0.5,0.5]) # mimimum bounds
pmax = np.array([1.5,1.5]) # maximum bounds
p_guess = (pmin + pmax)/2
bounds = np.c_[pmin, pmax]  # [[pmin[0],pmax[0]], [pmin[1],pmax[1]]]
sol = minimize(e, p_guess, args=(x,y), bounds=bounds)
print(sol)
if not sol.success:
    raise RuntimeError("Failed to solve")
popt = sol.x

"""









    

"""
#[okada_params,resnorm,residual,exitflag] =  lsqnonlin('okada_SWRZ_fit',okada_start,lower_bounds,upper_bounds);
options = optimset('fminsearch');
[okada_params,resnorm,exitflag,output] =  fminsearchbnd('okada_SWRZ_fit',okada_start,lower_bounds,upper_bounds,options);
"""
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

"""
h_okada_vert=quiver(sitex-x0,sitey-y0,0*stepE',calc_slip(3,:)',1)
h_okada_horiz=quiver(sitex-x0,sitey-y0,calc_slip(2,:)',calc_slip(1,:)',1)
set(h_okada_horiz,'Color','k')
set(h_okada_vert,'Color',[.7 .7 .7])
"""
 





