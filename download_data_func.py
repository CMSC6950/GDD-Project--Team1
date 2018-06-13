import sys
import urllib.request
import os
import pandas as pd
import numpy as np
import shutil
from pathlib import Path
import pdb

def download_data_func(stationID, year):
#    pdb.set_trace()

    # download the weather data for the station ID
    outfile = 'docs/data/' + str(stationID) + '_' + str(year) + '.csv'
    if not Path(outfile).exists():
        downloadUrl="http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=STID&Year=YEAR&timeframe=2&submit=%20Download+Data"
        url = downloadUrl.replace("STID",str(stationID)).replace("YEAR",str(year))
        urllib.request.urlretrieve(url,outfile)

        # Process the downloaded data
        df = pd.read_csv(outfile, usecols=(0,1,2,3,5,7,9),header=None,skiprows=25,sep=',',encoding="ISO-8859-1")
        df.columns = ['Date/Time','Year','Month','Day','Max_Temp','Min_Temp','Mean_Temp']
        df.dropna()
        df.to_csv(outfile)
    return

