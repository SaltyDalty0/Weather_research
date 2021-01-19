#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 00:16:35 2019

@author: DaltonGlove
"""
""" #unzips files in directory
import os
import zipfile

for path, dir_list, file_list in os.walk('/Users/DaltonGlove/Desktop/SMT_KP_weather'):
    for file_name in file_list:
        if file_name.endswith(".zip"):
            abs_file_path = os.path.join(path, file_name)

            # The following three lines of code are only useful if 
            # a. the zip file is to unzipped in it's parent folder and 
            # b. inside the folder of the same name as the file

            parent_path = os.path.split(abs_file_path)[0]
            output_folder_name = os.path.splitext(abs_file_path)[0]
            output_path = os.path.join(parent_path, output_folder_name)

            zip_obj = zipfile.ZipFile(abs_file_path, 'r')
            zip_obj.extractall(output_path)
            zip_obj.close()
            
"""
"""
#unzips all tar.gz files
import tarfile,fnmatch,os
 
rootPath = r"C:\Teste_Auto_Unzip"
pattern = '*.tar.gz'
for root, dirs, files in os.walk('/Users/DaltonGlove/Desktop/SMT_KP_weathercopy'):
    for filename in fnmatch.filter(files, pattern):
        #print(os.path.join(root, filename))
        tarfile.open(os.path.join(root, filename)).extractall(os.path.join(root, filename.split(".")[0]))
        
        
        
"""
import datetime, jdcal #, glob  

import os, csv

path = '/Users/DaltonGlove/Desktop/All_weather_sep/weather_smt/'

date_file_list=[]
         #os.walk(path)  #glob.glob(path)
for file in os.walk(path):
    for i in range(len(file[2])):     #len(file[2])):
        
        #print(file[2])
        #print(path + str(file[2][i]))
    
        #newstr = ''.join((ch if ch in '0123456789-' else ' ') for ch in str(file[2][i]))
        #Numbers = [float(i) for i in newstr.split()]
        #file_date = datetime.datetime.strptime(newstr, '        %m%d%y')
        
        #sort by modifidy date for 12m and since error corrected on 100103 use date from name for SMT
        
        mod_date = os.path.getmtime(path + str(file[2][i]))
        if i%100==0: print(mod_date, file[2][i], i)
        date_file_tuple = mod_date, file[2][i]
    
        date_file_list+=[(date_file_tuple)]  #date_file_list.append(date_file_tuple)
     
print('done getting timestamps', len(date_file_list))
date_file_list.sort()
i=0
#************
#for old 12m data 
#parse file name as string and convert to datetime for a check or use timestamps explicitly
#parse row as string and extract numbers to list 
#************

#gap from end of june 1994 to sept 1994


#102394 data changes from fractional hour of day
#to julian without 24 in beginning to shorten it (MJD) and 
#-1 from actual julian date? ask natalie if it was stored and named on the next day

#Tau not recorded until 102296, and relative humidity from the tipper until 091804

#pars

j1=0
data_array = []
for i in range(len(date_file_list)-1):
    #print(path + date_file_list[i][1])
    with open(path + date_file_list[i][1], "r") as files:
        j=0
    #parse numbers from string (includes float and negatives)
        newstr = ''.join((ch if ch in '0123456789-' else ' ') for ch in str(date_file_list[i][1]))
        #Numbers = [float(i) for i in newstr.split()]
        file_date = datetime.datetime.strptime(newstr, '        %m%d%y')
        #print(file_date)
        for row in files:
            if len(row):
            #parse numbers from string (includes float and negatives)
                newstr = ''.join((ch if ch in '0123456789.-' else ' ') for ch in str(row))
                Numbers = [float(i) for i in newstr.split()]
                parsed_data = Numbers[0:] 
                #mjd = parsed_data[0]                                #strftime('%m/%d/%y %H:%M')
                #dt = julian.from_jd(mjd, fmt='mjd')
                if len(parsed_data):
                    dt = jdcal.jd2gcal(2400000.5, parsed_data[0])
                    year = (dt[0])
                    month = (dt[1])
                    day = (dt[2])
                    hour = int(dt[3]/.0416666)
                    minute = int((dt[3]/.0006945) - (hour*60))
                    date = datetime.datetime(year, month, day, hour, minute)
                    stringdate = "{:%m/%d/%y %H:%M}".format(date)
                #print(stringdate, date)
                    parsed_data.insert(0,j1), parsed_data.insert(0,date), parsed_data.insert(0, stringdate)
                    data_array+=[(parsed_data[:])]
                    #print(parsed_data[:])
                    if j1==1341100 : print("\n", file_date, "\n", row, "\n", parsed_data, "\n") #%1000
                    j+=1
                    j1+=1
#with open('SMT_data.csv', mode='w') as file:

    #create callable command to write
#    Data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
#scroll through list of data assigning columns to eah data peice
        
#    for row in data_array:       
        
               
            
#            Data_writer.writerow(row)

"""
import os
import zipfile

for path, dir_list, file_list in os.walk('/Users/DaltonGlove/Desktop/SMT_KP_weather'):
    for file_name in file_list:
        if file_name.endswith(".zip"):
            abs_file_path = os.path.join(path, file_name)

            # The following three lines of code are only useful if 
            # a. the zip file is to unzipped in it's parent folder and 
            # b. inside the folder of the same name as the file

            parent_path = os.path.split(abs_file_path)[0]
            output_folder_name = os.path.splitext(abs_file_path)[0]
            output_path = os.path.join(parent_path, output_folder_name)

            zip_obj = zipfile.ZipFile(abs_file_path, 'r')
            zip_obj.extractall(output_path)
            zip_obj.close()
"""