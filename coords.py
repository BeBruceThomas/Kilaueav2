#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the GPS data for each year.
You will have to change the PATHS to data (excel or txt) !  
"""

import os
# Get all the files in the current working directory: optionnal, just to check if the directory is the good one 
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))
"""
from scripts.geographic import Geographic
geo = Geographic("geographic")
"""
import numpy as np
# Excel modul 
import xlrd
from openpyxl import load_workbook
# Name variables
from collections import defaultdict

nsites = 66

#--------------------------------------------------------------------------
# Open useful data.
#-------------------------------------------------------------------------- 

# Open Excel
path = "/gps/Bruce/Kilaueav2/data/coords"
access = xlrd.open_workbook(path+"/alldata.xlsx")
lendata = load_workbook(filename=path+"/alldata.xlsx", read_only=True)

# Open all sheets
sheets = access.sheet_names()

# 2003
s2003 = access.sheet_by_name(sheets[2])
# 2006
s2006 = access.sheet_by_name(sheets[6])
# 2017
s2017 = access.sheet_by_name(sheets[19])


#--------------------------------------------------------------------------
# Convert in Python transposed matrix.
#-------------------------------------------------------------------------- 

"""
Exemple of a matrix per year
For one year
array([[ id site ...],
       [ x ...],
       [ y ...],
       [ z ...]])
"""

"""
mm = defaultdict(int)
for year in [2003, 2017]:
    print('s%04d' % year)
    mm['mm%04d' % year] = np.zeros((12,nsites))
    for i in range(12):
        for j in range(nsites):
            mm['mm%04d' % year][i][j] = mm['s%04d' % year].cell_value(j,i)
    print(mm['mm%04d' % year])
"""



# Copy in Python matrix

m2003 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2003[i][j] = s2003.cell_value(j,i)

m2006 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2006[i][j] = s2006.cell_value(j,i)
        
m2017 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2017[i][j] = s2017.cell_value(j,i)


# Matrix cartesian X, Y, Z in meters

m2003c = np.zeros((4,nsites))
for j in range(nsites):
    m2003c[0][j] = m2003[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2003c[i][j] = m2003[i+3][j]

m2006c = np.zeros((4,nsites))
for j in range(nsites):
    m2006c[0][j] = m2006[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2006c[i][j] = m2006[i+3][j]
        
m2017c = np.zeros((4,nsites))
for j in range(nsites):
    m2017c[0][j] = m2017[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2017c[i][j] = m2017[i+3][j]


# Matrix latitude longitude in deg and h in meters 

m2003l = np.zeros((4,nsites))
for j in range(nsites):
    m2003l[0][j] = m2003[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2003l[i][j] = m2003[i+6][j]

m2006l = np.zeros((4,nsites))
for j in range(nsites):
    m2006l[0][j] = m2006[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2006l[i][j] = m2006[i+6][j]
        
m2017l = np.zeros((4,nsites))
for j in range(nsites):
    m2017l[0][j] = m2017[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2017l[i][j] = m2017[i+6][j]

# Matrix utm x y in meters 

m2003u = np.zeros((3,nsites))
for j in range(nsites):
    m2003u[0][j] = m2003[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2003u[i][j] = m2003[i+9][j]

m2006u = np.zeros((3,nsites))
for j in range(nsites):
    m2006u[0][j] = m2006[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2006u[i][j] = m2006[i+9][j]
        
m2017u = np.zeros((3,nsites))
for j in range(nsites):
    m2017u[0][j] = m2017[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2017u[i][j] = m2017[i+9][j]    

# other way        
"""
m2009ll = np.zeros((4,lens2009))
for j in range(lens2009):
    m2009ll[0][j] = m2009[0][j]
    ll = geo.cart_to_geo(m2009[1][j], m2009[2][j], m2009[3][j])
    m2009ll[1][j] = ll[0]
    m2009ll[2][j] = ll[1]
    m2009ll[3][j] = ll[2]

