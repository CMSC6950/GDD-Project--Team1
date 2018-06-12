import pandas as pd
import numpy as np
import cartopy.crs as ccrs
import sys
import os
import matplotlib.pyplot as plt
#import pdb

from cumgdd import cumgdd
from download_data_func import download_data_func

#pdb.set_trace()

tbase = 10
tupper = 30
year = 2016

# Get station list from station inventory which exists from the previous download step
station_inventory = "station_inventory.csv"
inventory_df = pd.read_csv(station_inventory, usecols=(0,1,3,6,7,15,16),index_col=0,skiprows=3,sep=',')
inventory_df.dropna()

# Get the list of NEWFOUNDLAND stations with valid data for a specific year 
NL_inventory_df = inventory_df[(inventory_df['Province']=='NEWFOUNDLAND') & (inventory_df['DLY Last Year']>=year) & (inventory_df["DLY First Year"]<=year)]

NL_stations = NL_inventory_df['Station ID'].tolist()
cumulative_gdd_list = []

# Download temparature data files for all cities in the list 
for station in NL_stations:
    download_data_func(station, year)
    infile = 'Data/' + str(station) + '_' + str(year) + '.csv'
    cumulative_gdd_list.append(cumgdd(infile, tbase, tupper))
    
# Add a column of cumulative gdd values
NL_inventory_df.insert(loc=4, column='Cumulative GDD', value=cumulative_gdd_list)
#NL_inventory_df.to_csv('inventory_df.csv')




# Plot gdd map with the above data

