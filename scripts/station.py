#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the STATION Class
"""

# Moduls imported
import os
import numpy as np


class Station():
    """
    Class that manages all concerning the staion id and date. 
    
    Attributs 
        name
    
    Functions
        stname2num : assigns a station number to a station name according to a reference list
    """
    
    def __init__(self, name):
        self.name = name
    
    def stname2num(self, reflist, stnm):
        """
        Function which assigns a station number to a station name according to a reference list. 
        Be sure to respect the case. 
        
        Parameters
            reflist: reference list
            
        Output
            stnum: table with station numbers
        
        About
            Each row of the string matrices stnm and reflist contains a station name. 
            All names must have the same length (usually 4 characters). 
        
        Example
            if     reflist=['VAVA', 'NIUE', 'TGPS'] and stnm=['TGPS', 'HNLU']
            then   stnum=[2, NaN]  and  mn=1
        
        Credits
            On the base of MATLAB code from Mike Bevis, 5 June 1997.     
        """
          
        n1 = np.size(reflist)
        
        n2_temp = len(reflist[0])
        for i in range(n1):
            if n2_temp != len(reflist[i]):
                raise ValueError("Some names in 'reflist' don't have the same length.")
        n2 = n2_temp
        
        n3 = np.size(stnm)
        
        n4_temp = len(stnm[0])
        for i in range(n3):
            if n4_temp != len(stnm[i]):
                raise ValueError("Some names in 'stnm' don't have the same length.")
        n4 = n4_temp
        
        if n2 != n4:
            raise ValueError("Some names in 'stnm' and in 'reflist' don't have the same length.")
        
        stnum = np.zeros((n3, 1))        
        for i in range(n3):
            for j in range(n1):
                if stnm[i] == reflist[j]:
                    stnum[i] = j
        
        return(stnum)