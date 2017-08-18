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


import coords
# Load BI_linefile
from data import bi


# Main program : all the run is done here
if __name__ == "__main__":
    
    ux03, uy03 = coords.m2003u[1], coords.m2003u[2]
    uy06 = coords.m2006u[2]
    uy09 = coords.m2011u[2]
    uy11 = coords.m2011u[2]
    
    #--------------------------------------------------------------------------
    # View in 3D: color for each year.
    #--------------------------------------------------------------------------    

    #try only the faults to see something 
    #put the lines to join 

    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
        
    # Loop on each site
    for year in range(coords.len_mYears):                
                       
        x = coords.mYearsXY[year][1]
        y = coords.mYearsXY[year][2]
        z = coords.mYearsZ[year][3]
        
        cmap = mpl.cm.autumn
        ax1.scatter(x, y, z, c=cmap(year / float(coords.len_mYears)), marker='o')
        
        #ax.scatter(xt, yt, zt, c='b', marker='^')
        
    ax1.set_xlabel('X Label')
    ax1.set_ylabel('Y Label')
    ax1.set_zlabel('Z Label')
        
    """
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
  
    # dx utm 
    d1_03_17 = coords.m2003_2017[1]
    d1_06_17 = coords.m2006_2017[1]
    d1_09_17 = coords.m2009_2017[1]
    d1_11_17 = coords.m2011_2017[1]
    d1_03_06 = coords.m2003_2006[1]
    d1_03_11 = coords.m2003_2011[1]
    d1_06_11 = coords.m2006_2011[1]
    
    # dy utm
    d2_03_17 = coords.m2003_2017[2]
    d2_06_17 = coords.m2006_2017[2]
    d2_09_17 = coords.m2009_2017[2]
    d2_11_17 = coords.m2011_2017[2]
    d2_03_06 = coords.m2003_2006[2]
    d2_03_11 = coords.m2003_2011[2]
    d2_06_11 = coords.m2006_2011[2]
    
    # dz utm
    d3_03_17 = coords.m2003_2017[3]
    d3_06_17 = coords.m2006_2017[3]
    d3_09_17 = coords.m2009_2017[3]
    d3_11_17 = coords.m2011_2017[3]
    d3_03_06 = coords.m2003_2006[3]
    d3_03_11 = coords.m2003_2011[3]
    d3_06_11 = coords.m2006_2011[3]
    
    print("Choose years of observartion in: \n 03-06to17")
    ch = input()
    
    
    if ch == "03-06to17":
    
        # Xcart
        X = plt.figure()
        axX = X.add_subplot(111)
                  
        plt.axhline(y=0.0, color='k')
        plt.axvline(x=2140269.57525397, color='k') # fault in 2
        plt.axvline(x=2141378.49758047, color='k') # fault in 17
        
        plt.plot(uy03, d1_03_17, marker='+', linestyle='', color='b', label="2017-2003")     
        for i in range(coords.nsites):
            plt.annotate(int(name[i]), (uy03[i], d1_03_17[i]))     
        plt.plot(uy06, d1_06_17, marker='+',  linestyle='', color='g', label="2017-2006")  
        for i in range(coords.nsites):
            plt.annotate(int(name[i]), (uy06[i], d1_06_17[i]))    
        
        plt.xlabel('Uy (m) : South to North')
        plt.ylabel('Cumulative Displacement in Ux (m)')
        plt.title('Ux')
        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
             
        # Ycart
        Y = plt.figure()
        axY = Y.add_subplot(111)   
           
        plt.axhline(y=0.0, color='k')
        plt.axvline(x=2140269.57525397, color='k') # fault in 2
        plt.axvline(x=2141378.49758047, color='k') # fault in 17
        
        plt.plot(uy03, d2_03_17, marker='+', linestyle='', color='b', label="2017-2003")     
        for i in range(coords.nsites):
            plt.annotate(int(name[i]), (uy03[i], d2_03_17[i]))     
        plt.plot(uy06, d2_06_17, marker='+',  linestyle='', color='g', label="2017-2006")  
        for i in range(coords.nsites):
            plt.annotate(int(name[i]), (uy06[i], d2_06_17[i]))    
    
        plt.xlabel('Uy (m) : South to North')
        plt.ylabel('Cumulative Displacement in Uy (m)')
        plt.title('Uy')
        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
            
        # Zcart
        Z = plt.figure()
        axZ = Z.add_subplot(111)
        
        plt.axhline(y=0.0, color='k')
        plt.axvline(x=2140269.57525397, color='k') # fault in 2
        plt.axvline(x=2141378.49758047, color='k') # fault in 17
        
        plt.plot(uy03, d3_03_17, marker='+', linestyle='', color='b', label="20017-2003")     
        for i in range(coords.nsites):
            plt.annotate(int(name[i]), (uy03[i], d3_03_17[i]))     
        plt.plot(uy06, d3_06_17, marker='+',  linestyle='', color='g', label="2017-2006")  
        for i in range(coords.nsites):
            plt.annotate(int(name[i]), (uy06[i], d3_06_17[i]))       
    
        plt.xlabel('Uy (m) : South to North')
        plt.ylabel('Cumulative Displacement in H (m)')
        plt.title('Uh')
        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)    
        
        plt.grid()
        plt.show()

    
    """
    # Xcart
    X = plt.figure()
    axX = X.add_subplot(111)
          
    plt.axhline(y=0.0, color='k')
    plt.axvline(x=2140269.57525397, color='k') # fault in 2
    plt.axvline(x=2141378.49758047, color='k') # fault in 17
    
    plt.plot(uy03, d1_03_17, marker='+', linestyle='', color='b', label="2017-2003")     
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d1_03_17[i]))     
    plt.plot(uy06, d1_06_17, marker='+',  linestyle='', color='g', label="2017-2006")  
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy06[i], d1_06_17[i]))    
    
    plt.plot(uy03, d1_03_06, marker='+', linestyle='', color='m', label="2006-2003") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d1_03_06[i]))    
    
    plt.plot(uy09, d1_09_17, marker='+', linestyle='', color='r', label="2017-2009")     
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy09[i], d1_09_17[i]))    
    plt.plot(uy11, d1_11_17, marker='+', linestyle='', color='c', label="2017-2011") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy11[i], d1_11_17[i]))    
    
    plt.plot(uy03, d1_03_11, marker='+', linestyle='', color='y', label="2011-2003") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d1_03_11[i]))    
    plt.plot(uy06, d1_06_11, marker='+', linestyle='', color='k', label="2011-2006") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy06[i], d1_06_11[i]))
    
    plt.xlabel('Uy (m) : South to North')
    plt.ylabel('Cumulative Displacement in Ux (m)')
    plt.title('Ux')
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
       
    
    # Ycart
    Y = plt.figure()
    axY = Y.add_subplot(111)   
          
    plt.axhline(y=0.0, color='k')
    plt.axvline(x=2140269.57525397, color='k') # fault in 2
    plt.axvline(x=2141378.49758047, color='k') # fault in 17
    
    plt.plot(uy03, d2_03_17, marker='+', linestyle='', color='b', label="2017-2003")     
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d2_03_17[i]))     
    plt.plot(uy06, d2_06_17, marker='+',  linestyle='', color='g', label="2017-2006")  
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy06[i], d2_06_17[i]))    
    
    plt.plot(uy03, d2_03_06, marker='+', linestyle='', color='m', label="2006-2003") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d2_03_06[i]))    
    
    plt.plot(uy09, d2_09_17, marker='+', linestyle='', color='r', label="2017-2009")     
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy09[i], d2_09_17[i]))    
    plt.plot(uy11, d2_11_17, marker='+', linestyle='', color='c', label="2017-2011") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy11[i], d2_11_17[i]))    
    
    plt.plot(uy03, d2_03_11, marker='+', linestyle='', color='y', label="2011-2003") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d2_03_11[i]))    
    plt.plot(uy06, d2_06_11, marker='+', linestyle='', color='k', label="2011-2006") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy06[i], d2_06_11[i]))
    

    plt.xlabel('Uy (m) : South to North')
    plt.ylabel('Cumulative Displacement in Uy (m)')
    plt.title('Uy')
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
    
    
    # Zcart
    Z = plt.figure()
    axZ = Z.add_subplot(111)
       
    plt.axhline(y=0.0, color='k')
    plt.axvline(x=2140269.57525397, color='k') # fault in 2
    plt.axvline(x=2141378.49758047, color='k') # fault in 17
    
    plt.plot(uy03, d3_03_17, marker='+', linestyle='', color='b', label="20017-2003")     
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d3_03_17[i]))     
    plt.plot(uy06, d3_06_17, marker='+',  linestyle='', color='g', label="2017-2006")  
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy06[i], d3_06_17[i]))    
    
    plt.plot(uy03, d3_03_06, marker='+', linestyle='', color='m', label="2006-2003") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d3_03_06[i]))    
    
    plt.plot(uy09, d3_09_17, marker='+', linestyle='', color='r', label="2017-2009")     
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy09[i], d3_09_17[i]))    
    plt.plot(uy11, d3_11_17, marker='+', linestyle='', color='c', label="2017-2011") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy11[i], d3_11_17[i]))    
    
    plt.plot(uy03, d3_03_11, marker='+', linestyle='', color='y', label="2011-2003") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy03[i], d3_03_11[i]))    
    plt.plot(uy06, d3_06_11, marker='+', linestyle='', color='k', label="2011-2006") 
    for i in range(coords.nsites):
        plt.annotate(int(name[i]), (uy06[i], d3_06_11[i]))
    

    plt.xlabel('Uy (m) : South to North')
    plt.ylabel('Cumulative Displacement in H (m)')
    plt.title('Uh')
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
    
    
    plt.grid()
    plt.show()
    
    """
    
    
    #--------------------------------------------------------------------------
    # Plot Kilauea map and . 
    #--------------------------------------------------------------------------
    

    plt.figure(figsize = (10, 10))
    # Plot faults?  
    plt.plot(bi.fx, bi.fy, 'k-')       
    # Plot Big Island
    plt.plot(bi.cx, bi.cy, 'k-')
    
    # Define limit axes
    axes = plt.gca()
    
    x0, y0, xe, ye = 254000, 2138000, 264000, 2148000
    x0f1, y0f1, xef1, yef1 = 260000, 2140000, 262000, 2141000

    
    plt.xlim([x0f1, xef1])
    plt.ylim([y0f1, yef1])
    
    plt.plot(ux03, uy03, 'bo')
    
    for i in range(66):
        # Simplfie notation
        ux = ux03[i]
        uy = uy03[i]
        #lati = lat[i][0]
        #long = lon[i][0]
        dux = - d1_03_17[i]
        duy = - d2_03_17[i]
        dh = d3_03_17[i]
        # Magenta arrows for elevation
        #if (lati >= xlims[0]) and (lati <= xlims[1]) and (long >= ylims[0]) and (long <= ylims[1]):
        plt.arrow(ux, uy, 0, dh*1000, head_width=10, head_length=10, fc='m', ec='m', clip_on=False)
            #plt.annotate('', xy=(lati, long+sU), xytext=(lati, long), arrowprops={'facecolor':'magenta', 'edgecolor':'magenta', 'linewidth':'0'})
        # Red arrows for motions
        #if (lati >= xlims[0]) and (lati <= xlims[1]) and (long >= ylims[0]) and (long <= ylims[1]):
        plt.arrow(ux, uy, dux*1000, duy*1000, head_width=10, head_length=10, fc='r', ec='r', clip_on=False)
            #plt.annotate('', xy=(lati+sE, long+sN), xytext=(lati, long), arrowprops={'facecolor':'red', 'edgecolor':'red', 'linewidth':'0'})
    
      
    plt.title("GPS Vectors")
    
