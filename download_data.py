import sys
import urllib.request
import os
import pandas as pd
import numpy as np
import shutil
from pathlib import Path
import pdb

#############################################################################
# argv[1] is a filename of format: stationID-year.name
# This script will download and write the data of 'stationID' at 'year' to 
# corresponding .csv file
#############################################################################

arglen = len(sys.argv)
if(arglen != 2):
	print("Invalid number of arguments!")
	exit()

# Read stationID and year from the filename
# pdb.set_trace()
temp = sys.argv[1].split('/')[1]
station = str(temp).split('-')
stationID = station[0]
year = station[1].split('.')[0]

# download station inventory
inventory_file = Path('station_inventory.csv')
if not inventory_file.exists():
    stationIDUrl = "ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv"
    urllib.request.urlretrieve(stationIDUrl,'station_inventory.csv')

# download the weather data for the station ID
outfile = sys.argv[1].split('.')[0] + '.csv'
downloadUrl="http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=STID&Year=YEAR&timeframe=2&submit=%20Download+Data"
url = downloadUrl.replace("STID",str(stationID)).replace("YEAR",str(year))
urllib.request.urlretrieve(url,outfile)

# Process the downloaded data
df = pd.read_csv(outfile, usecols=(0,1,2,3,5,7,9),header=None,skiprows=25,sep=',',encoding="ISO-8859-1")
df.columns = ['Date/Time','Year','Month','Day','Max_Temp','Min_Temp','Mean_Temp']
df.to_csv(outfile)

