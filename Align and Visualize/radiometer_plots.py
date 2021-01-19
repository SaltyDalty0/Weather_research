#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:37:34 2019

@author: DaltonGlove
"""

import csv
#import numpy as np
import math
import matplotlib.pyplot as plt, mpld3
import matplotlib
from matplotlib import rcParams
from pylab import text
import datetime
from source_elevation import sourceElevation, GLTCoord, M87Coord, LMTCoord, SMTCoord, AROCoord, SGRACoord, ApexCoord, JCMTCoord
#from matplotlib import rcParams    #change plot parameters
#import pandas as pd

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta


  #initialize colomuns of data
dates=[]
frac_dates=[]
index_list=[]
Tau_data=[]
PWV_list=[]
transmit_list=[]
hum_list=[]
windD_list=[]
windS_list=[]
press_list=[]
temp_list=[]
minthresh1=0
minthresh2=0

elevation_list1=[]
elevation_list2=[]
SatCoord= {'lat': 19,
           'lon': 155}

i=0

print("please select GLT, LMT, SMT, 12m, Apex, JCMT, or all data:")
char = str(input())
#for char in chars: **make listable input for overlaying graphs**
if char=='GLT' or char=='1' or char=='glt':    
#import file and read into list called data

###WIND: "C:\\Users\\LENOVO\\PATH"  MAC:'/Users/DaltonGlove/PATH'###
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\GLT_Weather.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    SatCoord==GLTCoord
    for row in data:  # index, id, timestamp, datetime, datetime, Tau, humidity%, wind Direction(east of north), wind speed, pressure, temperature, timestamp 
    # pull date as datetime object and add to astropy array    
        date1 = datetime.datetime.strptime(row[3], '%m/%d/%y %H:%M')
        stamp_date1 = datetime.datetime.timestamp(date1)
        frac_date1 =((stamp_date1/3.154e7)+1970)
        index = int(i)
        Tau = float(row[5])
        hum = int(row[6])
        windD = int(row[7])
        windS = float(row[8])
        press = float(row[9])
        temp = float(row[10])
        transmit = math.exp(-Tau)
    
        hum_list += [hum]
        windD_list += [windD]
        windS_list += [windS]
        press_list += [press]
        temp_list += [temp]
        dates += [date1] 
        frac_dates += [frac_date1]
        index_list += [index]  
        Tau_data += [Tau] 
        transmit_list += [transmit]
        i+=1


if char=='JCMT' or char=='6' or char=='jcmt':
    
#import file and read into list called data
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\JCMT_1989_2007.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)
        
    i=1
    SatCoord==JCMTCoord
    while i<len(data):
        if len(data[i]):
            date1 = datetime.datetime.strptime(data[i][1], '%b %d %Y %I:%M:%S:000%p')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(i)
            #nr,utdatetime,hst,tau_225,tau_error,csu_ut_dmf,tuple
            
            if len(data[i][3]):Tau=float(data[i][3])
            else: Tau=-1
            

            Tau_data+=[Tau]   #PWV_list+=[PWV]  
        
            
            dates += [date1] 
            frac_dates += [frac_date1]
            index_list += [index]  

            #if i%10000==0:print(i, data[i])
        
            i+=1
        

if char=='APEX' or char=='5' or char=='apex' or char=='Apex':
    
#import file and read into list called data
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\Apex_radiometer.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    i=2
    SatCoord==ApexCoord
    while i< len(data)-6:  # index, id, timestamp, datetime, datetime, Tau, humidity%, wind Direction(east of north), wind speed, pressure, temperature, timestamp 
    # pull date as datetime object and add to astropy array   
        
      if len(data[i]):
        #print(type(data[i][]), data[i][0])
        date1 = datetime.datetime.strptime(data[i][0], '%Y-%m-%dT%H:%M:%S')
        stamp_date1 = datetime.datetime.timestamp(date1)
        frac_date1 =((stamp_date1/3.154e7)+1970)
        index = int(i-1)
        
        #hum = float(data[i][2])
        #windD = float(data[i][5])
        #windS = float(data[i][6])
        #press = float(data[i][3])
        #temp = float(data[i][4])
        if len(data[i][1]):
            if -1.1<float(data[i][1])<10:
                Tau_data0 = (float(data[i][1]) + .31)/.84 #PWV
                Tau_data1 = (Tau_data0 - .1)/29
        else: Tau_data1 = -1 #PWV
        
        Tau_data+=[Tau_data1]   #PWV_list+=[PWV]  
        
        #hum_list += [hum]
        #windD_list += [windD]
        #windS_list += [windS]
        #press_list += [press]
        #temp_list += [temp]
        dates += [date1] 
        frac_dates += [frac_date1]
        index_list += [index]  

        #if i%10000==0:print(i, data[i])
        
        i+=1
        

elif char=='LMT' or char=='2' or char=='lmt':
    
#import LMT file and read into list called data
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\lmt_radiometer.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    SatCoord==LMTCoord    
    for row in data[1:]:
    # pull date as datetime object and add to astropy array    
        date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
        stamp_date1 = datetime.datetime.timestamp(date1)
        frac_date1 =((stamp_date1/3.154e7)+1970)
        index = int(row[2])
        Tau = float(row[3])
        transmit = math.exp(-Tau)
        
        #add frac_dates
        dates += [date1] 
        index_list += [index]
        frac_dates += [frac_date1]
        Tau_data += [Tau] 
        transmit_list += [transmit]
        
elif char=='SMT' or char=='3' or char=='smt':
    #['09/16/16 09:09', datetime.datetime(2016, 9, 16, 9, 9), 973, 57647.3816, 5.5, 49.0, 522.7, 2.0, 153.0, 0.0, 0.179, 0.0, 2.91, 38.3]
#import LMT file and read into list called data
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\SMT_data.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    SatCoord==SMTCoord
    for row in data:
    # pull date as datetime object and add to astropy array
        if len(row)>4:    
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(row[2])
            #Modjuldate = float(row[3])
            #Temp = float(row[4])
            #relhum = float(row[5])
            #press = float(row[6])
            #windspeed= float(row[7])
            #winddir= float(row[8])
            #raincheck = float(row[9])
            Tau = float(row[10])
            #if len(row)>11:
            #    maxWindSpeed= float(row[11])
            #    WindSpeedAve = float(row[12])  #over 5 readings
            #    if len(row)>13:
            #        tipper_relhum = float(row[13])
            
        
        #if i%1000==0 : print(index)
        
            #transmit = math.exp(-Tau)
        
        #add frac_dates
            dates += [date1] 
            index_list += [index] 
            frac_dates += [frac_date1]
            Tau_data += [Tau] 
            #transmit_list += [transmit]
            i+=1
elif char=='12m' or char=='4' or char=='12M':
   #['09/16/16 23:07', datetime.datetime(2016, 9, 16, 23, 7), 1059, 57647.9638, 28.4, 24.8, 612.2, 1.3, 137.0, 0.0, 0.186, 6.9] 
#import LMT file and read into list called data
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\12M_data_new.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    SatCoord==AROCoord
    for row in data:
    # pull date as datetime object and add to astropy array    
      #if len(row)>4:
       # date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
       # stamp_date1 = datetime.datetime.timestamp(date1)
       # frac_date1 =((stamp_date1/3.154e7)+1970)
       # index = int(row[2])
        #Modjuldate = float(row[3])
        #temp = float(row[4])
        if len(row)<=10:   
            Tau = -1
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(row[2])
            Tau_data += [Tau]
        #if len(row)>5:
        # relhum = float(row[5])
        # if len(row)>6:
        #  press = float(row[6])
        #  if len(row)>7:
        #   windspeed = float(row[7])
        #   if len(row)>8:
        #    winddir = float(row[8])
        #    if len(row)>9:
        #        raincheck = float(row[9])
        elif len(row)>10:
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(row[2])
            Tau = float(row[10])
            Tau_data += [Tau]
                    #if len(row)>11:
                    #    tipper_relhum = float(row[11])
        
        #if i%1000==0 : print(index)
        #transmit = math.exp(-Tau)
        #Tau_data += [Tau]
        #transmit_list += [transmit]
        #add frac_dates
        dates += [date1] 
        index_list += [index] 
        frac_dates += [frac_date1]
        i+=1
        
        
elif char=='all' or char=='6' or char=='All':
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\lmt_radiometer.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    for row in data:
    # pull date as datetime object and add to astropy array    
        date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
        stamp_date1 = datetime.datetime.timestamp(date1)
        frac_date1 =((stamp_date1/3.154e7)+1970)
        index = int(row[2])
        Tau = float(row[3])
        #transmit = math.exp(-Tau)
        
        #add frac_dates
        dates += [date1] 
        index_list += [index]
        frac_dates += [frac_date1]
        Tau_data += [Tau] 
        i+=1
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\GLT_Weather.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    for row in data:  # index, id, timestamp, datetime, datetime, Tau, humidity%, wind Direction(east of north), wind speed, pressure, temperature, timestamp 
    # pull date as datetime object and add to astropy array    
        date1 = datetime.datetime.strptime(row[3], '%m/%d/%y %H:%M')
        stamp_date1 = datetime.datetime.timestamp(date1)
        frac_date1 =((stamp_date1/3.154e7)+1970)
        index = int(i)
        Tau = float(row[5])
       
        dates += [date1] 
        frac_dates += [frac_date1]
        index_list += [index]  
        Tau_data += [Tau] 
        #transmit_list += [transmit]
        i+=1

    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\SMT_data.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    for row in data:
    # pull date as datetime object and add to astropy array
        if len(row)>4:    
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(row[2])
            
            Tau = float(row[10])
           
            dates += [date1] 
            index_list += [index] 
            frac_dates += [frac_date1]
            Tau_data += [Tau]
            i+=1
            
    with open('C:\\USERS\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\12M_data_new.csv', newline = '') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = list(readCSV)

#scroll through data assigning columns to eah data peice
    for row in data:
        if len(row)<=10:   
            Tau = -1
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(row[2])
            Tau_data += [Tau]
       
        elif len(row)>10:
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(row[2])
            Tau = float(row[10])
            Tau_data += [Tau]
                   
        dates += [date1] 
        index_list += [index] 
        frac_dates += [frac_date1]
            #transmit_list += [transmit]
        
#add more telescopes, satelitte coord, and dataframe
            
# save as numpy binary file
#np.save(BinaryAstroData)  #reload w/ np.load(BinaryAstroData)
Npts = len(dates)
print("total datapoints:", Npts, len(Tau_data), "(needs changed to sort for actual dates)1st and last dates are:\n" , dates[0], " and ", dates[Npts-1], 
      "\nplease enter 0 for whole data scatter plot, 1 for yearly two week interval percentile plots or 2 for one two week percentile plot\n",
      "or 3 for hour range percentile over whole year\n")

# choose your plotting option:
choose = int(input())

i=0
if choose == 0:
    fig, axs = plt.subplots()
    
    ###################################
    #   Weather scatter+line plot style 
    ###################################
    figsize=(8,6.5) #size of the figure

    #rcParams['text.usetex']=True
    #rcParams['font.family']='sans-serif'
    #rcParams['font.sans-serif']='Latin Modern Roman'
    """
    # axes and tickmarks
    rcParams['axes.labelsize']=18
    #rcParams['axes.labelweight']=600
    rcParams['axes.linewidth']=1.5

    rcParams['xtick.labelsize']=small
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
    """
    plt.figure(figsize=figsize)            # size of the figure
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize']=16
    plt.rcParams['lines.linewidth']=2.0
    plt.rcParams['lines.markersize']=6
    plt.rcParams['axes.labelsize']=10
    plt.rcParams['axes.labelweight']=600
    plt.rcParams['axes.linewidth']=2.5
    #twin the axes
    #axes2= axs.twinx()
    #new_fixed_axis = axes2.get_grid_helper().new_fixed_axis
    #axes2.axis["right"] = new_fixed_axis(loc="right", axes=axes2)
    #axes2.axis["right"].toggle(all=True)
            #adjust to prompt user for which graph to display
    Tau_list1=[]
    transmit_list1=[]
    frac_dates1=[]
    for i in range(len(Tau_data)):
        if Tau_data[i]!=-1 or Tau_data[i]!=0 or Tau_data[i]<4:
            #transmit_list1+=[transmit_list[i]]
            Tau_list1+=[Tau_data[i]]
            frac_dates1+=[frac_dates[i]]
            #elevation_list+=[sourceElevation(GLTCoord, M87Coord, dates[i])]
    #data=(transmit_list, elevation_list)
    #print(len(frac_dates1),len(elevation_list))
    plt.scatter(frac_dates1, Tau_list1, alpha = .5, s=1.5, color='blue')
    #axs.plot(frac_dates1, elevation_list, label="elevation")
    plt.xlabel('fractional dates')    #('time of day (hr)')
    plt.ylabel('Optical Depth')
    plt.xlim(frac_dates1[0], frac_dates[-1])
    plt.text(1998, 2, char, fontsize=30, horizontalalignment='center', verticalalignment='center')
    plt.ylim(0, 2.5)
    plt.tight_layout()
    plt.show()
    plt.savefig('full_%s_data.png' % char, format='png')


if choose == 1:
    
  #print("please enter start and end hours one after another \n(ex: 0 - 23)\n")
  #DayBegin = int(input())
  #DayEnd = int(input())
  month=1
  day=1
  
  perc1, perc2, perc3 = .25, .5, .75
  weekly_datesShiftday=[]
  weeklyTrans_dataSlice=[]    
  weeklyTau_dataSlice=[]
  weekly_dates=[]
  perc1pts = []
  perc2pts = []
  perc3pts = []
  elevate_fracdates=[]
  
  #add additional loop to go over each 30 min or 15 min interval
     #for minrange in range(1,2): if minrange = 1 minutethresh1 = minutethresh elif ...between 30min and the hour end
    
  for wkcount in range(0,26):
    fig, axs = plt.subplots()
    """
    ###################################
    #   Weather scatter+line plot style 
    ###################################
    #figsize=(8,6.5) #size of the figure

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
    #plt.figure(figsize=figsize)            # size of the figure
    """
    
    for hour in range(0, 24):  #add percentile check for each hour in this loop
            print("iterating through hour: ", hour)
            elevate_fracdates+=[hour]
       #for minthresh in range(1,3): 
       #     if minthresh == 1: minthresh1 = 0, minthresh2 = 30
       #     elif minthresh == 2: minthresh1 = 31, minthresh2 = 59  
            startsort = len(weekly_datesShiftday)           #adjust for fractional dates may be easier
            for i in range(len(dates)):
                startdate = datetime.datetime(int(dates[i].year), month, day, hour=0, minute=0, second=0)  
                nextweek = (startdate + datetime.timedelta(days=14)) 
                Elevate_date = (startdate + datetime.timedelta(days=6, hours=23, minutes=59))
                         #could use one loop inbetween Daybegin and dayend if sorting method is thought of
                if (int(dates[i].hour) == hour and dates[i] >= startdate and dates[i] <= nextweek and Tau_data[i] != -1 and Tau_data[i] < 7): #and int(dates[i].minutes) <= minthresh2 and int(dates[i].minutes >= minthresh1)) : # 30 min intervals by checking minutes threshhold
            
                  #weeklyTrans_dataSlice += [transmit_list[i]]   #weeklyTau_dataSlice += [Tau_data[i]]
                  weeklyTau_dataSlice += [Tau_data[i]]
                  weekly_dates +=[dates[i]] # + timedelta(minutes=30)
                  datesShiftday = datetime.datetime(dates[0].year, month, day, dates[i].hour, dates[i].minute) #shift to same month and day as first entry user selected
                  weekly_datesShiftday += [datesShiftday] 
            
             
       
            sorted_Tau = sorted(weeklyTau_dataSlice[startsort:])#sorted_Tau = sorted(weeklyTau_dataSlice[startsort:])
            if len(sorted_Tau):
                perc3pts += [sorted_Tau[int(len(sorted_Tau)*perc3)]]
                #perc2pts += [sorted_Tau[int(len(sorted_Tau)*perc2)]]   #make sure what you
                perc1pts += [sorted_Tau[int(len(sorted_Tau)*perc1)]]     #are percentiling
    #add check for LMT or GLT coord
    for date in perdelta(Elevate_date, Elevate_date + datetime.timedelta(hours=24), datetime.timedelta(hours=1)):  #minutes = 30
                            
           elevation_list1+= [sourceElevation(SatCoord, M87Coord, date)]
           elevation_list2+= [sourceElevation(SatCoord, SGRACoord, date)]

    if len(perc1pts):          
     print(str(nextweek), len(perc3pts), len(elevation_list1), len(elevation_list2))
     startdate = nextweek
     month = startdate.month
     day = startdate.day
    
     color = 'tab:blue'
     axs.set(title='%s' % str(startdate.date()), xlabel='time(hrs)', ylabel='Optical Depth(Tau)')
     #axs.set_ylabel('Optical Depth(Tau)', color=color) #Optical Depth(Tau)
     axs.grid()
     plt.text(1,1, char)
     axs.plot(perc3pts, color='blue'),  axs.plot(perc1pts, color='green'), #axs.plot(perc2pts, color='yellow'),
     plt.xlim(0, 24)
     plt.ylim(0,1)
    
     axs2=axs.twinx()
     color = 'tab:red'
     axs2.set_ylabel('Elevation (degrees)', color=color)  # we already handled the x-label with ax1
     axs2.plot(elevate_fracdates, elevation_list1, elevate_fracdates, elevation_list2, color=color)
     axs2.tick_params(axis='y', labelcolor=color)
     plt.ylim(0,90)
    
     #text(0.1, .9,'%s' % str(dateUsr.date()), ha='center', va='center', transform=axs.transAxes)
     fig.tight_layout()
     
     fig.savefig('fig%003d.png' % int(wkcount+1), format='png')
     plt.close(fig)
     #fig.clf()
     perc1pts.clear(), perc2pts.clear(), perc3pts.clear(), elevate_fracdates.clear(), elevation_list1.clear(), elevation_list2.clear(),
     weeklyTau_dataSlice.clear(), sorted_Tau.clear(), weeklyTrans_dataSlice.clear(), weekly_datesShiftday.clear(), weekly_dates.clear()
    else: 
        print('No data for interval')
        startdate = nextweek
        month = startdate.month
        day = startdate.day
                                    #keep axis conistent even though no data
        color = 'tab:blue'
        axs.set(title='%s' % str(startdate.date()), xlabel='hours', ylabel='Optical Depth(Tau)')
        axs.set_ylabel('Optical Depth(Tau)', color=color)
        axs.grid()
        axs.plot(perc3pts, color='blue'),  axs.plot(perc1pts, color='green'), #axs.plot(perc2pts, color='yellow'),
        plt.xlim(0, 24)
        plt.ylim(0,1)
    
        axs2=axs.twinx()
        color = 'tab:red'
        axs2.set_ylabel('Elevation (degrees), (no Tau data)', color=color)  # we already handled the x-label with ax1
        axs2.plot(elevate_fracdates, elevation_list1, elevate_fracdates, elevation_list2, color=color)
        axs2.tick_params(axis='y', labelcolor=color)
        plt.ylim(0,90)
        
        fig.tight_layout()
        fig.savefig('fig%003d.png' % int(wkcount+1), format='png')
        plt.close(fig)
        elevate_fracdates.clear(), elevation_list1.clear(), weeklyTau_dataSlice.clear(), elevation_list2.clear(),
        sorted_Tau.clear(), weeklyTrans_dataSlice.clear(), weekly_datesShiftday.clear(), weekly_dates.clear()
if choose == 2:
    fig, axs = plt.subplots()
    ###################################
    #   Weather scatter+line plot style 
    ###################################
    #figsize=(8,6.5) #size of the figure

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
    #plt.figure(figsize=figsize)            # size of the figure
    
    sortedperclist3 = []
    sortedperclist2 = []
    sortedperclist1 = []
    perc1, perc2, perc3 = .25, .5, .75
    weekly_datesShiftday=[]
    weeklyTau_dataSlice=[]
    weeklyTrans_dataSlice=[] 
    weekly_dates=[]
    perc1pts = []
    perc2pts = []
    perc3pts = []
    timepts = []
    elevate_dates=[]
    elevate_fracdates=[]
    elevation_list=[]
    
    print("please enter a start date for a given fortnight out of each year\n")
    month = int(input('Enter a month:\n'))
    day = int(input('Enter a day:\n'))
    print("please enter start and end hours one after another \n(ex: 0 - 23)\n")
    DayBegin = int(input())
    DayEnd = int(input())
    print("\n\n")
    
    for hour in range(DayBegin, DayEnd):
        #add additional loop to go over each 30 min or 15 min interval
        #for minrange in range(1,2): if minrange = 1 minutethresh1 = 30 elif ...between 30min and the hour end
              #also using frac_dates may be easier
        #for minthresh in range(1,3): 
        #    if minthresh == 1: minthresh1 = 0, minthresh2 = 30
        #    elif minthresh == 2: minthresh1 = 31, minthresh2 = 59
            startsort = len(weekly_datesShiftday)           
            for i in range(len(dates)):
                dateUsr = datetime.datetime(int(dates[i].year), month, day, hour=0, minute=0, second=0)  
                nextweek = (dateUsr + datetime.timedelta(days=14))
                #Elevate_date1 = (dateUsr + datetime.timedelta(days=7, hours=23, minutes=59))
                #Elevate_date2 = (dateUsr + datetime.timedelta(days=9))
                Elevate_date = (dateUsr + datetime.timedelta(days=6, hours=23, minutes=59))
                         #could use one loop inbetween Daybegin and dayend if sorting method is thought of
                if (int(dates[i].hour) == hour and dates[i] >= dateUsr and dates[i] <= nextweek and Tau_data[i] != -1 and Tau_data[i] < 5):   # and int(dates[i].minute) <= minthresh2 and int(dates[i].minute >= minthresh1)) : # 30 min intervals by checking minutes threshhold
            
                    weeklyTrans_dataSlice += [transmit_list[i]]
                    weeklyTau_dataSlice += [Tau_data[i]]
                    weekly_dates +=[dates[i]]
                #dates1Shiftweek = datetime.datetime(dates[0].year, dates[i].month, dates[i].day, dates[i].hour, dates[i].minute)
                #weekly_datesShiftweek += [dates1Shiftweek]  
                    datesShiftday = datetime.datetime(dates[0].year, month, day, dates[i].hour, dates[i].minute) #shift to same month and day as first entry user selected
                
                    stamp_date2 = datetime.datetime.timestamp(datesShiftday)
                    frac_date2 = ((stamp_date2/3.154e7)+1970)
                
                    frac_hour = (datesShiftday.hour/24)
                
                    weekly_datesShiftday += [datesShiftday]     
                        #capture middle day's elevation data
                    #if dates[i]>Elevate_date1 and dates[i] < Elevate_date2:
                    #elevation_list+=[sourceElevation(GLTCoord, M87Coord, dates[i])]
                    
                       #elevate_dates+=[datesShiftday]
                
                
            #elevation_list1+= [sourceElevation(GLTCoord, M87Coord, elevate_dates[-5])]
            #elevation_list2+= [sourceElevation(GLTCoord, SGRACoord, elevate_dates[-5])]
        
            elevate_fracdates+=[hour]
            print("iterating through hour:", hour) #Tau data not sorted minutely, ~60 pts for each hour 
        
        #sort and find max and length of percentage list
            sorted_Tau = sorted(weeklyTau_dataSlice[startsort:])
            perc3pts += [sorted_Tau[int(len(sorted_Tau)*perc3)]]
            perc2pts += [sorted_Tau[int(len(sorted_Tau)*perc2)]]   #make sure what you
            perc1pts += [sorted_Tau[int(len(sorted_Tau)*perc1)]]     #are percentiling
        #timepts += [frac_dates[(int((startsort+len(sorted_Tau)/2)-1))]]
            numindex = len(weeklyTau_dataSlice[startsort:])
    for date in perdelta(Elevate_date, Elevate_date + datetime.timedelta(hours=23), datetime.timedelta(hours=1)): #minutes=30
                            
           elevation_list1+= [sourceElevation(LMTCoord, M87Coord, date)]
           elevation_list2+= [sourceElevation(LMTCoord, SGRACoord, date)]
           
    color = 'tab:blue'
    axs.set(title='%s' % str(dateUsr.date()), xlabel='hours', ylabel='Optical Depth(Tau)')
    axs.set_ylabel('Optical Depth(Tau)', color=color)
    axs.grid()
    plt.text(1,1, char)
    axs.plot(perc3pts, color='blue'), axs.plot(perc2pts, color='yellow'), axs.plot(perc1pts, color='green')
    plt.xlim(0, (DayEnd+1))
    plt.ylim(0,1)
    
    axs2=axs.twinx()
    color = 'tab:red'#, tab:orange'
    axs2.set_ylabel('Elevation (degrees)', color=color)  # we already handled the x-label with ax1
    axs2.plot(elevate_fracdates, elevation_list1, elevate_fracdates, elevation_list2, color=color)
    axs2.tick_params(axis='y', labelcolor=color)
    plt.ylim(0,90)
    
    #text(0.1, .9,'%s' % str(dateUsr.date()), ha='center', va='center', transform=axs.transAxes)
    fig.tight_layout()
    plt.show()
    plt.savefig("Weekly_%s_weather_data.png"  % str(dateUsr.date()), format='png')
    
if choose == 3:
    
    fig, axs = plt.subplots()
   
    sortedperclist3=[]
    sortedperclist2=[]
    sortedperclist1=[]
    perc3pts=[]
    perc2pts=[]
    perc1pts=[]
    perc1, perc2, perc3 = .25, .5, .75
    dates_Slice=[]
    Tau_Slice=[]
    
    print("please enter start and end hours one after another \n(ex: 0 - 23)\n")
    DayBegin = int(input())
    DayEnd = int(input())
    print("\n\n")
    
    for hour in range(DayBegin, DayEnd):
         for months in range(1,13)	:
                 print("iterating through month: ", months)
             #for minthresh in range(1,3): 
             #    if minthresh == 1: minthresh1 = 30
             #    elif minthresh == 2: minthresh1 = 59
                 startsort = len(dates_Slice)
                 for i in range(len(dates)):
                     if (int(dates[i].hour) == hour and Tau_data[i] != -1 and 
                         dates[i].month == months and Tau_data[i] < 7): #and int(dates[i].minute) <= minthresh1):
                         Tau_Slice += [Tau_data[i]]
                         dates_Slice += [dates[i]] 
                 sorted_Tau = sorted(Tau_Slice[startsort:])
                 if len(sorted_Tau):
                    perc3pts += [sorted_Tau[int(len(sorted_Tau)*perc3)]]
                    perc2pts += [sorted_Tau[int(len(sorted_Tau)*perc2)]]   
                    perc1pts += [sorted_Tau[int(len(sorted_Tau)*perc1)]]
        
    axs.grid()    
    axs.plot(perc3pts, color='blue'),  axs.plot(perc1pts, color='green'), axs.plot(perc2pts, color='yellow')
    
    plt.xlabel('Month of Year')
    #matplotlib.axes.Axes.set_xticklabels(self, labels = hrstr)   #check
    #axs.set_xticklabels(np.arange(DayBegin, DayEnd))
    plt.ylabel('Optical Depth')
    plt.text(1,1, char + ' hours:\n' + str(DayBegin) + ' to ' + str(DayEnd))
    plt.axis([0,12, 0, 1.5])
    #set xticklabels
    labels = [item.get_text() for item in axs.get_xticklabels()]
    labels[0], labels[1], labels[2], labels[3], labels[4], labels[5], labels[6] = 'Jan', 'Mar', 'May', 'Jun', 'Aug', 'Nov', 'Dec'
    #labels[0], labels[1], labels[2], labels[3] = 'Jan', 'Feb', 'Mar', 'Apr'
    #labels[4], labels[5], labels[6], labels[7], labels[8] = 'May', 'Jun', 'Jul', 'Aug', 'Sept'
    #labels[9], labels[10], labels[11] = 'Oct', 'Nov', 'Dec',
    axs.set_xticklabels(labels)
    fig.tight_layout()
    plt.show()    #mpld3.show()    #web check
    #plt.savefig("Weekly_%7.8f_weather_data.pdf" % x) adjust for datetime's  
    
    
    
    
if choose == 4:
    
    fig, axs = plt.subplots()
    
    Tau_1=[]
    Tau_2=[]
    dates1=[]
    dates2=[]
    frac_dates1=[]
    frac_dates2=[]
    
    print("enter character for other dataset to be graphed against")
    print("please select GLT, LMT, SMT, 12m, Apex, or all data:")
    char2 = str(input())

    if char2=='GLT' or char2=='1' or char2=='glt':
    
        #import file and read into list called data
        with open('/Users/DaltonGlove/Desktop/PIRE_research/data_CSVs/GLT_Weather.csv', newline = '') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            data = list(readCSV)

    #scroll through data assigning columns to eah data peice
        for row in data:  # index, id, timestamp, datetime, datetime, Tau, humidity%, wind Direction(east of north), wind speed, pressure, temperature, timestamp 
            # pull date as datetime object and add to astropy array    
            date1 = datetime.datetime.strptime(row[3], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(i)
            Tau = float(row[5])
 #hum = int(row[6])windD = int(row[7])windS = float(row[8])press = float(row[9])temp = float(row[10])#transmit = math.exp(-Tau)
            
 #hum_list += [hum]#windD_list += [windD]#windS_list += [windS]#press_list += [press]#temp_list += [temp]
            dates2 += [date1] 
            frac_dates2 += [frac_date1]
            index_list += [index]  
            Tau_2 += [Tau] 
            transmit_list += [transmit]
            i+=1
            

    if char2=='APEX' or char2=='5' or char2=='apex' or char2=='Apex':
    
#import file and read into list called data
        with open('/Users/DaltonGlove/Desktop/PIRE_research/data_CSVs/Apex_radiometer.csv', newline = '') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            data = list(readCSV)

        i=2
        while i< len(data)-6:  # index, id, timestamp, datetime, datetime, Tau, humidity%, wind Direction(east of north), wind speed, pressure, temperature, timestamp    
             if len(data[i]):

                date1 = datetime.datetime.strptime(data[i][0], '%Y-%m-%dT%H:%M:%S')
                stamp_date1 = datetime.datetime.timestamp(date1)
                frac_date1 =((stamp_date1/3.154e7)+1970)
                index = int(i-1)
        #hum = float(data[i][2]) #windD = float(data[i][5]) #windS = float(data[i][6]) #press = float(data[i][3]) #temp = float(data[i][4])
                if len(data[i][1]):
                    if -1.1<float(data[i][1])<10:
                        Tau_data1 = float(data[i][1]) #PWV
                else: Tau_data1 = -1 #PWV
        
                Tau_2+=[Tau_data1]   #PWV_list+=[PWV]  
         #hum_list += [hum] #windD_list += [windD] #windS_list += [windS] #press_list += [press] #temp_list += [temp]
                dates2 += [date1] 
                frac_dates2 += [frac_date1]
                index_list += [index]  
                
                i+=1

    elif char2=='LMT' or char2=='2' or char2=='lmt':
    
#import LMT file and read into list called data
        with open('/Users/DaltonGlove/Desktop/PIRE_research/data_CSVs/lmt_radiometer.csv', newline = '') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            data = list(readCSV)

#scroll through data assigning columns to eah data peice
        for row in data:
    # pull date as datetime object and add to astropy array    
            date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
            stamp_date1 = datetime.datetime.timestamp(date1)
            frac_date1 =((stamp_date1/3.154e7)+1970)
            index = int(row[2])
            Tau = float(row[3])
            #transmit = math.exp(-Tau)
        
        #add frac_dates
            dates2 += [date1] 
            index_list += [index]
            frac_dates2 += [frac_date1]
            Tau_2 += [Tau] 
            #transmit_list += [transmit]
        
    elif char2=='SMT' or char2=='3' or char2=='smt':
    #['09/16/16 09:09', datetime.datetime(2016, 9, 16, 9, 9), 973, 57647.3816, 5.5, 49.0, 522.7, 2.0, 153.0, 0.0, 0.179, 0.0, 2.91, 38.3]
#import LMT file and read into list called data
        with open('/Users/DaltonGlove/Desktop/PIRE_research/data_CSVs/SMT_data.csv', newline = '') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            data = list(readCSV)

#scroll through data assigning columns to eah data peice
        for row in data:
    # pull date as datetime object and add to astropy array
            if len(row)>4:    
                date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
                stamp_date1 = datetime.datetime.timestamp(date1)
                frac_date1 =((stamp_date1/3.154e7)+1970)
                index = int(row[2])
            #Modjuldate = float(row[3])
            #Temp = float(row[4])
            #relhum = float(row[5])
            #press = float(row[6])
            #windspeed= float(row[7])
            #winddir= float(row[8])
            #raincheck = float(row[9])
                Tau = float(row[10])
            #if len(row)>11:
            #    maxWindSpeed= float(row[11])
            #    WindSpeedAve = float(row[12])  #over 5 readings
            #    if len(row)>13:
            #        tipper_relhum = float(row[13])
                dates2 += [date1] 
                index_list += [index] 
                frac_dates2 += [frac_date1]
                Tau_2 += [Tau] 
            #transmit_list += [transmit]
                i+=1
    elif char2=='12m' or char2=='4' or char2=='12M':
   #['09/16/16 23:07', datetime.datetime(2016, 9, 16, 23, 7), 1059, 57647.9638, 28.4, 24.8, 612.2, 1.3, 137.0, 0.0, 0.186, 6.9] 
#import LMT file and read into list called data
        with open('/Users/DaltonGlove/Desktop/PIRE_research/data_CSVs/12M_data_new.csv', newline = '') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            data = list(readCSV)

#scroll through data assigning columns to eah data peice
        for row in data:
   
            if len(row)<=10:   
                Tau = -1
                date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
                stamp_date1 = datetime.datetime.timestamp(date1)
                frac_date1 =((stamp_date1/3.154e7)+1970)
                index = int(row[2])
                Tau_2 += [Tau]
        #if len(row)>5:
        # relhum = float(row[5])
        # if len(row)>6:
        #  press = float(row[6])
        #  if len(row)>7:
        #   windspeed = float(row[7])
        #   if len(row)>8:
        #    winddir = float(row[8])
        #    if len(row)>9:
        #        raincheck = float(row[9])
            elif len(row)>10:
                date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
                stamp_date1 = datetime.datetime.timestamp(date1)
                frac_date1 =((stamp_date1/3.154e7)+1970)
                index = int(row[2])
                Tau = float(row[10])
                Tau_2 += [Tau]
                    #if len(row)>11:
                    #    tipper_relhum = float(row[11])
            dates2 += [date1] 
            index_list += [index] 
            frac_dates2 += [frac_date1]
            i+=1