m2011ll = np.zeros((4,lens2011))
for j in range(lens2011):
    m2011ll[0][j] = m2011[0][j]
    ll = geo.cart_to_geo(m2011[1][j], m2011[2][j], m2011[3][j])
    m2011ll[1][j] = ll[0]
    m2011ll[2][j] = ll[1]
    m2011ll[3][j] = ll[2]

m2017ll = np.zeros((4,nsites))
for j in range(nsites):
    m2017ll[0][j] = m2017[0][j]
    ll = geo.cart_to_geo(m2017[1][j], m2017[2][j], m2017[3][j])
    m2017ll[1][j] = ll[0]
    m2017ll[2][j] = ll[1]
    m2017ll[3][j] = ll[2]      
""" 
    
      
        
mYearsXY = [m2003u, m2006u, m2017u]
mYearsZ = [m2003l, m2006l, m2017l]
len_mYears = len(mYearsXY)
mYears_name = [2003, 2006, 2017]


#--------------------------------------------------------------------------
# Table per site (1 to 66) with coordinates for each year.
#--------------------------------------------------------------------------

"""
Exemple of a matrix for site evolution
For one site
array([[ year ...],
       [ x ...],
       [ y ...],
       [ z ...]])
"""

# Site evolution
se = defaultdict(int)

# Loop on each site
for site in range(1, nsites+1):
    # Create matrix changing name 
    se['se_%02d' % site] = np.empty((4,len_mYears))
    se['se_%02d' % site][:] = np.NAN   
    # Loop on each year of data
    for year in range(len_mYears):
        m = mYearsXY[year]
        # Loop to find the site
        for i in range(len(m[0])):
            se['se_%02d' % site][0][year] = mYears_name[year]
            # Check if data for this site
            if site == m[0][i]:
                se['se_%02d' % site][1][year] = m[1][i]
                se['se_%02d' % site][2][year] = m[2][i]
    for year in range(len_mYears):
        m = mYearsZ[year]
        # Loop to find the site
        for i in range(len(m[0])):
            # Check if data for this site
            if site == m[0][i]:
                se['se_%02d' % site][3][year] = m[3][i]

"""
for key, value in sorted(se.items()):
    print (key, value)
"""


#--------------------------------------------------------------------------
# Table of displacements for each point. 
#--------------------------------------------------------------------------

"""
This is between first year of measure and last year of measure.
Not always the same years for each site, so there will be many matrix like that.

Exemple of a matrix between 2 years.
For 2 years
array([[ id site ...],
       [ dx ...],
       [ dy ...],
       [ dz ...]])
"""

# Define matrix of years 
m2003_2017 = np.empty((4,nsites))
m2003_2017[:] = np.NAN
m2006_2017 = np.empty((4,nsites))
m2006_2017[:] = np.NAN

# Loop on each site
for site in range(1, nsites+1):
    # First lien for id sites
    m2003_2017[0][site-1] = site
    # Test to know which year of start 
    if se['se_%02d' % site][1][0] != 'nan' and se['se_%02d' % site][1][-1] != 'nan':
        # m2009_2017
        m2003_2017[1][site-1] = se['se_%02d' % site][1][0] - se['se_%02d' % site][1][-1]
        m2003_2017[2][site-1] = se['se_%02d' % site][2][0] - se['se_%02d' % site][2][-1]
        m2003_2017[3][site-1] = se['se_%02d' % site][3][0] - se['se_%02d' % site][3][-1]
    if se['se_%02d' % site][1][1] != 'nan' and se['se_%02d' % site][1][-1] != 'nan':
        # m2011_2017
        m2006_2017[1][site-1] = se['se_%02d' % site][1][1] - se['se_%02d' % site][1][-1]
        m2006_2017[2][site-1] = se['se_%02d' % site][2][1] - se['se_%02d' % site][2][-1]
        m2006_2017[3][site-1] = se['se_%02d' % site][3][1] - se['se_%02d' % site][3][-1] 
    # else, we let nan 


#print(m2003_2017)
