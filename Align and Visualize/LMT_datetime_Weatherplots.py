#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 01:06:57 2019

@author: DaltonGlove

/anaconda3/lib/python3.7/site-packages/pandas/plotting/_converter.py:129:
FutureWarning: Using an implicitly registered datetime converter for a matplotlib plotting method. The converter was registered by pandas on import. Future versions of pandas will require you to explicitly register matplotlib converters.

To register the converters:
    >>>from pandas.plotting import 
register_matplotlib_converters
    >>>register_matplotlib_converters()
warnings.warn(msg, FutureWarning)
  
"""
import csv
import numpy as np
import matplotlib.pyplot as plt, mpld3
import matplotlib
import datetime
from matplotlib import rcParams       # import to change plot parameters
#import pandas as pd


"""
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

"""



#define index grabbing func for datetime
def where_date(items, pivot):
    time_diff = np.abs([date - pivot for date in items])
    return time_diff.argmin(0)

def nearest_date(items,pivot):
    nearest=min(items, key=lambda x: abs(x - pivot))
    timedelta = abs(nearest - pivot)
    return nearest, timedelta

  #initialize colomuns of data
dates = []
index_list = []
Tau_data = []
matplotDates = []
 
#import file and read into list called data
with open('/Users/DaltonGlove/Desktop/lmt_radiometer.csv', newline = '') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    data = list(readCSV)

#scroll through data assigning columns to eah data peice
for row in data:
    # pull date as datetime object and add to astropy array    
    date1 = datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M')
    index = int(row[2])
    Tau = float(row[3])
        
    dates += [date1] #np.append(datesJuls, dateJul)
    index_list += [index] #np.append(index_list, index)
    Tau_data += [Tau] #np.append(Tau_data, Tau)
    
Npts = len(dates)
print("total datapoints:", Npts, "1st and last dates are:\n" , dates[0], " and ", dates[Npts-1], "\nplease enter 0 for whole data scatplot, 1 for yearly two week percent_plot or 2 for one two week percent_plot\n")

# save as numpy binary file
#np.save(BinaryAstroData)  #reload w/ np.load(BinaryAstroData)

# choose your plotting option:
choose = int(input())
#plot all/yearly
#fig, axs = plt.subplots()

if choose == 0:
    fig, axs = plt.subplots()
    
    
    dates = [pd.to_datetime(d) for d in dates]
    
    #x_ax = []
    
    #for i in range(len(dates)) :
        
     #  matplotDate = matplotlib.dates.date2num(dates[i])  #datestr
     #  matplotDates += [matplotDate]
       
     #  x_ax += [i]
    
    
    plt.scatter(dates, Tau_data, alpha = .5)
    #plt.plot_date(matplotDates, Tau_data, alpha=.5)
    #axs.plot(perc3pts, 'b'), axs.plot(perc2pts, 'b'), axs.plot(perc1pts, 'b')
    plt.xlabel('all year dates')    #('time of day (hr)')
    plt.ylabel('Optical Depth')
    plt.axis([0, 24, 0, 2])
    #plt.ylim(0, 2)
    plt.show()
    #stringdate = startdate.strftime("%Y-%m-%d")
    #plt.savefig('Year_weather_data.png', format='png')

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

if choose == 1:
  	
   #fig, axs = plt.subplots()
    
   print("please enter start and end hours one after another \n(ex: 0 - 23)\n")
   DayBegin = int(input())
   DayEnd = int(input()) 
   hrstr = []
   weeklyTau_dataSlice = []
   weekly_dates = []
   weekly_datesShiftweek = []
   weekly_datesShiftday = []   

   percTauday_list = []
   perc1, perc2, perc3 = .25, .5, .75
   percdates =[]
    
   datesTau = []
   percDatesTau = []
   matplotdates3 = []
   matplotdates2 = []
   matplotdates1 = []
   percmatplotdates = []
   sortedperclist3 = []
   sortedperclist2 = []
   sortedperclist1 = []
   
   unsortedperc3Tau = []
   unsortedperc3Time = []
   unsortedperc2Tau = []
   unsortedperc2Time = []
   unsortedperc1Tau = []
   unsortedperc1Time = []
    
   hrstr = []
    
   perc1pts = []
   perc2pts = []
   perc3pts = []
    
   minthresh1 = 29
   minthresh2 = 59
   month=1
   day=1
   # currently orders hourly data so hours are next to eachother, adjust to have range of hours for each year next to eachother if faster and not effective to the data
   	
   weeksarr=[]
   weekstauarr = []
   
   
    #initialize 26 length array and each weeks data is an element
   #for i in range(1,26):
        #weeksarr += [[]]
        #weekstauarr += [[]]
    #52 weeks in a year so that is 26 two week plots
    	# 14 is optimal day range only neglecting ~1 day of the year from data
   for wkcount in range(0,25):
     fig, axs = plt.subplots() 
     for hour in range(DayBegin, DayEnd):  #add percentile check for each hour in this loop
       
       print(hour)
       hrstr += [str(hour)]
        
       #add additional loop to go over each 30 min or 15 min interval
       #for minrange in range(1,2): if minrange = 1 minutethresh1 = minutethresh elif ...between 30min and the hour end
        
       startsort = len(weekly_datesShiftday)           
       for i in range(len(dates)):
           startdate = datetime.datetime(int(dates[i].year), month, day, hour=0, minute=0, second=0)  
           nextweek = (startdate + datetime.timedelta(days=14)) 
          
                         #could use one loop inbetween Daybegin and dayend if sorting method is thought of
           if (int(dates[i].hour) == hour and dates[i] >= startdate and dates[i] <= nextweek) : # 30 min intervals by checking minutes threshhold
            
               weeklyTau_dataSlice += [Tau_data[i]]
               weekly_dates +=[dates[i]]
                #dates1Shiftweek = datetime.datetime(dates[0].year, dates[i].month, dates[i].day, dates[i].hour, dates[i].minute)
                #weekly_datesShiftweek += [dates1Shiftweek]  
               datesShiftday = datetime.datetime(dates[0].year, month, day, dates[i].hour, dates[i].minute) #shift to same month and day as first entry user selected
               weekly_datesShiftday += [datesShiftday] 
               matplotDate = matplotlib.dates.date2num([datesShiftday])
               matplotDates += [matplotDate]
       sorted_Tau = sorted(weeklyTau_dataSlice[startsort:])
       #sortedperclist3 += sorted_Tau[:int(len(sorted_Tau)*perc3)]
       #sortedperclist2 += sorted_Tau[:int(len(sorted_Tau)*perc2)]
       #sortedperclist1 += sorted_Tau[:int(len(sorted_Tau)*perc1)]
       thresh3 = max(sorted_Tau[:int(len(sorted_Tau)*perc3)])
       thresh2 = max(sorted_Tau[:int(len(sorted_Tau)*perc2)])
       thresh1 = max(sorted_Tau[:int(len(sorted_Tau)*perc1)])
       perc1pts += [thresh1]
       perc2pts += [thresh2]
       perc3pts += [thresh3]
       print(thresh1, thresh2, thresh3, "\n") 
     #weeksarr[wkcount] += weekly_datesShiftday
     #weekstauarr[wkcount] += weeklyTau_dataSlice           
     print(nextweek)
     startdate = nextweek
     month = startdate.month
     day = startdate.day
    
   #for i in range(0,25): plt.scatter(weeksarr[i], weekstauarr[i], alpha =.5)
     #plt.scatter(weekly_datesShiftday, weeklyTau_dataSlice, alpha = .5)
     #plt.plot_date(matplotDates, weeklyTau_dataSlice, alpha=.5)
     axs.plot(perc3pts, 'b'), axs.plot(perc2pts, 'b'), axs.plot(perc1pts, 'b')
     plt.xlabel('time of day (hr)')
     plt.ylabel('Optical Depth')
     plt.axis([0, 24, 0, 1.5])
     #plt.show()                                    #use fractional year from timestamp for better dates axis
     #stringdate = startdate.strftime("%Y-%m-%d")
     fig.savefig('Yearly_weather_data_week_%s.png' % str(startdate.date()), format='png')
     #plt.close(fig)
     #fig.clf()
     perc1pts.clear(), perc2pts.clear(), perc3pts.clear()
     
     
# plot weekly grab
elif choose == 2:
    
    fig, axs = plt.subplots()
    
    print("please enter a start date for a given fortnight out of each year\n")
    month = int(input('Enter a month:\n'))
    day = int(input('Enter a day:\n'))
    print("please enter start and end hours one after another \n(ex: 0 - 23)\n")
    DayBegin = int(input())
    DayEnd = int(input())
    print("\n\n")
    
    percTauday_list = []
    perc1, perc2, perc3 = .25, .5, .75
    percdates =[]
    
    datesTau = []
    percDatesTau = []
    matplotdates3 = []
    matplotdates2 = []
    matplotdates1 = []
    percmatplotdates = []
    sortedperclist3 = []
    sortedperclist2 = []
    sortedperclist1 = []
    
    weeklyTau_dataSlice = []
    weekly_dates = []
    weekly_datesShiftweek = []
    weekly_datesShiftday = []
    
    unsortedperc3Tau = []
    unsortedperc3Time = []
    unsortedperc2Tau = []
    unsortedperc2Time = []
    unsortedperc1Tau = []
    unsortedperc1Time = []
    
    hrstr = []
    
    perc1pts = []
    perc2pts = []
    perc3pts = []
    
    minthresh1 = 29
    minthresh2 = 59
    
    #~~~~
    #this two weeks extracts unsorted lower percentile of data while iterating through, could be faster to not since it is unneeded to have those points
    # or change to only take percentile pts and not arrays
    #~~~~
    
    # grab sorted week from start index to end for date
            #loops same number of times as hour range, could change to func of finding indexs, but start and end would be doubling the times looped through data plus calling functions
    for hour in range(DayBegin, DayEnd):
        hrstr += [str(hour)]
        
        #add additional loop to go over each 30 min or 15 min interval
        #for minrange in range(1,2): if minrange = 1 minutethresh1 = minutethresh elif ...between 30min and the hour end
        
        
        startsort = len(weekly_datesShiftday)           
        for i in range(len(dates)):
            dateUsr = datetime.datetime(int(dates[i].year), month, day, hour=0, minute=0, second=0)  
            nextweek = (dateUsr + datetime.timedelta(days=14))
                         #could use one loop inbetween Daybegin and dayend if sorting method is thought of
            if (int(dates[i].hour) == hour and dates[i] >= dateUsr and dates[i] <= nextweek) : # 30 min intervals by checking minutes threshhold
            
                weeklyTau_dataSlice += [Tau_data[i]]
                weekly_dates +=[dates[i]]
                #dates1Shiftweek = datetime.datetime(dates[0].year, dates[i].month, dates[i].day, dates[i].hour, dates[i].minute)
                #weekly_datesShiftweek += [dates1Shiftweek]  
                datesShiftday = datetime.datetime(dates[0].year, month, day, dates[i].hour, dates[i].minute) #shift to same month and day as first entry user selected
                weekly_datesShiftday += [datesShiftday]     
                         #convert dates to matplotlib date format
                #matplotDate = matplotlib.dates.date2num(datesShiftday)
                #matplotdates += [matplotDate]         
        print(len(weekly_datesShiftday)) #Tau data not sorted minutely, ~60 pts for each hour 
        
        #sort and find max and length of percentage list
        sorted_Tau = sorted(weeklyTau_dataSlice[startsort:])
        sortedperclist3 += sorted_Tau[:int(len(sorted_Tau)*perc3)]
        sortedperclist2 += sorted_Tau[:int(len(sorted_Tau)*perc2)]
        sortedperclist1 += sorted_Tau[:int(len(sorted_Tau)*perc1)]
        thresh3 = max(sortedperclist3)
        thresh2 = max(sortedperclist2)
        thresh1 = max(sortedperclist1)
        perc1pts += [thresh1]
        perc2pts += [thresh2]
        perc3pts += [thresh3]
        numindex = len(weeklyTau_dataSlice[startsort:])
        
        for i in range(startsort, len(weeklyTau_dataSlice)):
            if weeklyTau_dataSlice[i] <= thresh3:
                    #loop through unsorted tau data adding each that would be in the sorted percentage list with corresponding datetime
                unsortedperc3Tau += [weeklyTau_dataSlice[i]]
                unsortedperc3Time += [weekly_datesShiftday[i]]
                
                matplotDate = matplotlib.dates.date2num(weekly_datesShiftday[i])
                matplotdates3 += [matplotDate]
                
            elif weeklyTau_dataSlice[i] <= thresh2:
                
                unsortedperc2Tau += [weeklyTau_dataSlice[i]]
                unsortedperc2Time += [weekly_datesShiftday[i]]
                
                matplotDate = matplotlib.dates.date2num(weekly_datesShiftday[i])
                matplotdates2 += [matplotDate]
            
            elif weeklyTau_dataSlice[i] <= thresh1:
                
                unsortedperc1Tau += [weeklyTau_dataSlice[i]]
                unsortedperc1Time += [weekly_datesShiftday[i]]
                
                matplotDate = matplotlib.dates.date2num(weekly_datesShiftday[i])
                matplotdates1 += [matplotDate]
            

    axs.plot(perc3pts, 'b'), axs.plot(perc2pts, 'b'), axs.plot(perc1pts, 'b')
    #axs.scatter()
    axs.set(title='weekly', xlabel='Dates', ylabel='Absorbance(Tau)')
    axs.grid()
    #plt.savefig("Weekly_%7.8f_weather_data.pdf" % x)
#plt.xticks(np.arange(DayBegin, DayEnd))  #adjust ticks 
#plt.show() #line plotting
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #scat plotting  
    #axs.scatter(unsortedpercTime, unsortedpercTau, alpha = .5)
    #plt.title('perc biweekly scatt plot')
    plt.xlabel('time of day (hr)')
    #matplotlib.axes.Axes.set_xticklabels(self, labels = hrstr)   #check
    #axs.set_xticklabels(np.arange(DayBegin, DayEnd))
    plt.ylabel('Optical Depth')
    plt.text(1,1, str(day) + '/' + str(month))
    plt.axis([0,24, 0, 1.5])
    plt.show()    #mpld3.show()    #web check
    #plt.savefig("Weekly_%7.8f_weather_data.pdf" % x) adjust for datetime's  