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


import os
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))


# Moduls imported
import numpy as np
import matplotlib.pyplot as plt
from scripts_okada.okada_wrapper.okada_wrapper import dc3d0wrapper, dc3dwrapper
"""
# nead scipy version 0.11.0 at least, not possible to use here because version 0.9.0 and upgrade doesn't work
import scipy 
print(scipy.__version__)
from scipy import optimize
from scipy.optimize import minimize
"""


# Import of extern moduls 
#from scripts_okada import okadadc3d
#from scripts_okada import test_okada


# Choose the path to access data 
path = "/gps/Bruce/Kilaueav2"

os.chdir("/gps/Bruce/Kilaueav2")

# Load dataForOkada
from data import dataForOkada

#--------------------------------------------------------------------------
# Fit an Okada : surface deformation due to a finite rectangular source.
#--------------------------------------------------------------------------



# Data
#--------------------------------------------------------------------------

m2017u = np.zeros((2, 66))
"""
with open(path+'/data/coords/m2017u_xmodif.dat') as f:
    fdata = [line.rstrip() for line in f]
with open(path+'/data/coords/m2017u_ymodif.dat') as f:
    fdata = [line.rstrip() for line in f]
""""""
m2017u_x = open(path+"/data/coords/m2017u_xmodif.dat", "r")
m2017u_y = open(path+"/data/coords/m2017u_ymodif.dat", "r")
for i in range(66):
    m2017u[0][i] = m2017u_x.readline()
    m2017u[1][i] = m2017u_y.readline()
m2017u_x.close()
m2017u_y.close()
"""
m2017u_x = [261019.167041,
261000.588192,
260994.969326,
261007.658321,
261020.950818,
261038.755829,
260997.989385,
260966.489602,
260918.673363,
260909.620073,
260891.508984,
260836.099641,
260794.310199,
260781.893628,
260734.393806,
260754.390613,
260763.444555,
260732.820087,
260710.466006,
260650.208959,
260629.624308,
260758.705512,
260584.868601,
260547.529067,
260534.991264,
260523.713494,
260466.066394,
260452.258372,
260426.555554,
260389.063283,
260415.347785,
260379.2597,
260379.776686,
260325.460241,
260308.247749,
260269.158898,
260251.228897,
260191.9983,
260207.906469,
260137.975251,
260038.457103,
260223.863458,
260187.793109,
260914.603357,
260815.398051,
260715.22381,
260622.994437,
260587.397885,
260525.161083,
260507.342749,
260417.792698,
260393.564802,
260399.069952,
260434.162622,
260449.13373,
260458.938316,
260415.335063,
260436.310307,
260419.4299,
260411.772691]
m2017u_y = [2140372.66466,
2140269.57525,
2140147.84576,
2140051.00059,
2140478.18352,
2140579.56606,
2140662.30476,
2140762.95566,
2140865.98344,
2140978.89289,
2141080.16454,
2141168.98073,
2141259.56711,
2141276.59354,
2141281.14994,
2141356.13711,
2141378.49758,
2141472.42172,
2141582.17563,
2141673.24251,
2141764.6638,
2141418.6039,
2141862.27082,
2141965.4271,
2142069.84716,
2142125.87269,
2142268.23351,
2142377.86567,
2142483.67936,
2142542.34682,
2142606.66268,
2142666.2272,
2142742.77337,
2142856.08138,
2142961.71682,
2143059.2705,
2143166.53099,
2143248.39674,
2143339.44709,
2143399.44476,
2143675.37971,
2143783.5128,
2143935.42013,
2139987.28731,
2139939.72837,
2139861.02239,
2139752.77188,
2139657.99369,
2139573.46698,
2139476.15004,
2139430.56812,
2139328.47529,
2139215.2412,
2139113.97658,
2138983.4869,
2138881.08446,
2138786.42731,
2138684.755,
2138585.40038,
2138491.50559
]
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


def get_params():
    """
    okada_pr are the okada parameters that matlab program gives us as the okada fit doesn't work on python
    """
    poisson_ratio = okada_pr[10]
    mu = 30
    lmda = (2 * mu * poisson_ratio) / (1 - 2 * poisson_ratio)
    alpha = (lmda + mu) / (lmda + 2 * mu)
    
    x0 = [ okada_pr[0], okada_pr[1], - okada_pr[2] ]
    depth = okada_pr[2]
    dip = okada_pr[4]
    strike_width = [ -okada_pr[5]/2, okada_pr[5]/2 ]
    dip_width = [ -okada_pr[6]/2, okada_pr[6]/2 ]
    dislocation = [ okada_pr[7], okada_pr[8], okada_pr[9] ]
    
    return alpha, x0, depth, dip, strike_width, dip_width, dislocation


def calc_SWZR_okada():
    """
    """
    alpha, x0, depth, dip, strike_width, dip_width, dislocation = get_params()
    x = m2017u_x
    n0 = len(x)
    print(x)
    y = m2017u_y
    n1 = len(y)
    print(y)
    ux = np.zeros((n0, n1))
    for i in range(n0):
        #for j in range(10):
        success, u, grad_u = dc3dwrapper(alpha, 
                                         [x[i], y[i], -1.0],
                                         depth, 
                                         dip,
                                         strike_width, 
                                         dip_width,
                                         dislocation
                                        )
        assert(success == 0)
        #ux[i, j] = u[0]
        #ux[i, i] = u[0]
        ux[i] = u[0]
        print(u[0])

    levels = np.linspace(-0.5, 0.5, 21)
    cntrf = plt.contourf(x, y, ux.T, levels = levels)
    plt.contour(x, y, ux.T, colors = 'k', levels = levels, linestyles = 'solid')
    plt.xlabel('x')
    plt.ylabel('y')
    print('gazou')
    cbar = plt.colorbar(cntrf)
    #tick_locator = plt.ticker.MaxNLocator(nbins=5)
    #cbar.locator = tick_locator
    #cbar.update_ticks()
    #cbar.set_label('$u_{\\textrm{x}}$')
    #plt.savefig("strike_slip.png")
    plt.show()
    print('gazou2')
    
    
    
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
    """

 
    



# Main Okada 
#--------------------------------------------------------------------------

# Okada parameters

okada_prA = dataForOkada.okada_intern[0]

len_bounds = len(okada_prA)

okada_pr = np.zeros(len_bounds)

for i in range(len_bounds):
    okada_pr[i] = okada_prA[i]


# Fit Okada 

"""
fun = okada_SWZR_fit()

pmin = lower_bounds # mimimum bounds
pmax = upper_bounds # maximum bounds
p_guess = (pmin + pmax)/2  
bounds = np.c_[pmin, pmax]  # [[pmin[0],pmax[0]], [pmin[1],pmax[1]]]

sol = scipy.optimize.minimize(fun, p_guess, args=(), bounds=bounds)   
    
if not sol.success:
    raise RuntimeError("Failed to solve")
okada_params = sol.x   
"""

okada_params = okada_pr

"""
nsite = 15
calc_slip = np.zeros((1, nsite))
#for isite in range(nsite):
    #site_slip = calc_SWZR_okada(okada_params, site_neu_posn)
#test_dc3d()
    #calc_slip[0][isite] = site_slip
"""


calc_SWZR_okada()     



"""
h_okada_vert=quiver(sitex-x0,sitey-y0,0*stepE',calc_slip(3,:)',1)
h_okada_horiz=quiver(sitex-x0,sitey-y0,calc_slip(2,:)',calc_slip(1,:)',1)
set(h_okada_horiz,'Color','k')
set(h_okada_vert,'Color',[.7 .7 .7])
"""
 





