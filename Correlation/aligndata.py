# python script to align the LMT and SMT data
# it 

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import csv

# function to find the datetime in <items> which is
# the closest to the date <pivot>. it return the minimum
# difference (in nanoseconds) and the location where it found it
def nearest(items, pivot):
    dif=np.abs(items-pivot)
    mindif=np.amin(dif)
    return mindif, np.where(dif==mindif)
    
# read SMT dates and tau's
dataRead=pd.read_csv('C:\\Users\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\lmt_radiometer.csv',header=0)
tauRead=dataRead['tau'] 
tauLMT=tauRead.to_numpy()
whenRead=dataRead['dateStart']
whenLMT=pd.to_datetime(whenRead)
dateLMT=whenLMT.to_numpy()

print('Read LMT data')

# read APEX dates and tau's
dataRead=pd.read_csv('C:\\Users\\LENOVO\\Desktop\\PIRE_research\\data_CSVs\\SMT_data_edit.csv',header=0)
tauRead=dataRead['tau']
SMTtau=tauRead.to_numpy()
whenRead=dataRead['dateStart']
whenSMT=pd.to_datetime(whenRead)
SMTdate=whenSMT.to_numpy()

print('Read SMT data') #Apex

"""
# read LMT dates and tau's
dataRead=pd.read_csv('Desktop/PIRE_research/data_CSVs/lmt_radiometer.csv',header=0)
tauRead=dataRead['tau']
LMTtau=tauRead.to_numpy()
whenRead=dataRead['dateStart']
whenLMT=pd.to_datetime(whenRead)
LMTdate=whenLMT.to_numpy()

print('Read SMT data') #Apex

# read SMT dates and tau's
dataRead=pd.read_csv('Desktop/PIRE_research/data_CSVs/12M.csv',header=0)
tauRead=dataRead['tau']
APEXtau=tauRead.to_numpy()
whenRead=dataRead['dateStart']
whenAPEX=pd.to_datetime(whenRead)
APEXdate=whenAPEX.to_numpy()

print('Read SMT data') #Apex

"""







# pick the LMT datetimes as the basis and find the
# nearest neighbors of the SMT datetimes

# define a threshold of 10min
thres=np.timedelta64(10,'m')
with open('SMT&LMT_filter_aligned.csv', "w") as outfile:
   writer = csv.writer(outfile) 
   # for all LMT datetimes (starting from the second)
   for i in np.arange(1,np.size(dateLMT)):
     #print(dateLMT[i], type(dateLMT[i]))
     if (whenLMT[i].hour < 12 ) and (whenLMT[i].hour > 2) and (dateLMT[i]!=dateLMT[i-1]):
          mindif,wheremin=nearest(SMTdate, dateLMT[i])
		  # convert to an integer index
          whereminint=int(str(wheremin[0][0]))
		  # if the minimum difference is less than 10 minutes
          if (mindif<thres):
              writer.writerow([dateLMT[i],tauLMT[i],SMTdate[whereminint],SMTtau[whereminint]]) 
		     # otherwise, for SMT, print -1
          else:
              writer.writerow([dateLMT[i],tauLMT[i],SMTdate[whereminint],-1])