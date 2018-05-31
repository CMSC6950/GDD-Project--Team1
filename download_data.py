import sys
import urllib.request
import os
import pandas as pd
import numpy as np

arglen = len(sys.argv)
if(arglen != 3):
	print("Not enough arguments: Please pass in the 3 arguments: input.csv start_year end_year")
	return

# Url down sometimes                             	
stationIDUrl = "ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv"
outputFileName = "plot_data.csv"

# Delete the old downloaded file
if(os.file.exists(outputFileName)):
	os.remove(outputFileName)

# Read the City Names in input.csv
CityIdPair = {}
CityRows = pd.read_csv(sys.argv[0],skiprows=1,header=None,sep='\s')
CityRows.columns = ['Cities']
Cities = np.array(rows['Cities'].values)

StationRows = pd.read_csv(station_inventory.csv,sep=',',header=None)
StationRows.columns =["Name","Province","Climate ID","Station ID","WMO ID","TC ID","Latitude (Decimal Degrees)","Longitude (Decimal Degrees)","Latitude","Longitude","Elevation (m)","First Year","Last Year","HLY First Year","HLY Last Year","DLY First Year","DLY Last Year","MLY First Year","MLY Last Year"]    
                

for city in Cities:
	city = city.upper()
	CityIdPair[city] = StationRows.query('Name == city')['Station ID']

	


