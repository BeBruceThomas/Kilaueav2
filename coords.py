#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the GPS data for each year.
You will have to change the PATHS to data (excel or txt) !  
Could be done automatic.
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
# 2004
s2004 = access.sheet_by_name(sheets[4])
# 2006
s2006 = access.sheet_by_name(sheets[6])
# 2007
s2007 = access.sheet_by_name(sheets[8])
# 2008
s2008 = access.sheet_by_name(sheets[11])
# 2009
s2009 = access.sheet_by_name(sheets[13])
# 2011
s2011 = access.sheet_by_name(sheets[15])
# 2017
s2017 = access.sheet_by_name(sheets[17])


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

m2004 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2004[i][j] = s2004.cell_value(j,i)
        
m2006 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2006[i][j] = s2006.cell_value(j,i)
        
m2007 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2007[i][j] = s2007.cell_value(j,i)

m2008 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2008[i][j] = s2008.cell_value(j,i)

m2009 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2009[i][j] = s2009.cell_value(j,i)

m2011 = np.zeros((12,nsites))
for i in range(12):
    for j in range(nsites):
        m2011[i][j] = s2011.cell_value(j,i)
        
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

m2004c = np.zeros((4,nsites))
for j in range(nsites):
    m2004c[0][j] = m2004[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2004c[i][j] = m2004[i+3][j]

m2006c = np.zeros((4,nsites))
for j in range(nsites):
    m2006c[0][j] = m2006[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2006c[i][j] = m2006[i+3][j]

m2007c = np.zeros((4,nsites))
for j in range(nsites):
    m2007c[0][j] = m2007[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2007c[i][j] = m2007[i+3][j]

m2008c = np.zeros((4,nsites))
for j in range(nsites):
    m2008c[0][j] = m2008[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2008c[i][j] = m2008[i+3][j]

m2009c = np.zeros((4,nsites))
for j in range(nsites):
    m2009c[0][j] = m2009[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2009c[i][j] = m2009[i+3][j]

m2011c = np.zeros((4,nsites))
for j in range(nsites):
    m2011c[0][j] = m2011[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2011c[i][j] = m2011[i+3][j]
        
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

m2004l = np.zeros((4,nsites))
for j in range(nsites):
    m2004l[0][j] = m2004[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2004l[i][j] = m2004[i+6][j]

m2006l = np.zeros((4,nsites))
for j in range(nsites):
    m2006l[0][j] = m2006[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2006l[i][j] = m2006[i+6][j]

m2007l = np.zeros((4,nsites))
for j in range(nsites):
    m2007l[0][j] = m2007[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2007l[i][j] = m2007[i+6][j]

m2008l = np.zeros((4,nsites))
for j in range(nsites):
    m2008l[0][j] = m2008[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2008l[i][j] = m2008[i+6][j]

m2009l = np.zeros((4,nsites))
for j in range(nsites):
    m2009l[0][j] = m2009[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2009l[i][j] = m2009[i+6][j]

m2011l = np.zeros((4,nsites))
for j in range(nsites):
    m2011l[0][j] = m2011[0][j]
for i in range(1, 4):
    for j in range(nsites):
        m2011l[i][j] = m2011[i+6][j]
        
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

m2004u = np.zeros((3,nsites))
for j in range(nsites):
    m2004u[0][j] = m2004[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2004u[i][j] = m2004[i+9][j]

m2006u = np.zeros((3,nsites))
for j in range(nsites):
    m2006u[0][j] = m2006[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2006u[i][j] = m2006[i+9][j]

m2007u = np.zeros((3,nsites))
for j in range(nsites):
    m2007u[0][j] = m2007[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2007u[i][j] = m2007[i+9][j]

m2008u = np.zeros((3,nsites))
for j in range(nsites):
    m2008u[0][j] = m2008[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2008u[i][j] = m2008[i+9][j]

m2009u = np.zeros((3,nsites))
for j in range(nsites):
    m2009u[0][j] = m2009[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2009u[i][j] = m2009[i+9][j]

m2011u = np.zeros((3,nsites))
for j in range(nsites):
    m2011u[0][j] = m2011[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2011u[i][j] = m2011[i+9][j]
        
m2017u = np.zeros((3,nsites))
for j in range(nsites):
    m2017u[0][j] = m2017[0][j]
for i in range(1, 3):
    for j in range(nsites):
        m2017u[i][j] = m2017[i+9][j]    

m2017u_x = open("data/coords/m2017u_x.dat", "w")
m2017u_y = open("data/coords/m2017u_y.dat", "w")
for i in range(nsites):
    m2017u_x.write(str(m2017u[1][i]) + "\n")
    m2017u_y.write(str(m2017u[2][i]) + "\n")
m2017u_x.close() 
m2017u_y.close() 

# other way        
"""
m2017ll = np.zeros((4,nsites))
for j in range(nsites):
    m2017ll[0][j] = m2017[0][j]
    ll = geo.cart_to_geo(m2017[1][j], m2017[2][j], m2017[3][j])
    m2017ll[1][j] = ll[0]
    m2017ll[2][j] = ll[1]
    m2017ll[3][j] = ll[2]      
""" 
    
      
        
mYearsXY = [m2003u, m2004u, m2006u, m2007u, m2008u, m2009u, m2011u, m2017u]
mYearsZ = [m2003l, m2004l, m2006l, m2007l, m2008l, m2009l, m2011l, m2017l]
len_mYears = len(mYearsXY)
mYears_name = [2003, 2004, 2006, 2007, 2008, 2009, 2011, 2017]


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
m2017_2003 = np.empty((4,nsites))
m2017_2003[:] = np.NAN
m2017_2006 = np.empty((4,nsites))
m2017_2006[:] = np.NAN
m2017_2009 = np.empty((4,nsites))
m2017_2009[:] = np.NAN
m2017_2011 = np.empty((4,nsites))
m2017_2011[:] = np.NAN
m2006_2003 = np.empty((4,nsites))
m2006_2003[:] = np.NAN
m2011_2003 = np.empty((4,nsites))
m2011_2003[:] = np.NAN
m2011_2006 = np.empty((4,nsites))
m2011_2006[:] = np.NAN

# Loop on each site
for site in range(1, nsites+1):
    # First lien for id sites
    m2017_2003[0][site-1] = site
    m2017_2006[0][site-1] = site
    m2017_2009[0][site-1] = site
    m2017_2011[0][site-1] = site
    m2006_2003[0][site-1] = site
    m2011_2003[0][site-1] = site
    m2011_2006[0][site-1] = site
    # Test to know which year of start 
    if se['se_%02d' % site][1][0] != 'nan' and se['se_%02d' % site][1][-1] != 'nan':
        # m2017_2003
        m2017_2003[1][site-1] = - se['se_%02d' % site][1][0] + se['se_%02d' % site][1][-1]
        m2017_2003[2][site-1] = - se['se_%02d' % site][2][0] + se['se_%02d' % site][2][-1]
        m2017_2003[3][site-1] = - se['se_%02d' % site][3][0] + se['se_%02d' % site][3][-1]    
    if se['se_%02d' % site][1][2] != 'nan' and se['se_%02d' % site][1][-1] != 'nan':
        # m2017_2006
        m2017_2006[1][site-1] = - se['se_%02d' % site][1][2] + se['se_%02d' % site][1][-1]
        m2017_2006[2][site-1] = - se['se_%02d' % site][2][2] + se['se_%02d' % site][2][-1]
        m2017_2006[3][site-1] = - se['se_%02d' % site][3][2] + se['se_%02d' % site][3][-1] 
    if se['se_%02d' % site][1][5] != 'nan' and se['se_%02d' % site][1][-1] != 'nan':
        # m2017_2009
        m2017_2009[1][site-1] = - se['se_%02d' % site][1][5] + se['se_%02d' % site][1][-1]
        m2017_2009[2][site-1] = - se['se_%02d' % site][2][5] + se['se_%02d' % site][2][-1]
        m2017_2009[3][site-1] = - se['se_%02d' % site][3][5] + se['se_%02d' % site][3][-1] 
    if se['se_%02d' % site][1][6] != 'nan' and se['se_%02d' % site][1][-1] != 'nan':
        # m2017_2011
        m2017_2011[1][site-1] = - se['se_%02d' % site][1][6] + se['se_%02d' % site][1][-1]
        m2017_2011[2][site-1] = - se['se_%02d' % site][2][6] + se['se_%02d' % site][2][-1]
        m2017_2011[3][site-1] = - se['se_%02d' % site][3][6] + se['se_%02d' % site][3][-1] 
    if se['se_%02d' % site][1][0] != 'nan' and se['se_%02d' % site][1][2] != 'nan':
        # m2006_2003
        m2006_2003[1][site-1] = - se['se_%02d' % site][1][0] + se['se_%02d' % site][1][2]
        m2006_2003[2][site-1] = - se['se_%02d' % site][2][0] + se['se_%02d' % site][2][2]
        m2006_2003[3][site-1] = - se['se_%02d' % site][3][0] + se['se_%02d' % site][3][2] 
    if se['se_%02d' % site][1][0] != 'nan' and se['se_%02d' % site][1][6] != 'nan':
        # m2011_2003
        m2011_2003[1][site-1] = - se['se_%02d' % site][1][0] + se['se_%02d' % site][1][6]
        m2011_2003[2][site-1] = - se['se_%02d' % site][2][0] + se['se_%02d' % site][2][6]
        m2011_2003[3][site-1] = - se['se_%02d' % site][3][0] + se['se_%02d' % site][3][6] 
    if se['se_%02d' % site][1][2] != 'nan' and se['se_%02d' % site][1][6] != 'nan':
        # m2011_2006
        m2011_2006[1][site-1] = - se['se_%02d' % site][1][2] + se['se_%02d' % site][1][6]
        m2011_2006[2][site-1] = - se['se_%02d' % site][2][2] + se['se_%02d' % site][2][6]
        m2011_2006[3][site-1] = - se['se_%02d' % site][3][2] + se['se_%02d' % site][3][6] 
    # else, we let nan 


#print(m2017_2003)


