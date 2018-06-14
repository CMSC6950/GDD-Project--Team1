# This script depends on the output of gdd.py
import pandas as pd
import re
import os

# Get all gdd files in the directory
files = os.listdir(os.getcwd()+'/Data/')
gdd_files = ['Data/' + filename for filename in files if filename.endswith('GDD.csv')]
gdd_files

# Define a regular expression to get tbase from file name
re_id_tbase = re.compile("^Data/(\d*)-\d+_base_(\d*)_GDD.csv$")
# Get the list of stations for gdd plot
station_set = set()
for name in gdd_files:
    m = re_id_tbase.match(name)
    station_set.add(m.groups()[0])
    
station_list = list(station_set)

# First station
infiles = ['Data/' + filename for filename in files if filename.endswith('GDD.csv') and filename.startswith(station_list[0])]

# Read csv files for each tbase of the same station
df_list = []
for f in infiles:
    dfi = pd.read_csv(f, index_col=0)
    m = re_id_tbase.match(f)
    base = m.groups()[1]
    dfi.columns = ['tbase = ' + base]
    df_list.append(dfi)
# Concaternate the different dataframes
df = pd.concat(df_list,axis=1)

plot1 = df.plot(figsize=(15,10), title = 'Daily GDD for station ' + station_list[0] + ' with different tbase')
fig1 = plot1.get_figure()
fig1.savefig("docs/plots/" + station_list[0] + '_daily_gdd_plot.png')


# Second Station
infiles = ['Data/' + filename for filename in files if filename.endswith('GDD.csv') and filename.startswith(station_list[1])]

# Read csv files for each tbase of the same station
df_list = []
for f in infiles:
    dfi = pd.read_csv(f, index_col=0)
    m = re_id_tbase.match(f)
    base = m.groups()[1]
    dfi.columns = ['tbase = ' + base]
    df_list.append(dfi)
# Concaternate the different dataframes
df = pd.concat(df_list,axis=1)

plot1 = df.plot(figsize=(15,10), title = 'Daily GDD for station ' + station_list[1] + ' with different tbase')
fig1 = plot1.get_figure()
fig1.savefig("docs/plots/" + station_list[1] + '_daily_gdd_plot.png')


# Third Station
infiles = ['Data/' + filename for filename in files if filename.endswith('GDD.csv') and filename.startswith(station_list[2])]

# Read csv files for each tbase of the same station
df_list = []
for f in infiles:
    dfi = pd.read_csv(f, index_col=0)
    m = re_id_tbase.match(f)
    base = m.groups()[1]
    dfi.columns = ['tbase = ' + base]
    df_list.append(dfi)
# Concaternate the different dataframes
df = pd.concat(df_list,axis=1)

plot1 = df.plot(figsize=(15,10), title = 'Daily GDD for station ' + station_list[2] + ' with different tbase')
fig1 = plot1.get_figure()
fig1.savefig("docs/plots/" + station_list[2] + '_daily_gdd_plot.png')
