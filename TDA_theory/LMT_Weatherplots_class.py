#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 01:45:17 2019

@author: DaltonGlove
"""
#filtration global analysis of extrema for timeseries unfruitful, adjust for cleasened data

import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import ripser
import persim
import persim.plot
from scipy import fftpack

def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]

  #initialize colomuns of data
dates1 = []
dates2 = []
datesJuls1 = []
datesJuls2 = []
time = []
index_list = []
cutoff_index = []
Tau_data1 = []
Tau_data2 = []
datesTau = []
diffTau = [] 

thresh = float(input('please enter thresholding value of Tau(normally: 5): \n' ))


i = 1
#import file and read into list called data

# change to correct directory
with open('/Users/DaltonGlove/Desktop/testdata1_2.csv', newline = '') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    data = list(readCSV)   
#print(data)
#f = open('file.csv', 'r', newline = '')
#scroll through list of data assigning columns to eah data peice
for row in data:
            #dateJul = float(row[0])
            #index = int(float(row[1]))
            Tau1 = float(row[2])
            Tau2 = float(row[5])
            
            Tau_data1 += [float(row[2])]
            datesJuls1 += [float(row[0])]
            Tau_data2 += [float(row[5])]
            datesJuls2 += [float(row[3]) - 365.]
            index_list += [i]
            
            diffTau += [Tau1 - Tau2]
            
            i+=1   
Npts1 = len(datesJuls1)
Npts2 = len(datesJuls2)
print("length of data arrays:\n", Npts1, Npts2, '\n')
i = 0
# Thresholding values for persistence diagram computations
for i in range(Npts1):
    if Tau_data1[i] > thresh :
        Tau_data1[i]=thresh
    if Tau_data2[i] > thresh :
        Tau_data2[i]=thresh
    i+=1
# average sections of data to smooth out
aveTau1 = []
stepNpts = 250
timeSlices1 = []
aveTau2 = []
timeSlices2 = []
AveDiffTau = []

i=0
while i < Npts1 : 
    if (i+stepNpts) < Npts1 :
        aveTau1 += [sum(Tau_data1[i:i+stepNpts])/stepNpts]
        timeSlices1 += [datesJuls1[i+int(stepNpts/2)]]
        
        AveDiffTau +=[sum(diffTau[i:i+stepNpts])/stepNpts]
    i+=stepNpts
i=0
while i < Npts2: 
    if (i+stepNpts) < Npts2 :         
        aveTau2 += [sum(Tau_data2[i:i+stepNpts])/stepNpts]
        timeSlices2 += [datesJuls2[i+ int(stepNpts/2)]]
    i+=stepNpts
print("length of averages data arrays:\n", len(timeSlices2), len(timeSlices1), '\n')       

# combine data into 2D arrays
    
datesTau2 = np.array((timeSlices2, aveTau2))
datesTau2 = datesTau2.T

datesTau1 = np.array((timeSlices1, aveTau1))
datesTau1 = datesTau1.T

###################################################################
#align data together by year based on frequency

# abondon ship for this method

#freqs = []
#Npoints = len(Tau_data1)
#SamplePeriod = datesJuls1[-1] - datesJuls1[0]
#SampleRate = Npoints/SamplePeriod
#Yf = fftpack.fft(Tau_data1)

#freqs = fftpack.fftfreq(len(Tau_data1)) * SampleRate

# add these lines to plotting area
    #axs.stem(freqs, np.abs(Yf))
    #axs.set_xlim(-SampleRate / 2, SampleRate / 2)
    #axs.set_xlim(0, 2)
###################################################################

# Statistics comparison: 

# Covariance matrix with diagnal as variance
# variance: spread of data around it's mean
# covariance: directional relation of 2 randvars
print("(Co)Variance matrix: \n", np.cov(aveTau1, aveTau2))

###################################################################
# Persistent homology comparisons:  
#will need to have ripser and Cython package installed
# lower star filtration and bottleneck comparison

dgm1 = ripser.lower_star_img(datesTau1)
dgm2 = ripser.lower_star_img(datesTau2)
#for x in dgm1:print(x)
#print("\n\n\n")
#for y in dgm2:print(y) 

#persim.plot_diagrams(dgm2, show=True)
#persim.plot_diagrams(dgm1, show=True)

#print(d, (matching, D))
d, (matching, D) = persim.bottleneck(dgm1, dgm2, matching=True)
persim.plot.bottleneck_matching(dgm1, dgm2, matching, D, labels=['1st $H_1$', '2nd $H_1$'])
plt.title("Distance {:.3f}".format(d))

#print(persim.sliced_wasserstein(dgm1, dgm2, M=50))

#######################################################################################################
    #plot of data
 
# choose if plot is year or a week
choose = 0

fig, axs = plt.subplots()


if choose == 1:

    """    
    print("(Co)Variance matrix: \n", np.cov(aveTau1, aveTau2))

    dgm1 = ripser.lower_star_img(datesTau1)
    dgm2 = ripser.lower_star_img(datesTau2)
    
    d, (matching, D) = persim.bottleneck(dgm1, dgm2, matching=True)
    persim.plot.bottleneck_matching(dgm1, dgm2, matching, D, labels=['1st $H_1$', '2nd $H_1$'])
    plt.title("Distance {:.3f}".format(d))
    """

    axs.plot(timeSlices1, aveTau1, timeSlices2, aveTau2)    
    axs.set_xlabel('time')
    axs.set_ylabel('average of year')
    axs.grid(True)

    fig.tight_layout()

    # threshold by plot 
    #plt.ylim(0, thresh)
    
    #plt.savefig('Yearly_weather_data.png')



# plot a week of data chosen by user
else:

# input for julian date
    print("please enter a start date and time for a given week in the Julian date format:\n*note that if date is before earliest in data file it will not run*\n")
    x = float(input())

# add 7 for next week
    nextweek = float(x + 7.)
    print ("\nthe start and end date and time in Julian is:\n" , x, nextweek)

# find starting index value of data
    start = 0.
    end = 7.
    
    #startarr, = (find_nearest(datesJuls1, x))
    #endarr, = (np.where(datesJuls1 == nextweek))
    start = min(range(len(datesJuls1)), key =lambda i: abs(datesJuls1[i] - x))    #startarr[0]
    end =  min(range(len(datesJuls1)), key =lambda i: abs(datesJuls1[i] - nextweek))    #endarr[0]
    print("\nstart and end index's of data list is: \n", start, end)    
    j=start
    i=0
    weekly_data_list1 = []
    weekly_Tau1 = []
    weekly_data_list2 = []
    weekly_Tau2 = []
    weeklydiffTau = []
    # grab week from start index to end date
    for i in range(7):
   
        weekly_data1 = datesJuls1[j] 
        weekly_data2 = datesJuls2[j] - 365.
        j += 1
          
        weekly_data_list1 +=  [weekly_data1]
        weekly_Tau1 += [Tau_data1[j]]
        weekly_data_list2 +=  [weekly_data2]
        weekly_Tau2 += [Tau_data2[j]]
        weeklydiffTau += [(Tau_data1[j] - Tau_data2[j])]
        
    # print(weekly_data_list, weekly_Tau)
    Npts1 = len(weekly_data_list1)
    Npts2 = len(weekly_data_list2)
    print("length of weekly data arrays:\n", Npts1, Npts2, '\n')

    # average weekly data
    
    weekaveTau1 = []
    weekstepNpts = 100
    weektimeSlices1 = []
    weekaveTau2 = []
    weektimeSlices2 = []
    weekAveDiffTau = []

    i=0
    
    
    while i < Npts1 : 
        if (i+stepNpts) < Npts1 :
            weekaveTau1 += [sum(weekly_Tau1[i:i+stepNpts])/stepNpts]
            weektimeSlices1 += [weekly_data_list1[i+int(stepNpts/2)]]
        
            weekAveDiffTau +=[sum(weeklydiffTau[i:i+stepNpts])/stepNpts]
        i+=stepNpts
    i=0
    while i < Npts2: 
        if (i+stepNpts) < Npts2 :         
            weekaveTau2 += [sum(weekly_Tau2[i:i+stepNpts])/stepNpts]
            weektimeSlices2 += [weekly_data_list2[i+ int(stepNpts/2)]]
        i+=stepNpts
    print("length of averages data arrays:\n", len(weektimeSlices2), len(weektimeSlices1), '\n')       

 # weekly stats and homology
 
    print("(Co)Variance matrix: \n", np.cov(weekaveTau1, weekaveTau2))
    
    weekdatesTau2 = np.array((weektimeSlices2, weekaveTau2))
    weekdatesTau2 = weekdatesTau2.T

    weekdatesTau1 = np.array((weektimeSlices1, weekaveTau1))
    weekdatesTau1 = weekdatesTau1.T

    dgm1 = ripser.lower_star_img(weekdatesTau1)
    dgm2 = ripser.lower_star_img(weekdatesTau2)
    
    d, (matching, D) = persim.bottleneck(dgm1, dgm2, matching=True)
    persim.plot.bottleneck_matching(dgm1, dgm2, matching, D, labels=['1st $H_1$', '2nd $H_1$'])
    plt.title("Distance {:.3f}".format(d))

    axs.plot(weektimeSlices1, weekaveTau1, weektimeSlices2, weekaveTau2)     
#    axs.plot (weekly_data_list, weekly_Tau, 'b')
    axs.set(title='weekly', xlabel='Dates', ylabel='Absorbance(Tau)')
    axs.grid()
    #plt.savefig("Weekly_%7.8f_weather_data.png" % x)
   
plt.show()
