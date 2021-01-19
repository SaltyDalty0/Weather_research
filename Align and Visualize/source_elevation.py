#!/usr/bin/env python

## @package source_elevation.py
#
#    calculates the elevation of an astronomical source
#
#    \author DP (UofA)
#  
#    \version 1.0
#  
#    \date October 15, 2019
#
#    \bug No known bugs
#    
#    \warning No known warnings
#    
#    \todo Nothing left

import numpy as np
import matplotlib.pyplot as plt
import datetime

##@var telescopeCoord
# dictionary with the latitude and longitude of the telescope (in degrees)
# this is for the GLT
GLTCoord= {'lat': 76.5333,
           'lon': -68.6999}

LMTCoord= {'lat': 18.9857,
		   'lon': -97.3148}

SMTCoord= {'lat': 32.701611,
		   'lon': -109.891244}

AROCoord= {'lat': 31.9583,
		   'lon': -111.5967}  #(12M telescope)
ApexCoord={'lat': 23,
           'lon': 67}

JCMTCoord={'lat': 19,
           'lon': 155}


##@var sourceCoord
# dictionary with the RA (hh mm ss) and DEC (deg mm ss) of the source
# this is for M87
M87Coord={'RAh':12.0,
          'RAm':30.0,
          'RAs':49.423382,
          'DECd':12.0,
          'DECm':23.0,
          'DECs':28.04366}

SGRACoord={'RAh':17.0,
          'RAm':45.0,
          'RAs':40.036,
          'DECd':-29.0,
          'DECm':00.0,
          'DECs':28.17}


def sourceElevation(telescopeCoord,sourceCoord,obsDateTime):
    """!@brief calculate source elevation

    @param telescopeCoord dictionary with coordinates of telescope
 
    @param sourceCoord dictionary with source coordinates

    @param obsDateTime datetime with object with observing UT time

    @returns source elevation in degrees

    \author unknown (stackoverflow)
  
    \version 1.0
  
    \date October 15, 2019

    \bug No known bugs
    
    \warning No known warnings

    \todo Nothing left
    """
    # first calculate dayUT in year and timeUT
    new_year_day = datetime.datetime(obsDateTime.year, 1, 1)
    dayUT=(obsDateTime - new_year_day).days + 1

    timeUT=obsDateTime.hour+obsDateTime.minute/60+obsDateTime.second/3600
    
    # first calculate the GMST
    GMST_OFFSET = 6.6547660
    gmst = GMST_OFFSET+0.0657098244*dayUT+1.00273791*timeUT;

    # convert source RA and DEC to degrees
    ra_hr=sourceCoord['RAh']+sourceCoord['RAm']/60.+sourceCoord['RAs']/3600.
    dec_deg=sourceCoord['DECd']+sourceCoord['DECm']/60.+sourceCoord['DECs']/3600.

    # calculate source hour angle (in hours)
    gha_hr=gmst-ra_hr
    # convert it to rad
    gha_rad=np.pi*gha_hr/12.0

    # convert declination to rad
    dec_rad=np.pi*dec_deg/180.0

    # telescope latitude and longitude in rad
    tellat_rad=np.pi*telescopeCoord['lat']/180.0
    tellon_rad=np.pi*telescopeCoord['lon']/180.0

    # sine of elevation

    sinel=np.sin(tellat_rad)*np.sin(dec_rad)+np.cos(tellat_rad)*np.cos(dec_rad)*np.cos(gha_rad-tellon_rad)

    # elevation in degrees
    elevation=np.arcsin(sinel)*180./np.pi
    if (elevation<0): elevation=0
    return elevation


#elevation=sourceElevation(GLTCoord,M87Coord,datetime.datetime.now())

#print(elevation)
