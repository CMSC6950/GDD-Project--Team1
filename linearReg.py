import numpy as np
import pandas as pd
import time as time
import math
import os
import csv
import matplotlib.pyplot as plt
import itertools

colors = itertools.cycle(['b','g','r','c','m','y','k'])

#file paths
plotpath = (os.getcwd()+'/Plots/')
filepath = (os.getcwd()+'/Data/')


def get_gdd_files(filepath,start,end):
    "This function gets gdd files from the Data/ directory"
    station_name_id = ""
    list_years = list(range(int(start),int(end)+1))
    files = os.listdir(filepath)
    files = [file for file in files if file.endswith('GDD.csv')]
    for i in range(0,len(files)):
        split_file = files[i].split('-')
        sta_id = split_file[0]
        sta_year = split_file[1]

        if sta_id in files[i] and sta_year in str(list_years):
            station_name_id =sta_id
            df = pd.read_csv(filepath+files[i], encoding = 'utf-8',index_col=0)
            gddfile_name = filepath+'GDD_Value_'+station_name_id+'_'+str(start)+'_'+str(end)+'.csv'
            df.to_csv(gddfile_name , mode='a', header=False)




def gddPlot_linearReg(station_id_name,start=2016,end=2017):
    gdd_name = filepath+'GDD_Value_'+station_id_name+'_'+str(start)+'_'+str(end)+'.csv'
    list_years = list(range(int(start),int(end)))
    GDD_mean = []
    fig = plt.figure(figsize=(12, 6))
    plt.title('GDD from '+str(start)+' to '+str(end)+', in '+ station_id_name)
    plt.ylabel('GDD across different years')
    plt.xlabel('Dates')
    plt.ylim(0,1000)
    plt.xlim(int(start)-1,int(end))
    Data = pd.read_csv(gdd_name, encoding = 'utf-8')
    Data.columns =['AccGDD','Date/Time']

    for year in list_years:
        instance = Data[Data['Date/Time'].str.contains(str(year))]
        GDD_mean.append(np.mean(instance['AccGDD']))
        print(GDD_mean)
    (m,b) = np.polyfit(list_years,GDD_mean,1)
    yp = np.polyval([m,b],list_years)
    plt.scatter(list_years, GDD_mean,color= next(colors), label = "Accumalated GDD mean in "+station_id_name)
    plt.plot(list_years,yp)
    plt.legend(loc='upper left')
    fig.savefig(plotpath+'/GDD_LinearRegression_'+station_id_name+'.png')

gddPlot_linearReg('49568')

#gddPlot_linearReg(station_id_name,start=2013,end=2017)

  
