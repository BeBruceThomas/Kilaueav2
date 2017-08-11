#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the OKADA Class - DC3D
"""

import os
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))


# Moduls imported
from okada_wrapper.okada_wrapper import dc3d0wrapper, dc3dwrapper
import numpy as np
import matplotlib.pyplot as plt


os.chdir("/gps/Bruce/Kilaueav2")
# Load Data
from data import dataForOkada



plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern Roman']
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 14
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['lines.linewidth'] = 1


# Choose the path to access data 
path = "/gps/Bruce/Kilaueav2"

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

site_neu_slip = np.zeros((3, 15))

site_neu_slipX = open(path+"/data/site_neu/site_neu_slipX.dat", "r")
for i in range(15):
    site_neu_slip[0][i] = site_neu_slipX.readline()
site_neu_slipX.close()
site_neu_slipY = open(path+"/data/site_neu/site_neu_slipY.dat", "r")
for i in range(15):
    site_neu_slip[1][i] = site_neu_slipY.readline()
site_neu_slipY.close()
site_neu_slipZ = open(path+"/data/site_neu/site_neu_slipZ.dat", "r")
for i in range(15):
    site_neu_slip[2][i] = site_neu_slipZ.readline()
site_neu_slipZ.close()

site_neu_err = np.zeros((3, 15))

site_neu_errX = open(path+"/data/site_neu/site_neu_errX.dat", "r")
for i in range(15):
    site_neu_err[0][i] = site_neu_errX.readline()
site_neu_errX.close()
site_neu_errY = open(path+"/data/site_neu/site_neu_errY.dat", "r")
for i in range(15):
    site_neu_err[1][i] = site_neu_errY.readline()
site_neu_errY.close()
site_neu_errZ = open(path+"/data/site_neu/site_neu_errZ.dat", "r")
for i in range(15):
    site_neu_err[2][i] = site_neu_errZ.readline()
site_neu_errZ.close()





#--------------------------------------------------------------------------
# Functions 
#--------------------------------------------------------------------------


def okada_SWZR_fit():
    """
    Evaluates the misfit of an okada solution defined by the passed parameters to the slip (and errors) globally defined.
    """
    
    nsite = len(site_neu_err[0])
    
    slip_weights = np.zeros((3, nsite))
    for i in range(3):
        for j in range(nsite):
            slip_weights[i][j] = 1 / (site_neu_err[i][j]**2)
    
    # only for z first
    calc_slip = np.zeros((3, nsite))
    slip_misfit = np.zeros((3, nsite))
    
    for i in range(3):
        for j in range(nsite):
            site_slip = calc_SWZR_okada(dataForOkada.okada_start, site_neu_posn)
            calc_slip[i][j] = site_slip
            slip_misfit[i][j] = site_neu_slip[i][j] - calc_slip[i][j]
    
    misfit = np.zeros((1, nsite))
    
    for isite in range(15):            
        misfit[0][isite] = slip_misfit[0][isite] * slip_weights[2][isite] / (sum(slip_weights[2]))
    return misfit 



def calc_SWZR_okada(okada_params, site_neu):
    """
    """
    
    #result = dtopotools.SubFault().okada(self, site_neu[1] - okada_params[0], site_neu[0] - okada_params[1])
    
    success, u, grad_u = dc3dwrapper(0.6, 
                                     [1.0, 1.0, -1.0],
                                     3.0, 
                                     90, 
                                     [-0.7, 0.7], 
                                     [-0.7, 0.7],
                                     [1.0, 0.0, 0.0]
                                     ) 
        
    return success


  
def get_params():
    """
    """
    poisson_ratio = dataForOkada.okada_start[10]
    mu = 30
    lmda = (2 * mu * poisson_ratio) / (1 - 2 * poisson_ratio)
    alpha = (lmda + mu) / (lmda + 2 * mu)
    
    x0 = [ dataForOkada.okada_start[0], dataForOkada.okada_start[1], - dataForOkada.okada_start[2] ]
    depth = dataForOkada.okada_start[2]
    dip = dataForOkada.okada_start[4]
    strike_width = [ -dataForOkada.okada_start[5]/2, dataForOkada.okada_start[5]/2 ]
    dip_width = [ -dataForOkada.okada_start[6]/2, dataForOkada.okada_start[6]/2 ]
    dislocation = [ dataForOkada.okada_start[7], dataForOkada.okada_start[8], dataForOkada.okada_start[9] ]
    
    return alpha, x0, depth, dip, strike_width, dip_width, dislocation

def test_dc3d():
    """
    """
    alpha, x0, depth, dip, strike_width, dip_width, dislocation = get_params()
    n = [100, 100]
    x = np.linspace(dataForOkada.lower_bounds[0], dataForOkada.upper_bounds[0], n[0])
    y = np.linspace(dataForOkada.lower_bounds[1], dataForOkada.upper_bounds[1], n[1])
    ux = np.zeros((n[0], n[1]))
    for i in range(n[0]):
        for j in range(n[1]):
            success, u, grad_u = dc3dwrapper(alpha, [x[i], y[j], x0[2]],
                                             depth, 
                                             dip,
                                             strike_width, 
                                             dip_width,
                                             dislocation
                                            )
            assert(success == 0)
            ux[i, j] = u[0]

    levels = np.linspace(-0.5, 0.5, 21)
    cntrf = plt.contourf(x, y, ux.T, levels = levels)
    plt.contour(x, y, ux.T, colors = 'k', levels = levels, linestyles = 'solid')
    plt.xlabel('x')
    plt.ylabel('y')
    cbar = plt.colorbar(cntrf)
    tick_locator = plt.ticker.MaxNLocator(nbins=5)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.set_label('$u_{\\textrm{x}}$')
    plt.savefig("strike_slip.png")
    plt.show()



    
    

