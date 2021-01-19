#!/usr/bin/env python3

import redis, json, time, csv
import matplotlib.pyplot as plt
import numpy as np
import datetime
import re

r = redis.Redis(host='192.168.1.11', port=6379, db=0, decode_responses=True) #192.168.1.11=local host

#last mongoDB date
#date = datetime.datetime.strptime(('dfas/sdsfs/saf 8:20') '%m/%d/%y %H:%M')

re_days = 1      # retrieve data within this number of days
t2 = time.time()
t1 = t2 - re_days*24*3600    # timestamp from last mongoDB date: 1561914076 
i=1

# weather
# Monitoring data is a dictionary like {'temperature': -3.5, 'pressure': 991.4}.
# It was converted to a string and written to the RDB as a Sorted Set (zset)
# with its timestamp as the "score" of that zset. So we extract data by scores:

ret_list = r.zrangebyscore('weatherData', t1, t2, withscores=False)

# The conversion of weatherData to string uses JSON, but the others may not be the case.
# Here to define a function trying to recover the original dictionary:
def rv_decode(vstr):
    """ In case the value of a zset element is not in JSON format. """
    try:
        val = json.loads(vstr)
    except json.decoder.JSONDecodeError:
        try:
            val = json.loads(vstr.replace("\'", "\""))
        except json.decoder.JSONDecodeError:
            val = {'not_json_raw': vstr}
    if isinstance(val, str):
        val = {'not_json_raw': val}
    return val      # dict

ret = rv_decode(ret_list[0])     # 1st entry

# There shall not be exception raised when JSON-decoding the weatherData.
# example entry:
# {'datetime': '191007 051614 1570425413', 'temperature': -3.5, 'pressure': 991.4, 
# 'humidity': 81.0, 'windspeed': 5.0, 'winddir': 158.0}
# with format / unit as
# {'datetime': DATE TIME POSIXTIME, 'temperature': C, 'pressure': mbar, 
# 'humidity': %, 'windspeed': m/s, 'winddir': degree}

print(ret['windspeed'])

dates, temps, hums, press=[], [], [], []

#open new file to write data into        
#with open('GLT_WeatherData_recent.csv', mode='w') as GLT_WeatherData_recent:

    #create callable command to write
    #Data_writer = csv.writer(GLT_WeatherData_recent, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #scroll through list of data assigning columns to eah data peice
#for row in ret_list:
    #if len(row): 
    #keyword args     some reason unaccessible with string indices
    #objId = row['_id']
    #date = row['datetime'] 
    #hum = row['humidity']
    #windD = row['winddir']
    #windS = row['windspeed']
    #pres = row['pressure']
    #temp = row['temperature']
    #score = row['score']
    
    #parse numbers from string (includes float and negatives)
        #newstr = ''.join((ch if ch in '0123456789.-' else ' ') for ch in str(row))
        #Numbers = [float(i) for i in newstr.split()]
        #parsed_data = Numbers[0:8:1]
    
    #if i%100==0:
     #   dates+=[((score/3.154e7)+1970)]
      #  temps+=[temp]
       # press+=[pres]
        #hums+=[hum]
           
    #get datetime from timestamp for weatherData
        #converted_date = datetime.datetime.fromtimestamp(int(parsed_data[2])).strftime('%m/%d/%y %H:%M')

        #Data_writer.writerow([i, -1, converted_date, converted_date, parsed_data[5], parsed_data[7], parsed_data[6], parsed_data[4], parsed_data[3], int(parsed_data[2])])
        #i+=1


# JSON decoding may fail for the following zsets; custom parsers may be reqired to
# resolve the original values --

# radiometer
ret_list = r.zrangebyscore('radiometerData', t1, t2, withscores=False)
ret = rv_decode(ret_list[2])     # 3rd entry
print(ret)

i=0
#open new file to write data into        
#with open('GLT_radiometerData_recent.csv', mode='w') as GLT_radiometerData_recent:

    #create callable command to write
    #Data_writer = csv.writer(GLT_radiometerData_recent, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #scroll through list of data assigning columns to eah data peice
for row in ret_list:
    if len(row):    
    #parse numbers from string (includes float and negatives)
        newstr = ''.join((ch if ch in '0123456789.-' else ' ') for ch in str(row))
        Numbers = [float(i) for i in newstr.split()]
        parsed_data = Numbers[0:10:1]   #objId iterates through numbers AND letters so go by negative index of gathered number to only take data and not id numbers
        
        #dates+=[((parsed_data[0]/3.154e7)+1970)]   #gets time for radiometerData
        #Tau_list+=[parsed_data[9]]

        converted_date = datetime.datetime.fromtimestamp(int(parsed_data[9])).strftime('%m/%d/%y %H:%M')

        #Data_writer.writerow([i, int(parsed_data[9]), converted_date, parsed_data[1], parsed_data[2], parsed_data[3], parsed_data[4]]) #i, converted_date, Taustamp, Tau, elevat, rain, rainQual)
        print([i, int(parsed_data[9]), converted_date, parsed_data[1], parsed_data[2], parsed_data[3], parsed_data[4]])
        i+=1

i=0
# example entry:
#index after backwards parse:      8         7                   6...
# {'timestamp':1570421262,'tau':0.466037,'elevation':89.800003,'rainflag':0,
#    5                    4             3             2
# 'rainflagQuality':0,'HKDalarm':0,'status':1,'statusTimestamp':1570421262,
#     1                            0                  
# 'hkdTimestamp':1570421261,'tauTimestamp':1570421261}
# Consult with Nimesh for the variable definitions.

# maser weather
#ret_list = r.zrangebyscore('maserHouseWeather', t1, t2, withscores=False)
#ret = rv_decode(ret_list[3])     # 4th entry
# example  entry:
# {'temperature': '21.1 C', 'dewPoint': '-4.0 C', 'timestamp': 1567510132.9682877, 
# 'datetime': '03 Sep 2019 08:28:52', 'humidity': '18.3 %'}


