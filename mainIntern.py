#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Main Program for Internship Kilauea 2017
Run in Console 
"""


# Moduls imported
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Name variables
from collections import defaultdict

# Get all the files in the current working directory: optionnal, just to check if the directory is the good one 
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))


# Choose the path to access data: have to find a solution to change only in the main only or directly emter in the interface 
path = "/gps/Bruce/Kilaueav2"


# Load final_vstack_out_pagers_rtv_datenums
import coords



# Main program : all the run is done here
if __name__ == "__main__":
    
    """    
    #--------------------------------------------------------------------------
    # View in 3D: color for each year.
    #--------------------------------------------------------------------------    

    #try only the faults to see something 
    #put the lines to join 

    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
        
    # Loop on each site
    for year in range(coords.len_mYears):                
                       
        x = coords.mYears[year][1]
        y = coords.mYears[year][2]
        z = coords.mYears[year][3]
        
        cmap = mpl.cm.autumn
        ax1.scatter(x, y, z, c=cmap(year / float(coords.len_mYears)), marker='o')
        
        #ax.scatter(xt, yt, zt, c='b', marker='^')
        
    ax1.set_xlabel('X Label')
    ax1.set_ylabel('Y Label')
    ax1.set_zlabel('Z Label')
        
   
    #--------------------------------------------------------------------------
    # View in 3D: color for each site.
    #--------------------------------------------------------------------------  
    
    #can also do it only for each site, have to put orientation

    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, projection='3d')
        
    # Loop on each site
    for site in range(1, 67):                
                       
        x = coords.se['se_%02d' % site][1]
        y = coords.se['se_%02d' % site][2]
        z = coords.se['se_%02d' % site][3]
        
        cmap = mpl.cm.autumn
        ax2.scatter(x, y, z, c=cmap(site / float(67)), marker='o')
        
        #ax.scatter(xt, yt, zt, c='b', marker='^')
        
    ax2.set_xlabel('X Label')
    ax2.set_ylabel('Y Label')
    ax2.set_zlabel('Z Label')
    
    """

    #--------------------------------------------------------------------------
    # Cumulative Distance from line.
    #--------------------------------------------------------------------------    
      
    line = [0] * coords.nsites
    name = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]

    # Absciss     
    uy09 = coords.m2009u[2]
    uy11 = coords.m2011u[2]
    
    # Xcart
    X = plt.figure()
    axX = X.add_subplot(111)
       
    d09 = coords.m2009_2017[1]
    d11 = coords.m2011_2017[1]
       
    plt.plot(uy09, line, linestyle='-', color='g')
    plt.plot(uy09, d09, marker='+', linestyle='', color='r') 
    plt.plot(uy11, d11, marker='+',  linestyle='', color='b')
    
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy09[i], d09[i]))
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy11[i], d11[i]))

    plt.xlabel('Uy (m)')
    plt.ylabel('Cumulative Displacement in Ux (m)')
    plt.legend()
        
    # Ycart
    Y = plt.figure()
    axY = Y.add_subplot(111)   
    
    d09 = coords.m2009_2017[2]      
    d11 = coords.m2011_2017[2]
       
    plt.plot(uy09, line, linestyle='-', color='g')
    plt.plot(uy09, d09, marker='+', linestyle='', color='r') 
    plt.plot(uy11, d11, marker='+',  linestyle='', color='b') 
    
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy09[i], d09[i]))
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy11[i], d11[i]))
    
    plt.xlabel('Uy (m)')
    plt.ylabel('Cumulative Displacement in Uy (m)')
    plt.legend()
    
    
    # Zcart
    Z = plt.figure()
    axZ = Z.add_subplot(111)
    
    d09 = coords.m2009_2017[3]
    d11 = coords.m2011_2017[3]
    
    plt.plot(uy09, line, linestyle='-', color='g')
    plt.plot(uy09, d09, marker='+', linestyle='', color='r') 
    plt.plot(uy11, d11, marker='+',  linestyle='', color='b')
    
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy09[i], d09[i]))
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy11[i], d11[i]))
        
    plt.xlabel('Uy (m)')
    plt.ylabel('Cumulative Displacement in H (m)')
    plt.legend()
    
    
    plt.grid()
    plt.show()
    

    