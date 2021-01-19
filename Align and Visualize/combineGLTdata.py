#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:34:03 2019
to combine csv files
@author: DaltonGlove
"""

import csv 
import datetime

i=1
j=0

#open and read each file into data list
with open('/Users/DaltonGlove/Desktop/GLT_WeatherData_recent.csv', newline = '') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #data1[row][index, object ID, date time timestamp, datetime, humidity, 
    #           wind direction, wind speed, pressure, temperature, score=timestamp]
    data1 = list(readCSV) 
    
    
with open('/Users/DaltonGlove/Desktop/GLT_radiometerData_recent.csv', newline = '') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #data2[row][index, timestamp, datetime, Tau, elevation, 
    #            rainflag, rainflagQuality]
    data2 = list(readCSV) 
        
#print(data1[0][3], data2[0][2], type(data1[0][3]), type(data2[0][2]))
    
with open('GLT_WeatherradiometerData_recent3.csv', mode='w') as GLT_WeatherradiometerData_recent3:

    #create callable command to write
    Data_writer = csv.writer(GLT_WeatherradiometerData_recent3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
#scroll through list of data assigning columns to eah data peice
        
    for row in data1:       #every ten minutes
            
        #set object types for easier comparison
            date1 = datetime.datetime.strptime(row[3], '%m/%d/%y %H:%M')
            date2 = datetime.datetime.strptime(data2[j][2], '%m/%d/%y %H:%M')
            
            date1=date1.replace(second=0, microsecond=0)
            date2=date2.replace(second=0, microsecond=0)
            
            stamp_date1 = datetime.datetime.timestamp(date1)
            stamp_date2 = datetime.datetime.timestamp(date2)
            
            frac_date1 =((stamp_date1/3.154e7)+1970)
            frac_date2 =((stamp_date2/3.154e7)+1970)
            
            while stamp_date2<stamp_date1:
            #for (frac_date2<frac_date1) :    
                                #timestamp and datetime with timestamp error use time stamp at end of list for iterating if needed
                Data_writer.writerow([i, -1, data2[j][1], date2, date2, data2[j][3], -1, -1, -1, -1, -1, data2[j][1]])
                j+=1
                i+=1 
                date2 = datetime.datetime.strptime(data2[j][2], '%m/%d/%y %H:%M')
                date2=date2.replace(second=0, microsecond=0)
                stamp_date2 = datetime.datetime.timestamp(date2)
                frac_date2 =((stamp_date2/3.154e7)+1970)
                #check if data1 is at or past first iteration of data2    
            if stamp_date1<stamp_date2: 
                 		# index, id, timestamp, datetime, datetime, Tau, humidity, wind Direction, wind speed, pressure, temperature, timestamp 
                Data_writer.writerow([i, row[1], stamp_date1, date1, date1, -1, row[4], row[5], row[6], row[7], row[8], row[9]])    #put -1 in for Tau if no measurement
                #elif date2>date1:

                i+=1
            if stamp_date1==stamp_date2:  #write both data into when it lines up
                #print(date1, date2)
            
                Data_writer.writerow([i, row[1], stamp_date2, date1, date2, data2[j][3], row[4], row[5], row[6], row[7], row[8], row[9]])
                j+=1                                        
                i+=1
            
                #if frac_date1<frac_date2: break  #might break from whole loop
            if i%1000==0:print(i, ' out of about ', (len(data1)+len(data2)))
       
            