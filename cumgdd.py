import pandas as pd
import numpy as np
import sys
#import pdb

'''
This script calculates the cumulative GDD and
save the results to a csv file.
'''

def cumgdd(infile, tbase, tupper):
#    pdb.set_trace()
    
    df = pd.read_csv(infile,index_col=0)
    date = df['Date/Time']
    
    df.loc[df['Max_Temp']>tupper,'Max_Temp'] = tupper
    df.loc[df['Min_Temp']<tbase,'Min_Temp'] = tbase
    # Calculate daily growing degrees
    gdd = ((df['Max_Temp'] + df['Min_Temp'])/2 - tbase).to_frame()
    gdd.loc[gdd[0]<0, 0] = 0
    # Compute cumulative GDD and reset index to date
    cumgdd = gdd.cumsum()
    cumgdd.columns = ['Cumulative GDD']
    cumgdd.index = date

    # Save GDD data
#    year = df['Year'][0]
#    prefix = infile.split('.')[0]
#    outfile = prefix + '_CumGDD' + '.csv'
#    cumgdd.to_csv(outfile, sep=',')

    return cumgdd.iloc[-1,0]
