#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the Calendar class
"""


# Moduls imported
import numpy as np
from datetime import date


class Calendar():
    """
    Class to access all time data and permit conversions. 
    
    Attributs 
        name 
    
    Functions
        jdyTOmjd : convert julian-day & year to modified-julian-day
        mjdTOjdy : convert modified-julian-day to julian-day & year
    """
    
    def __init__(self, name):
        self.name = name
             
    def jdyTOmjd(self, jday, year):
        """
        Function to convert jday & year to modified-julian-day.
        """
        
        jday_zero = 34012
        year_zero = 1952
        
        if year < 100:
            # convert it to 4 digit 
            year = year + 1900
            if year < 1980:
                year = year + 100 
        
        numyears = year - year_zero
        numleaps = np.fix((numyears + 3) / 4)
        if numyears < 0:
            numleaps = np.fix((numyears) / 4)
        daydifference = numyears * 365
        mjd = (jday_zero - 1) + daydifference + numleaps + jday
        
        return(mjd)
    
    def mjdTOjdy(self, mjd):
        """
        Function to convert modified-julian-day to jday & year.
        """
        
        mattime = mjd + 678942
        datevects = date.fromordinal(mattime - 366)
        """
        years = 
        """
        doy1s = date.toordinal(datevects) + 366
        doys = mattime - doy1s + 1
        
        return(doys, years)