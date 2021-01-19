import numpy as np
import matplotlib.pyplot as plt
import csv
import corner

from datetime import datetime

#from plotParams import setPlotParams

def replacem1(array1):
    return np.where(array1==-1, -99, array1)

data=[np.array(map(int, line.split(','))) for line in open('/Users/DaltonGlove/Desktop/SMT_data_edit.csv', newline = '')]               #np.genfromtxt('SMT_data.csv',delimiter=',',usecols=np.arange(0,14))
#data = data.reshape([len(data), 10])
#with open('/Users/DaltonGlove/Desktop/SMT_data.csv', newline = '') as csvfile:
#        readCSV = csv.reader(csvfile, delimiter=',')
#        data = list(readCSV)    
#print(data[0:], data[:0])
dateObs=np.asarray([datetime.datetime.strptime(x, '%m/%d/%y %H:%M') for x in data[:0]])  #datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')


fractionalyear=np.asarray([datetime.timestamp(x)/(365.*24.*3600.)+1970-2019 for x in data[:0]])
temperature1=data[:4]       #data[:,10]
pressure1=data[:6]      #[:,9]
rel_humidity1=data[:5]         #[:,6]
wind_dir1=data[:8]
wind_speed1=data[:7]
tauarray1=data[:10]
#rainflag=data[:,12]

#replace all -1 with -99
temperature=replacem1(temperature1)
pressure=replacem1(pressure1)
rel_humidity=replacem1(rel_humidity1)
wind_dir=replacem1(wind_dir1)
wind_speed=replacem1(wind_speed1)
tauarray=replacem1(tauarray1)

temperature=(temperature!=-99) & (tauarray!=-99) & (tauarray<1)
pressure=(temperature!=-99) & (tauarray!=-99) & (tauarray<1)
rel_humidity=(temperature!=-99) & (tauarray!=-99) & (tauarray<1)
wind_dir=(temperature!=-99) & (tauarray!=-99) & (tauarray<1)
wind_speed=(temperature!=-99) & (tauarray!=-99) & (tauarray<1)
tauarray=(temperature!=-99) & (tauarray!=-99) & (tauarray<1)


weatherAll=np.asarray(list(
    
    zip(temperature, pressure, rel_humidity, wind_dir, wind_speed, tauarray)))
        
    #zip(temperature[(temperature!=-99) & (tauarray!=-99) & (tauarray<1)],
    #    pressure[(temperature!=-99) & (tauarray!=-99) & (tauarray<1)],
    #    rel_humidity[(temperature!=-99) & (tauarray!=-99) & (tauarray<1)],
    #    wind_dir[(temperature!=-99) & (tauarray!=-99) & (tauarray<1)],
    #    wind_speed[(temperature!=-99) & (tauarray!=-99) & (tauarray<1)],
    #    tauarray[(temperature!=-99) & (tauarray!=-99) & (tauarray<1)])))

fig1=corner.corner(weatherAll,labels=["Temperature (o C)","Pressure (mbar)","Rel. humidity (%)","Wind Dir (deg)","Wind Speed (m/s)","Tau"],show_titles=True, plot_datapoints=False, plot_contours=True, levels=(0.68,0.95), title_kwargs={"fontsize": 10})

fig1.savefig('cornerplotSMT.pdf')

