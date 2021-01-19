#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 02:07:38 2020

@author: DaltonGlove
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import csv, datetime

hum_list = []
PWV_list=[]
windD_list = []
windS_list = []
press_list = []
temp_list = []
dates = [] 
frac_dates = []
index_list = []



with open('/Users/DaltonGlove/Desktop/Apex_radiometer.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
i=2
while i< len(data)-6:  # index, id, timestamp, datetime, datetime, Tau, humidity%, wind Direction(east of north), wind speed, pressure, temperature, timestamp 
    # pull date as datetime object and add to astropy array   
        
    if len(data[i]):
        #print(type(data[i][0]), data[i][0])
        date1 = datetime.datetime.strptime(data[i][0], '%Y-%m-%dT%H:%M:%S')
        stamp_date1 = datetime.datetime.timestamp(date1)
        frac_date1 =((stamp_date1/3.154e7)+1970)
        index = int(i-1)
        #Tau = float(row[5])
        #hum = float(data[i][2])
        #windD = float(data[i][5])
        #windS = float(data[i][6])
        #press = float(data[i][3])
        #temp = float(data[i][4])
        #transmit = math.exp(-Tau)
    
        #hum_list += [hum]
        #windD_list += [windD]
        #windS_list += [windS]
        #press_list += [press]
        #temp_list += [temp]
        #dates += [date1] 
        #frac_dates += [frac_date1]
        #index_list += [index]  
        
        if len(data[i][1]):
            if -1.1<float(data[i][1])<10:
                PWV = float(data[i][1])
        else: PWV = -1
        
        PWV_list+=[PWV]
        frac_dates+=[frac_date1]
        dates+=[date1]
       
        if i%10000==0:print(i, date1, frac_date1, PWV)
        
        i+=1



fig, axs = plt.subplots()
    
    ###################################
    #   Weather scatter+line plot style 
    ###################################
figsize=(8,6.5) #size of the figure

    #rcParams['text.usetex']=True
    #rcParams['font.family']='sans-serif'
    #rcParams['font.sans-serif']='Latin Modern Roman'

    # axes and tickmarks
rcParams['axes.labelsize']=18
    #rcParams['axes.labelweight']=600
rcParams['axes.linewidth']=1.5

rcParams['xtick.labelsize']=16
rcParams['xtick.top']=True
rcParams['xtick.bottom']=True
rcParams['xtick.direction']='in'
rcParams['xtick.major.size']=6
rcParams['xtick.minor.size']=3
rcParams['xtick.major.width']=1.2
rcParams['xtick.minor.width']=1.2
rcParams['xtick.minor.visible']=True
rcParams['ytick.labelsize']=16
rcParams['ytick.left']=True
rcParams['ytick.right']=True
rcParams['ytick.direction']='in'
rcParams['ytick.major.size']=6
rcParams['ytick.minor.size']=3
rcParams['ytick.major.width']=1.2
rcParams['ytick.minor.width']=1.2
rcParams['ytick.minor.visible']=True

    # points, errorbars, and lines
rcParams['lines.linewidth']=2.0
rcParams['lines.markeredgewidth']=0.5
rcParams['lines.markersize']=6
rcParams['errorbar.capsize']=2

plt.figure(figsize=figsize)            # size of the figure

#Tau_list1=[]
#transmit_list1=[]
#frac_dates1=[]
#for i in range(len(PWV_list)):
#    if PWV_list[i]!=-1:
#        PWV+=[Tau_data[i]]
#        frac_dates1+=[frac_dates[i]]
            #elevation_list+=[sourceElevation(GLTCoord, M87Coord, dates[i])]
    #data=(transmit_list, elevation_list)
    #print(len(frac_dates1),len(elevation_list))
plt.scatter(frac_dates, PWV_list, alpha = .5, s=5)
    #axs.plot(frac_dates1, elevation_list, label="elevation")
plt.xlabel('Time(fractional dates)')    #('time of day (hr)')
plt.ylabel('Perc. Water Vapor')
plt.text(1,1, 'Apex')
#plt.ylim(0, 5)
    #fig.tight_layout()
plt.show()
plt.savefig('Apex_PWV_data.png', format='png')
