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
data_path= (os.getcwd()+'/Data/')

#count to get the name of each citie
city_index = 0
for station in StationIDs:
	for year in years:
		ID = station
		url = downloadUrl.replace("STID",str(ID)).replace("YEAR",str(year))
		filename = Cities[city_index] + "-" +str(ID) + "-" + str(year) + ".csv"
		with open(filename, 'w') as datafile:
			urllib.request.urlretrieve(url,filename)
		#Getting specific data
		data_frame = pd.read_csv(filename, usecols=(0,1,2,3,5,7,9),header=None, skiprows=25, sep=",", encoding="ISO-8859-1")
		data_frame.columns=['Date/Time','Year','Month','Day','Max_Temp','Min_Temp','Mean_Temp']
		new_fname =  data_path+filename
		data_frame.to_csv(new_fname)
		# removing temporary saved files
		os.remove(filename)
		#increment to go through each one
	city_index += 1
#remove station file
os.remove('station_inventory.csv')
print("Files Extracted")
