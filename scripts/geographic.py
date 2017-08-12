#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the GEOGRAPHIC Class
"""

# Moduls imported
import math

# Global variables

K0 = 0.9996

E = 0.00669438
E2 = E * E
E3 = E2 * E
E_P2 = E / (1.0 - E)

SQRT_E = math.sqrt(1 - E)
_E = (1 - SQRT_E) / (1 + SQRT_E)
_E2 = _E * _E
_E3 = _E2 * _E
_E4 = _E3 * _E
_E5 = _E4 * _E

M1 = (1 - E / 4 - 3 * E2 / 64 - 5 * E3 / 256)
M2 = (3 * E / 8 + 3 * E2 / 32 + 45 * E3 / 1024)
M3 = (15 * E2 / 256 + 45 * E3 / 1024)
M4 = (35 * E3 / 3072)

P2 = (3. / 2 * _E - 27. / 32 * _E3 + 269. / 512 * _E5)
P3 = (21. / 16 * _E2 - 55. / 32 * _E4)
P4 = (151. / 96 * _E3 - 417. / 128 * _E5)
P5 = (1097. / 512 * _E4)

R = 6378137

ZONE_LETTERS = "CDEFGHJKLMNPQRSTUVWXX"



class OutOfRangeError(ValueError):
    pass



class Geographic():
    
    def __init__(self, name):
        self.name = name
    
    def d2u(self, lon, lat, zone):
        """
        
        """
    
    def from_latlon(self, latitude, longitude, force_zone_number=None):
        """
        This function convert Latitude and Longitude to UTM coordinate
    
        Parameters
        ----------
        latitude: float
            Latitude between 80 deg S and 84 deg N, e.g. (-80.0 to 84.0)

        longitude: float
            Longitude between 180 deg W and 180 deg E, e.g. (-180.0 to 180.0).

        force_zone number: int
            Zone Number is represented with global map numbers of an UTM Zone
            Numbers Map. You may force conversion including one UTM Zone Number.
            More information see utmzones.
        """
        
        if not -80.0 <= latitude <= 84.0:
            raise OutOfRangeError("latitude out of range (must be between 80 deg S and 84 deg N)")
        if not -180.0 <= longitude <= 180.0:
            raise OutOfRangeError("longitude out of range (must be between 180 deg W and 180 deg E)")
    
        lat_rad = math.radians(latitude)
        lat_sin = math.sin(lat_rad)
        lat_cos = math.cos(lat_rad)
    
        lat_tan = lat_sin / lat_cos
        lat_tan2 = lat_tan * lat_tan
        lat_tan4 = lat_tan2 * lat_tan2
    
        if force_zone_number is None:
            zone_number = Geographic.latlon_to_zone_number(self, latitude, longitude)
        else:
            zone_number = force_zone_number
    
        zone_letter = Geographic.latitude_to_zone_letter(self, latitude)
    
        lon_rad = math.radians(longitude)
        central_lon = Geographic.zone_number_to_central_longitude(self, zone_number)
        central_lon_rad = math.radians(central_lon)
    
        n = R / math.sqrt(1 - E * lat_sin**2)
        c = E_P2 * lat_cos**2
    
        a = lat_cos * (lon_rad - central_lon_rad)
        a2 = a * a
        a3 = a2 * a
        a4 = a3 * a
        a5 = a4 * a
        a6 = a5 * a
    
        m = R * (M1 * lat_rad -
                 M2 * math.sin(2 * lat_rad) +
                 M3 * math.sin(4 * lat_rad) -
                 M4 * math.sin(6 * lat_rad))
    
        easting = K0 * n * (a +
                            a3 / 6 * (1 - lat_tan2 + c) +
                            a5 / 120 * (5 - 18 * lat_tan2 + lat_tan4 + 72 * c - 58 * E_P2)) + 500000
    
        northing = K0 * (m + n * lat_tan * (a2 / 2 +
                                            a4 / 24 * (5 - lat_tan2 + 9 * c + 4 * c**2) +
                                            a6 / 720 * (61 - 58 * lat_tan2 + lat_tan4 + 600 * c - 330 * E_P2)))
    
        if latitude < 0:
            northing += 10000000
    
        return ([easting, northing, zone_number, zone_letter])
    
    
    def latitude_to_zone_letter(self, latitude):
        
        if -80 <= latitude <= 84:
            return (ZONE_LETTERS[int(latitude + 80) >> 3])
        else:
            return (None)
    
    
    def latlon_to_zone_number(self, latitude, longitude):
        
        if 56 <= latitude < 64 and 3 <= longitude < 12:
            return (32)
    
        if 72 <= latitude <= 84 and longitude >= 0:
            if longitude <= 9:
                return (31)
            elif longitude <= 21:
                return (33)
            elif longitude <= 33:
                return (35)
            elif longitude <= 42:
                return (37)
    
        return (int((longitude + 180) / 6) + 1)
    
    
    def zone_number_to_central_longitude(self, zone_number):
        
        return ((zone_number - 1) * 6 - 180 + 3)