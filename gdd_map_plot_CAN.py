import pandas as pd
import numpy as np
import cartopy.crs as ccrs
import sys
import os
import matplotlib.pyplot as plt
#import pdb

from cumgdd import cumgdd
from download_data_func import download_data_func

tbase = 10
tupper = 30
year = 2016

# Get station list from station inventory which exists from the previous download step
station_inventory = "station_inventory.csv"
inventory_df = pd.read_csv(station_inventory, usecols=(0,1,3,6,7,15,16),index_col=0,skiprows=3,sep=',')
inventory_df = inventory_df.dropna()

# Get the list of NEWFOUNDLAND stations with valid data for a specific year 
inventory_df = inventory_df[(inventory_df['DLY Last Year']>=year) & (inventory_df["DLY First Year"]<=year)]

all_stations = inventory_df['Station ID'].tolist()
cumulative_gdd_list = []

# Download temparature data files for all cities in the list 
for station in all_stations:
#    pdb.set_trace()
    download_data_func(station, year)
    infile = 'Data/' + str(station) + '_' + str(year) + '.csv'
    cumulative_gdd_list.append(cumgdd(infile, tbase, tupper))
    
# Add a column of cumulative gdd values
inventory_df.insert(loc=4, column='Cumulative GDD', value=cumulative_gdd_list)
inventory_df.dropna(subset=["Cumulative GDD"], inplace=True)

# Plot GDD map for all Canada
inventory_df = inventory_df[inventory_df["Latitude (Decimal Degrees)"]<70]
lats = np.array(inventory_df['Latitude (Decimal Degrees)'].tolist())
lons = np.array(inventory_df['Longitude (Decimal Degrees)'].tolist())
cgdd = np.array(inventory_df["Cumulative GDD"].tolist())
fig = plt.figure(figsize=(15,20))

# Scatter Plot
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines('10m')
ax.scatter(lons, lats, marker='o', c=cgdd, s=cgdd, transform=ccrs.PlateCarree(), alpha=0.5)
ax.set_extent([-145,-50,40,70])
plt.title("Effective growing degree days of Canada in 2016", fontsize=20)
plt.savefig("Plots/GDD_Map_CAN_scatter.png")

# Contour Plt
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines('10m')
c = ax.tricontour(lons, lats, cgdd)
ax.clabel(c, inline=1, fontsize=10)
ax.tricontourf(lons, lats, cgdd)
ax.scatter(lons, lats, marker='o', color='k', s=10, transform=ccrs.PlateCarree(), alpha=0.5)
ax.set_extent([-145,-50,40,70])
plt.title("Effective growing degree days of Canada in 2016", fontsize=20)
plt.savefig("Plots/GDD_Map_CAN_contour.png")
