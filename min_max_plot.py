import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from pandas import Series, DataFrame
import pandas as pd
import csv
import sys
import os.path
import pdb

fig,ax1=plt.subplots()
fig = plt.figure(figsize=(15,7))
ax2=ax1.twinx()


def get_weather_data(file_name):
    """
    This function reads a csv file and returns the date, min,max Temperature
    args:file_name (csv data file)
    output:Date/Time,Max_Temp, Min_Temp
    """
    df=pd.read_csv(file_name,encoding='ISO-8859-1')
    #sanitize data removing missing values etc
    df.replace('E', np.nan,inplace=True)
    df.replace('M', np.nan,inplace=True)
    df = df.dropna(how='any')
    return df['Date/Time'] ,df['Max_Temp'], df['Min_Temp']


def min_max_plot(filename,filepath= (os.getcwd()+'/Data/'),plot_dir = (os.getcwd()+'/Plots/')):
    """
        This function makes min and max plots and save them
    args :filename(csv), filepath(default),output(default)
    output:
        save min and max plots
    """
    date,max_temp,min_temp=get_weather_data(filepath+filename)
    date=pd.to_datetime(date)

    #plot graphs
    maxy,=plt.plot_date(date,max_temp,'ro-',label="max temp")
    mint,=plt.plot_date(date,min_temp,'cx-',label="min temp")

    #Add legend to the above two plot
    plt.legend(handles=[maxy,mint])
    plt.ylabel("Temperature")
    plt.xlabel("Date")
    city_name = filename.split('-')
    city_name =city_name[0]
    plt.title("Min & Max Temperature of "+str(city_name))

    # To save the plot with the argument's name
    f_name = os.path.basename(filename[:-4])

    outfile = plot_dir + f_name + "_minmax.png"
    print("Plot min_max output file : " + plot_dir + f_name + "_minmax.png")

    #save plot
    plt.savefig(outfile, format = "png")


def get_allfiles():
    files = os.listdir(filepath)
    return files

#csv data files location
filepath= (os.getcwd()+'/Data/')

#pdb.set_trace()

files = get_allfiles()
for file in files:
    if str(file).endswith('.csv'):
        Data = pd.read_csv(filepath+file, encoding = 'utf-8')
        min_max_plot(file)
