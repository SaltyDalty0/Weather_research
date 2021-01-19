#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:08:57 2019

@author: DaltonGlove
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime
import jdcal

  #initialize colomuns of data
dates1 = []
datesJuls = []
index_list = []
Tau_data = []
i=0 
#import file and read into list called data
with open('/Users/DaltonGlove/Desktop/lmt_radiometer.csv', newline = '') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    data = list(readCSV)   
#open new file to write julian dates and Tau data into with index        
with open('JulRadioData_file.csv', mode='w') as JulRadioData_file:

    #create callable command to write
    Data_writer = csv.writer(JulRadioData_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
#scroll through list of data assigning columns to eah data peice
    for row in data:
            
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
          
            #recast dates as julian date and float w/ jdcal switch to use astropy for this
            dateJul = float(sum(jdcal.gcal2jd(date1.year, date1.month, date1.day))+ date1.hour + date1.minute + date1.second) 
            dateJul = dateJul + date1.hour*.0416666 + date1.minute*.0006945 + date1.second*.000012 - .5
              
            #dateJul = Time(date1, scale='utc')
       
            #append to arrays
            datesJuls += ([dateJul])
            index_list += ([i])
            Tau_data += ([float(row[3])])
            
            Data_writer.writerow([dateJul, i, float(row[3])])
            i+=1
Npts = len(datesJuls)
print("total datapoints:", Npts, "1st and last dates in Julian are:\n" , datesJuls[0], " and ", datesJuls[Npts-1])
"""
# average sections of data to smooth out
aveTau = []
stepNpts = 250 #average over this many pts
dateSlices = []

i=0
while i < Npts : 
    
    if (i+stepNpts) < Npts :
        aveTau += [sum(Tau_data[i:i+stepNpts])/stepNpts]
        dateSlices += [datesJuls[i+int(stepNpts/2)]]
    
    # adjust to capture last interval of data
    elif (i+stepNpts) > Npts: 
        Npts2Ave = Npts - i
        aveTau += [sum(Tau_data[i:i+Npts2Ave])/Npts2Ave]
        dateSlices += [datesJuls[i+int(Npts2Ave/2)]]
    i+=stepNpts
print("averagelists:", aveTau)       
fig, ax = plt.subplots()
ax.plot (dateSlices, aveTau, 'b')  
ax.set(title='yearly smoothed(Npts=250)', xlabel='dates', ylabel='Optical Depth')
ax.grid()
#plt.ylim(0, 2.5)
#plt.savefig('YearlyAve_weather_data.png')

 #switch to binary save files
#outfile = open(Julian_npzfile
#np.savez(Julian_npzfile, datesJuls=datesJuls, Tau_data=Tau_data)
#outfile.seek(0)
#npzfile = np.load(outfile)
#npzfile.files
#['y', 'x']
#npzfile['x']
"""     
