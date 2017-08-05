#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the OKADA Class - CLAWPACK
"""

# Moduls imported
from clawpack.geoclaw import dtopotools

# Load Data
from data import dataForOkada
from data import site_neu



class OkadaCLAWPACK():
 
    
    def __init__(self, name):
        self.name = name

    
    def set_params(self, params):
        """
        Set the subfault parameters. 
        """
        
        subfault = dtopotools.SubFault()
        
        subfault.longitude = params[0]
        subfault.latitude = params[1]
        subfault.depth = params[2]
        subfault.strike = params[3]
        subfault.dip = params[4]
        subfault.length = params[5]
        subfault.width = params[6]
        subfault.rake = params[7]
        subfault.slip = params[8]

        subfault.coordinate_specification = "top center"
    
        fault = dtopotools.Fault()
        fault.subfaults = [subfault]
        
        return fault, subfault
      
        
    def calc_SWZR_okada(self, okada_params, site_neu):
        """
        """
        
        result = dtopotools.SubFault().okada(self, site_neu[1] - okada_params[0], site_neu[0] - okada_params[1])
        
        return result