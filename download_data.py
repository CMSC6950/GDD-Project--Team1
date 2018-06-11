import sys
import os
import pandas as pd
import numpy as np
from pathlib import Path
import urllib
import pdb

if len(sys.argv) != 4:
    print("Invalid number of arguments.\n")
    exit()

# Debug
#pdb.set_trace()

infile = sys.argv[1]
cityRows = pd.read_csv(infile, skiprows=1, header=None, sep=',')
cityRows.columns = ['StationID', 'City', 'Tbase']

stationIDs = np.array(cityRows['StationID'].values.tolist())
cities = np.array(cityRows['City'].values.tolist())

start_year = int(sys.argv[2])
end_year = int(sys.argv[3])
years = np.arange(start_year, end_year+1)

# download station inventory if not exists
inventory_file = Path('station_inventory.csv')
if not inventory_file.exists():
    stationIDUrl = "ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv"
    urllib.request.urlretrieve(stationIDUrl,'station_inventory.csv')

# Download data and write output file
path = os.getcwd()
for stationID in stationIDs:
    for year in years:
        outfile = path + '/Data/' + str(stationID) + '-' + str(year) + '.csv'
        if not Path(outfile).exists():
            downloadUrl="http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=STID&Year=YEAR&timeframe=2&submit=%20Download+Data"
            url = downloadUrl.replace("STID",str(stationID)).replace("YEAR",str(year))
            urllib.request.urlretrieve(url,outfile)

            # Process the downloaded data
            df = pd.read_csv(outfile, usecols=(0,1,2,3,5,7,9),header=None,skiprows=25,sep=',',encoding="ISO-8859-1")
            df.columns = ['Date/Time','Year','Month','Day','Max_Temp','Min_Temp','Mean_Temp']
            df.to_csv(outfile)
