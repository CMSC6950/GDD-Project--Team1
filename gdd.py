import pandas as pd
import numpy as np
import sys
#import pdb

'''
This script calculates the daily GDD and
save the results to a csv file.
'''

if __name__ == "__main__":
    tbase = int(sys.argv[2])
    tupper = int(sys.argv[3])
    infile = sys.argv[1]

#    pdb.set_trace()

    df = pd.read_csv(infile,index_col=0)
    date = df['Date/Time']

    df.loc[df['Max_Temp']>tupper,'Max_Temp'] = tupper
    df.loc[df['Min_Temp']<tbase,'Min_Temp'] = tbase

    # Calculate daily growing degrees
    gdd = ((df['Max_Temp'] + df['Min_Temp'])/2 - tbase).to_frame()
    gdd.loc[gdd[0]<0, 0] = 0
    gdd.columns = ["Daily GDD"]
    gdd.index = date

    # Save GDD data
    year = df['Year'][0]
    prefix = infile.split('.')[0]
    if tbase != 10:
        outfile = prefix + '_base_' + str(tbase) + ' _GDD' + '.csv'
    else:
        outfile = prefix + '_GDD' + '.csv'
    gdd.to_csv(outfile, sep=',')


# used only by the test suite(pytest)
def gddCal(maxTemp,minTemp,tbase,tupper):
	print('Running Test for GDD calculation')
	if maxTemp > tupper:
		maxTemp = tupper
	if minTemp < tbase:
		minTemp = tbase
	gdd = (maxTemp + minTemp)/2 - tbase
	if gdd < 0:
		return 0
	else:
		return gdd
