import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
import gdd


def plot_GDD(fileNames,tbase,tupper,stName):
	x = np.linspace(1,12,365,endpoint=True)
	leg =[]
	fig= plt.figure(figsize=(10,6))
	for file in fileNames:
		year = file.split('_')[0].split('-')[1]
		print('Plotting Accumulated GDD for',stName,'and year',year)
		leg.append(year)
		df = pd.read_csv(file)
		if len(df) == 366:
			df.drop(df.tail(1).index,inplace=True)
		date = df['Date/Time']
		gdd = df['Daily GDD']
		cumgdd = gdd.cumsum()
		plt.plot(x,cumgdd)
	plt.legend(leg,loc='upper left')
	ax = plt.gca()
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.yaxis.grid()
	ax.set_xlabel('Months', color='black', fontsize=16)
	ystring = 'Cumulative GDD (>' + str(tbase) + ')°C' 
	ax.set_ylabel(ystring, color='black', fontsize=16)
	plotTitle = 'Accumulated Growing Degree Days For - ' + str(stName)
	plt.title(plotTitle, color="black", fontsize=16)
	#plt.xlabel("Year/Time")
	#plt.ylabel("accumulated GDD")
	#plt.show()
	saveAs = './Plots/' + str(stName) + '.png'
	fig.savefig(saveAs)
	plt.gcf().clear()


stationRows = pd.read_csv('input.csv',skiprows=1,header=None)
stationRows.columns = ["StationID","StationName","TBase","TUpper"]
stationdIDs = np.array(stationRows["StationID"].values)
stationNames = np.array(stationRows["StationName"].values)
Tbase = np.array(stationRows.TBase.unique())
Tupper = np.array(stationRows.TUpper.unique())
Tbase = Tbase[0]
Tupper = Tupper[0]



for stid,stName in zip(stationdIDs,stationNames):
	fileNames = []
	for file in glob.glob('./Data/'+str(stid)+"-[0-9]*.csv"):
		if not '10_GDD' in file:
			continue
		fileNames.append(file)
	plot_GDD(fileNames,Tbase,Tupper,stName)
	#saveAs = '/Plots/' + str(stName) + '.png'
	#gddPlot.savefig(saveAs)