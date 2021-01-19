#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:31:24 2019

@author: DaltonGlove
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime
from astropy.time import Time #ISO
import jdcal

# initialize colomuns of data
dates1 = []
dates2 = []
astro_dates = []
time = []
onlydates = []
index_list = np.array([])
Tau_data = np.array([])
i = 0

# import file and read into list called data
with open('/Users/DaltonGlove/Desktop/lmt_radiometer.csv', newline = '') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    data = list(readCSV)   

# scroll through list of data assigning columns to eah data peice
for row in data:
              
  # assign columns and iterate through rows          
         
            #date2 = row[1]
            date1 = row[0]
            # pull date as datetime object
            #date1 = datetime.datetime.strptime(date1, '%m/%d/%Y %H:%M:%S')
            #astrotime1 = Time(date1, scale='utc')
            #print(type(astrotime1))
            
            index = int(float(row[2]))
            Tau = float(row[3])
            # print(astrotime1, index, Tau) 
            # specify format with .iso or .tt.datetime
            
            astro_dates += [astrotime1] #np.append(datesJuls, dateJul)
            index_list += [index] #np.append(index_list, index)
            Tau_data += [Tau] #np.append(Tau_data, Tau)
print(astro_dates)
"""
i=0    
# open new file to write astropy dates and Tau data into with index        
with open('AstropyRadioData_file.csv', mode='w') as AstropyRadioData_file:

    #create callable command to write
    Data_writer = csv.writer(AstropyRadioData_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for i in range(len(astro_dates)):
        
    # write in rows 
        Data_writer.writerow([astro_dates[i], index_list[i], Tau_data[i]])
"""              