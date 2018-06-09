import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os,glob
import matplotlib.cm as cm


##############################################################################################################
#																											 #
# THIS SCRIPT WILL READ THE *-CumGDD.csv files in the ./Data Folder and create GDD plots for selected cities #
#																											 #
##############################################################################################################

# Read station IDs and Station Names
stationRows = pd.read_csv('input.csv',skiprows=1,header=None)
stationRows.columns = ["StationID","StationName","TBase"]
stationdIDs = np.array(stationRows["StationID"].values)
stationNames = np.array(stationRows["StationName"].values)
Tbase = np.array(stationRows.TBase.unique())

# Use StationIDs to read GDD files from Data folder and call function to plot it
os.chdir("./Data")
for stid,stName in zip(stationdIDs,stationNames):
	fileNames = []
	for file in glob.glob(str(stid)+"*-CumGDD.csv"):
		fileNames.append(file)
	gddPlot = plot_gdd_forCity(fileNames,stName,Tbase)
	saveAs = '../Plots/' + str(stName) + '.png'
	gddPlot.savefig(saveAs)

# function to plot GDD per city for multiple years
def plot_gdd_forCity(fileNames,stName,tbase):
	allYearsData = pd.DataFrame()
	yearList = []
	for file in fileNames:
		df = pd.read_csv(file,skiprows=1,header=None)
		yearList.append(df)
	allYearsData = pd.concat(yearList)
	allYearsData.columns = ['Date','GDD']
	allYearsData[['year','month','day']] = allYearsData['Date'].str.split('-',expand=True)
	
	years = np.array(allYearsData.year.unique()) #get the years
	colors = cm.rainbow(np.linspace(0, 1, len(years)))
	x = np.linspace(1,12,365,endpoint=True)
	
	for year,c in zip(years,colors): 
		plt.plot(x,allYearsData[allYearsData['GDD'].notnull() & (allYearsData['year'] == year)].GDD,color=c,label=year)
		
	plt.legend(loc='upper left')
	ax = plt.gca()
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.yaxis.grid()
	ax.set_xlabel('Months', color='black', fontsize=16)
	ystring = 'Cumulative GDD (>' + str(tbase) + ')°C' 
	ax.set_ylabel(ystring, color='black', fontsize=16)
	plotTitle = 'Accumulated Growing Degree Days For - ' + str(stName)
	plt.title(plotTitle, color="black", fontsize=16)
	return plt
	