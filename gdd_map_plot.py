import pandas as pd
import numpy as np
import cartopy.crs as ccrs
import sys
import os
import matplotlib.pyplot as plt
import pdb

from cumgdd import cumgdd
from download_data_func import download_data_func

pdb.set_trace()

# Get station list from station inventory which exists from the previous download step
station_inventory = "station_inventory.csv"
inventory_df = pd.read_csv(station_inventory, usecols=(0,1,3,6,7),index_col=0,skiprows=3,sep=',')

nl_stations = inventory_df.loc[inventory_df['Province']=='NEWFOUNDLAND','Station ID'].tolist()
cumulative_gdd_list = []

tbase = 10
tupper = 30
year = 2016

# Download temparature data files for all cities in the list 
for station in nl_stations:
    download_data_func(station, year)
    infile = 'Data/' + str(station) + '_' + str(year) + '.csv'
    cumulative_gdd_list.append(cumgdd(infile, tbase, tupper))
    
# Add a column of cumulative gdd values
inventory_df.insert(loc=3, column='Cumulative GDD', value=cumulative_gdd_list)
inventory_df.to_csv('inventory_df.csv')


# Plot gdd map with the above data

