import os, sys, stat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#file path
fpath= (os.getcwd()+'/Data/')
p_path= (os.getcwd()+'/Plots/')

def  get_weather_data(filename):
    df = pd.read_csv(filename,usecols=(1,5,6),encoding = 'utf-8',encoding='ISO-8859-1',skiprows=24)
    df.replace('E', np.nan,inplace=True)
    df.replace('M', np.nan,inplace=True)
    df = data.dropna(how='any')
    return df['Date/Time'],df['Max_Temp'],df['Min_Temp']

def min_max_plot:
