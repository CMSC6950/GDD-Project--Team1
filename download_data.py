import sys
import urllib.request
import os
import pandas as pd
import numpy as np
import shutil
import pdb

arglen = len(sys.argv)
if(arglen != 4):
	print("Invalid number of arguments: Please pass in the 3 arguments: input.csv start_year end_year")
	exit()

# download station inventory
stationIDUrl = "ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv"
urllib.request.urlretrieve(stationIDUrl,'station_inventory.csv')
outputFileName = "plot_data.csv"

# Read the Station IDs in input.csv
CityIdPair = {}
CityRows = pd.read_csv(sys.argv[1],skiprows=1,header=None,sep=',')
CityRows.columns = ['StationID','Cities','Tbase']

StationIDs = np.array(CityRows['StationID'].values.tolist())
Cities = np.array(CityRows['Cities'].values.tolist())
	
# Read year range
years = np.arange(int(sys.argv[2]),int(sys.argv[3]) + 1)
	
# download the weather data for the station IDs
downloadUrl="http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=STID&Year=YEAR&timeframe=2&submit=%20Download+Data"
for station in StationIDs:
	for year in years:
		ID = station
		url = downloadUrl.replace("STID",str(ID)).replace("YEAR",str(year))
		filename = str(ID) + "-" + str(year) + ".csv"
		urllib.request.urlretrieve(url,filename)


	


