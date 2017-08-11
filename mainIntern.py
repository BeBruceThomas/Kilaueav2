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


# Get all the files in the current working directory: optionnal, just to check if the directory is the good one 
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))


# Choose the path to access data: have to find a solution to change only in the main only or directly emter in the interface 
path = "/gps/Bruce/Kilaueav2"


# Load final_vstack_out_pagers_rtv_datenums
from data import coords



# Main program : all the run is done here
if __name__ == "__main__":
    
    
    #--------------------------------------------------------------------------
    # View in 3D: color for each year.
    #--------------------------------------------------------------------------    

    """
    try only the faults to see something 
    put the lines to join 
    """
    
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
    
    """
    can also do it only for each site, have to put orientation
    """
    
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
    

    #--------------------------------------------------------------------------
    # Cumulative Distance from line.
    #--------------------------------------------------------------------------    
    
    # Define line going North (could also do 2 different following sites in general EW)
    # North line based on k001 latitude
    
    


    
    plt.show()
    



    
    
    
    
    
    