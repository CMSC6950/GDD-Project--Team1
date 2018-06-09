import sys
import os
import pandas as pd
import numpy as np
from pathlib import Path
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

# Download data and write output file
path = os.getcwd()
listfile = path + '/Data/' + 'cities_list.txt'
with open(listfile, 'w+') as listfile_handle:
    for stationID in stationIDs:
        for year in years:
            listfile_handle.write(str(stationID)+'-'+str(year)+'\n')
            outfile = path + '/Data/' + str(stationID) + '-' + str(year) + '.name'
            if not Path(outfile).exists():
                with open(outfile, 'a'):
                    os.utime(outfile, None)