"""

# MongoDB, one time dump ===================================================== #
import pymongo

# login the MongoDB, authentication required  #local host = 192.168.1.11
m = pymongo.MongoClient('192.168.1.11:27017', username='gltdbgirl', password='glt12m@Thule', 
                        authSource='GreenlandTelescope', authMechanism='SCRAM-SHA-256')

# all RedisDB keys are stored under the single database 'GreenlandTelescope' as collections
db = m.GreenlandTelescope

# each zset in the RedisDB is stored as a collection with the same name in the 
# MongoDB, and each entry of that zset is stored as one document.
collection1 = db['radiometerData']      # 'weatherData' or 'radiometerData' or 'maserHouseWeather'
cursor = collection1.find()          # no query rules -> find all documents


#arrays to check plots
dates=[]
temps=[]
press=[]
hums=[]
Tau_list=[]
#Numbers=[]

#open new file to write data into        
#with open('GLT_Weatherdata_Tau.csv', mode='w') as GLT_Weatherdata_Tau:

    #create callable command to write
    #Data_writer = csv.writer(GLT_Weatherdata_Tau, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #scroll through list of data assigning columns to eah data peice
for row in cursor:    #reindent to include in with open file loop when wrting
        #print(type(row))
        if len(row):
            #weatherdata    
            #objId = row['_id']
            #date = row['datetime'] 
            #hum = row['humidity']
            #windD = row['winddir']
            #windS = row['windspeed']
            #pres = row['pressure']
            #temp = row['temperature']
            #score = row['score']
            
            #if i%100==0:
            #    dates+=[((score/3.154e7)+1970)]
            #    temps+=[temp]
            #    press+=[pres]
            #    hums+=[hum]
            
            #radiometerdata     labels don't work use parsed numbers from string below
            #Taustamp = row['tauTimestamp']
            #Tau = row['tau']
            #elevat = row['elevation']
            #rain = row['rainflag']
            #rainQual = row['rainflagQuality']
            #HKD = row['HKDalarm']   
            #status = row['status']
            
            #parse numbers from string (includes float and negatives)
            newstr = ''.join((ch if ch in '0123456789.-' else ' ') for ch in str(row))
            Numbers = [float(i) for i in newstr.split()]
            parsed_data = Numbers[-1:-11:-1]   #objId iterates through numbers AND letters so go by negative index of gathered number to only take data and not id numbers
            
            
            dates+=[((parsed_data[0]/3.154e7)+1970)]   #gets time for radiometerData
            Tau_list+=[parsed_data[9]]
            
            #get datetime from timestamp for weatherData
            #converted_date = datetime.datetime.fromtimestamp(score).strftime('%m/%d/%y %H:%M') #score or parsed_data[0](Tautimestamp)
            
            #Data_writer.writerow([i, objId, date, converted_date, hum, windD, windS, pres, temp, score])
               #or
            #Data_writer.writerow([i, parsed_data[0], converted_date, parsed_data[9], parsed_data[8], parsed_data[7], parsed_data[6]]) #i, converted_date, Taustamp, Tau, elevat, rain, rainQual)
            i+=1
i=0   
         
    #10                     #9                  #8              #7
#{'timestamp':1570421262,'tau':0.466037,'elevation':89.800003,'rainflag':0,
# 'rainflagQuality':0,'HKDalarm':0,'status':1,'statusTimestamp':1570421262,
# 'hkdTimestamp':1570421261,'tauTimestamp':1570421261}

#sort and grab percentiles
timepts = []
stepNpts=2000    #calc in loop based on dates for accuracy
perc1, perc2, perc3 = .25, .5, .75
perc1pts, perc2pts, perc3pts = [], [], []
#observe each ~5min to start then every 10min so sort over ~4000-8000pts to estimate month
for i in range(len(Tau_list)):
    
    if i+stepNpts < len(Tau_list):
        sorted_Tau = sorted(Tau_list[i:(i+stepNpts)])
        perc3pts += [sorted_Tau[int(len(sorted_Tau)*perc3)]]
        perc2pts += [sorted_Tau[int(len(sorted_Tau)*perc2)]]
        perc1pts += [sorted_Tau[int(len(sorted_Tau)*perc1)]]
        timepts+=[dates[int(i+(stepNpts/2))]]
        i+=stepNpts
    if i+stepNpts > len(Tau_list): break
        #sorted_Tau = sorted(Tau_list[i:len(Tau_list)])
        #perc3pts += [sorted_Tau[int(len(sorted_Tau)*perc3)]]
        #perc2pts += [sorted_Tau[int(len(sorted_Tau)*perc2)]]
        #perc1pts += [sorted_Tau[int(len(sorted_Tau)*perc1)]]
        #timepts+=[dates[len(Tau_list)-1]]

#graph test   

#print(len(dates), len(Tau_list))
fig, axs = plt.subplots()
print('please enter 1 for full plot of data, 2 for percentiles')
choose = int(input())

if choose == 1:
    plt.scatter(dates, Tau_list, s=5, c='b', alpha=.5)
    plt.xlabel('Year (Fractional from UTC timestamp)')
    plt.ylabel('Optical Depth (Tau)')
    plt.ylim(0, 2.5)
    plt.show()
    plt.savefig('fullTaudata.png', format='png')
if choose ==2:
    axs.plot(timepts, perc3pts, 'bo', markersize=2), axs.plot(timepts, perc2pts, 'bo', markersize=2), axs.plot(timepts, perc1pts, 'bo', markersize = 2)
    plt.xlabel('Year (Fractional from UTC timestamp)')
    plt.ylabel('Optical Depth (percentile)')            #plt.axis([0, 24, 0, 1.5])
    plt.ylim(0, 1.2)
    plt.savefig('testTauPercent.png', format='png')
"""
"""
for doc in cursor:
    try:
        pres = doc['pressure']
        
        #print('pressure= ', pres)
        # convert & write to a sqlite db on disk for example
        
        
        
    except KeyError:                # in case the original RDB entry was not JSON-compatible
        raw = doc['not_json_raw']
        print('raw string= ', raw)
        # custom parser for this non-JSON string
        # convert & write to a sqlite db on disk for example

"""
