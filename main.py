#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Main Program 
Run in Console 
"""


# Moduls imported
import os
import numpy as np
import matplotlib.pyplot as plt


# Get all the files in the current working directory: optionnal, just to check if the directory is the good one 
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))


# Import of extern moduls 
from scripts.calendar import Calendar
cal = Calendar("calendar")
from scripts.station import Station
sta = Station("station")
from scripts.model import Model
mod = Model("model", cal.jdyTOmjd(137, 2015), cal.jdyTOmjd(133, 2015))
from scripts.annex import Annex
annex = Annex("annex")
from scripts.geographic import Geographic
geo = Geographic("geographic")

# Choose the path to access data: have to find a solution to change only in the main only or directly emter in the interface 
path = "/gps/Bruce/Kilaueav2"


# Load final_vstack_out_pagers_rtv_datenums
from data import rtv
# Load BI_linefile
from data import bi





# Main program : all the run is done here
if __name__ == "__main__":
    
    
    #--------------------------------------------------------------------------
    # GPS station : ids and dates 
    #--------------------------------------------------------------------------
    
    
    # Date of start of analyse
    t0 = cal.jdyTOmjd(125, 2015)
    # Dates of start and end of dike
    t1 = cal.jdyTOmjd(133, 2015)
    t2 = cal.jdyTOmjd(137, 2015)
    
    # Reference sites for GPS
    # kilsites is currently a list but on matlab it was a table          
    kilsites = ['UWEV', 'NUPM', 'AHUP', 'HOVL', 'CNPK', 'BYRL', 'NPIT', 'KOSM', 'OUTL', 'CRIM', 'MANE', 'HLNA', 'KFAP', 'AINP', 'GOPM']
    
    # isN : table with numbers assigned at each GPS station name
    # ! "is" is not use as a variable in Python beaucause it already exist as a function in Python, not the same as in MATLAB 
    isN = sta.stname2num(rtv.stnm, kilsites)
    # isN size : 15 lines (GPS number) for 1 column
    len_isN = len(isN)
    
    # it : array with ids of measures after t0 
    it = np.where(rtv.epochs >= t0)
    # it size : 1 line for n columns (398)
    len_it = len(it[0])
    
    # mjds : list with dates assigned at each ids of array "it"
    # mjds size : len_it elements (398)
    mjds = [0] * len_it
    for i in range(len_it):
        mjds[i] = rtv.epochs[it[0][i]]
    # conversion of mjds in jdays & years
    """
    # Conversion in jdays & years 
    # [doys, yrs] = mjday(mjds)
    jdys = np.zeros((len_it,2))
    for i in range(len_it):
        [doys, yrs] = cal.mjdTOjdy( mjds[i] )
        jdys[i][0] = doys
        jdys[i][1] = yrs
    """
    
    # subN, subE, subU : tables for north, east and altitude coordinates for the stations of interest after date t0
    # subN, subE, subU size : len_isN (15) lines, one for each GPS & len_it (398) columns, one for each date of measure after t0
    subN = np.zeros((len_isN, len_it))
    for i in range(len_it):
        for j in range(len_isN):
            subN[j][i] = rtv.rt_north.cell_value(int(isN[j][0])+1, i+311)
    subE = np.zeros((len_isN, len_it))
    for i in range(len_it):
        for j in range(len_isN):
            subE[j][i] = rtv.rt_east.cell_value(int(isN[j][0])+1, i+311)
    subU = np.zeros((len_isN, len_it))
    for i in range(len_it):
        for j in range(len_isN):
            subU[j][i] = rtv.rt_up.cell_value(int(isN[j][0])+1, i+311)
    
    
    # ifit : list with dates after t0 but not during the dike, same role as it but without dike dates and has the form of a list not array
    # ifit size : date number (303) elements 
    ifit1 = np.where(mjds <= t1)[0]
    ifit2 = np.where(mjds >= t2)[0]
    len_ifit = len(ifit1) + len(ifit2)
    #ifit = np.zeros((1, len_ifit))
    ifit = [0] * len_ifit
    j = 0
    for i in range(len_ifit):
        if i <= len(ifit1)-1:
            ifit[i] = ifit1[i] + 1
        else:
            ifit[i] = ifit2[j] + 1
            j += 1
    
    
    
    #--------------------------------------------------------------------------
    # Fit a Robust Step to each site's time series.
    #--------------------------------------------------------------------------
    
    
    # x : table with dates for each ifit ids (without dike) 
    # x size : n lines (303) for 1 column 
    
    x = np.zeros((len_ifit, 1))
    for i in range(len_ifit):
        x[i][0] = mjds[ifit[i]-1]
    
    
    # search on each GPS site 
    stepN = [0] * len_isN
    errsN = [0] * len_isN  
    stepE = [0] * len_isN
    errsE = [0] * len_isN
    stepU = [0] * len_isN
    errsU = [0] * len_isN
    
    for isite in range(0, len_isN):
        [bhat, a0hat, a1hat, err] = mod.robust_step(x, annex.get_y(ifit, subN, isite)[0], t1, t2)
        stepN[isite] = a1hat
        errsN[isite] = err
        [bhat, a0hat, a1hat, err] = mod.robust_step(x, annex.get_y(ifit, subE, isite)[0], t1, t2)
        stepE[isite] = a1hat
        errsE[isite] = err
        [bhat, a0hat, a1hat, err] = mod.robust_step(x, annex.get_y(ifit, subU, isite)[0], t1, t2)
        stepU[isite] = a1hat
        errsU[isite] = err 
    
    
    # Save data in a GMT-readable table
    fid = open("Kilauea_May2015_Intrusion.dat", "w")
    fid.write("Site     Lat          Lon            Elev       N (mm)    err     E (mm)    err     U (mm)    err")
    fid.write("")
    
    # Write data for each GPS station 
    for isite in range(len_isN):
        
        fid.write("\n" 
                  + kilsites[isite] 
                  + "     " 
                  + str( format(rtv.lat[ int(isN[isite][0]) ] [0], '.5f') ) 
                  + "     "
                  + str( format(rtv.lon[ int(isN[isite][0]) ] [0], '.5f') )
                  + "     "
                  + str( format(rtv.elev[ int(isN[isite][0]) ] [0], '.1f').zfill(6) )
                  + "     "
                  + str( format(stepN[isite], '.1f').zfill(5) )
                  + "     "
                  + str( format(errsN[isite], '.1f') )
                  + "     "
                  + str( format(stepE[isite], '.1f').zfill(5) )
                  + "     "
                  + str( format(errsE[isite], '.1f') )
                  + "     "
                  + str( format(stepU[isite], '.1f').zfill(5) )
                  + "     "
                  + str( format(errsU[isite], '.1f') )
                  )
    
    # Close table for a save!
    fid.close()
    
    
    #--------------------------------------------------------------------------
    # Plot GPS data and linear regression. 
    #--------------------------------------------------------------------------
    
    
    # Plot variables
    x0 = 250000
    y0 = 2140000
    xlims = [0, 20000]
    ylims = [-3000, 13000]
    
    # site : table with UTM coordinate of each station GPS 
    sitex = np.zeros((len_isN, 1))
    sitey = np.zeros((len_isN, 1))
    for isite in range(len_isN):
        result = geo.from_latlon(rtv.lat[ int(isN[isite][0]) ][0], rtv.lon[ int(isN[isite][0]) ][0])
        sitex[isite] = result[0]
        sitey[isite] = result[1]               
    
    #twocolfig(6.5)
    plt.figure(figsize = (10, 8))
    # Plot faults?  
    plt.plot(bi.fx - x0, bi.fy - y0, 'k-')   
    
    # Plot Big Island
    plt.plot(bi.cx - x0, bi.cy - y0, 'k-')
    
    # Define limit axes
    
    axes = plt.gca()
    #axes.set_xlim([xlims[0], xlims[1]])
    #axes.set_ylim([ylims[0], ylims[1]])
    
    plt.xlim([xlims[0], xlims[1]])
    plt.ylim([ylims[0], ylims[1]])
    
    plt.plot(sitex - x0, sitey - y0, 'bo')
    
    for i in range(len_isN):
        # Simplfie notation
        lat = sitex - x0
        lon = sitey - y0
        lati = lat[i][0]
        long = lon[i][0]
        sU = stepU[i]
        sE = stepE[i]
        sN = stepN[i]
        # Magenta arrows for elevation
        if (lati >= xlims[0]) and (lati <= xlims[1]) and (long >= ylims[0]) and (long <= ylims[1]):
            plt.arrow(lati, long, 0, sU*100, head_width=500, head_length=1000, fc='m', ec='m', clip_on=False)
            #plt.annotate('', xy=(lati, long+sU), xytext=(lati, long), arrowprops={'facecolor':'magenta', 'edgecolor':'magenta', 'linewidth':'0'})
        # Red arrows for motions
        if (lati >= xlims[0]) and (lati <= xlims[1]) and (long >= ylims[0]) and (long <= ylims[1]):
            plt.arrow(lati, long, sE*100, sN*100, head_width=500, head_length=1000, fc='r', ec='r', clip_on=False)
            #plt.annotate('', xy=(lati+sE, long+sN), xytext=(lati, long), arrowprops={'facecolor':'red', 'edgecolor':'red', 'linewidth':'0'})
    
      
    plt.title("GPS Vectors between days 133 and 137 2015")
    
    plt.show()
    plt.savefig("GPS_Vectors_133_137_2015.png")
    
    
    #--------------------------------------------------------------------------
    # First Part of Okada.
    #--------------------------------------------------------------------------
    
    
    # Definition of the site locations & motions
    site_neu_posn = np.zeros((3,len_isN))    
    for isite in range(len_isN):
        result = geo.from_latlon(rtv.lat[ int(isN[isite][0]) ][0], rtv.lon[ int(isN[isite][0]) ][0])
        site_neu_posn[0][isite] = result[1] - y0
        site_neu_posn[1][isite] = result[0] - x0 
        site_neu_posn[2][isite] = rtv.elev[int(isN[isite][0])]
    site_neu_slip = [stepN, stepE, stepU]
    site_neu_err =  [errsN, errsE, errsU]
    
    
    # Save data in a GMT-readable table
    f_posnY = open("data/site_neu/site_neu_posnY.dat", "w")
    for i in range(len_isN):
        f_posnY.write(str(site_neu_posn[0][i]) + "\n")
    f_posnY.close()    
    f_posnX = open("data/site_neu/site_neu_posnX.dat", "w")
    for i in range(len_isN):
        f_posnX.write(str(site_neu_posn[1][i]) + "\n")
    f_posnX.close()      
    f_posnZ = open("data/site_neu/site_neu_posnZ.dat", "w")
    for i in range(len_isN):
        f_posnZ.write(str(site_neu_posn[2][i]) + "\n")
    f_posnZ.close()  
    
    f_slipY = open("data/site_neu/site_neu_slipY.dat", "w")
    for i in range(len_isN):
        f_slipY.write(str(site_neu_slip[0][i]) + "\n")
    f_slipY.close()  
    f_slipX = open("data/site_neu/site_neu_slipX.dat", "w")
    for i in range(len_isN):
        f_slipX.write(str(site_neu_slip[1][i]) + "\n")
    f_slipX.close()  
    f_slipZ = open("data/site_neu/site_neu_slipZ.dat", "w")
    for i in range(len_isN):
        f_slipZ.write(str(site_neu_slip[2][i]) + "\n")
    f_slipZ.close()      
    
    f_errY = open("data/site_neu/site_neu_errY.dat", "w")
    for i in range(len_isN):
        f_errY.write(str(site_neu_err[0][i]) + "\n")
    f_errY.close() 
    f_errX = open("data/site_neu/site_neu_errX.dat", "w")
    for i in range(len_isN):
        f_errX.write(str(site_neu_err[1][i]) + "\n")
    f_errX.close() 
    f_errZ = open("data/site_neu/site_neu_errZ.dat", "w")
    for i in range(len_isN):
        f_errZ.write(str(site_neu_err[2][i]) + "\n")
    f_errZ.close()