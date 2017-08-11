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
    # View in 3D.
    #--------------------------------------------------------------------------    
    
    # Loop on each site
    for site in range(1, 67):                
                
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        x = coords.se['se_%02d' % site][1]
        y = coords.se['se_%02d' % site][2]
        z = coords.se['se_%02d' % site][3]
               
        ax.scatter(x, y, z, c='r', marker='o')
        
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        
        plt.show()
    


    #--------------------------------------------------------------------------
    # Distance from line.
    #--------------------------------------------------------------------------    
    
    # Define line going North (coudl also do 2 different following sites in general EW)
    # North line based on k001 latitude
    
    
    
    
    
    