#!/usr/bin/env python3
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the ANNEX Class 
"""

# Moduls imported
import numpy as np


class Annex():
    
    def __init__(self, name):
        self.name = name
    
    def get_y(self, ifit, sub, isite):
        """
        We suppose first that there is only 2 time zones. So len_tz == 2.
        """
        
        # Create the list with time zones to study 
        list_startstop = [ifit[0]]
        i = 0
        while i <= len(ifit)-2:
            if ifit[i+1] != ifit[i] + 1:
                list_startstop.append(ifit[i])
                list_startstop.append(ifit[i+1])
            i += 1
        list_startstop.append(ifit[-1])
        
        # Count number of time zone
        #len_tz = len(list_startstop) / 2
        
        # Create the sub-divisions of sub
        stop1 = list_startstop[1]
        sub1 = sub[isite, :stop1]
        start2 = list_startstop[2]-1
        sub2 = sub[isite, start2:]
        # Transpose sub-divisions 
        sub1T = sub1.T
        sub2T = sub2.T
        
        # Concatenate the sub-divisions
        yT = np.concatenate((sub1T, sub2T))
        # Transpose to have final matrix
        y = yT.T
        
        return([y, sub1, sub2])