import pandas as pd
import numpy as np
import cartopy.crs as ccrs
import sys
import os
import matplotlib.pyplot as plt
#import pdb

from cumgdd import cumgdd
from download_data_func import download_data_func

# For testing, this script only process a small part of the stations
# To be fixed when writing real code.

#pdb.set_trace()

# Get station list from station inventory which exists from the previous download step
station_inventory = "station_inventory.csv"
inventory_df = pd.read_csv(station_inventory, usecols=(0,1,3,6,7),index_col=0,skiprows=3,sep=',')

# Define a sample for testing
sample_inventory_df = inventory_df.loc[inventory_df['Province']=='NEWFOUNDLAND'][1:300:10]

nl_stations = inventory_df.loc[inventory_df['Province']=='NEWFOUNDLAND','Station ID'].tolist()
cumulative_gdd_list = []

tbase = 10
tupper = 30
year = 2016

# Download temparature data files for all cities in the list 
for station in nl_stations[1:300:10]:
    download_data_func(station, year)
    infile = 'Data/' + str(station) + '_' + str(year) + '.csv'
    cumulative_gdd_list.append(cumgdd(infile, tbase, tupper))
    
# Add a column of cumulative gdd values
#inventory_df.insert(loc=3, column='Cumulative GDD', value=cumulative_gdd_list)
#inventory_df.to_csv('inventory_df.csv')
sample_inventory_df.insert(loc=3, column='Cumulative GDD', value=cumulative_gdd_list)
sample_inventory_df.to_csv('inventory_df.csv')




# Plot gdd map with the above data

