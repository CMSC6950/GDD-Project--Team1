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
    gdd['Data/Time'] = df['Date/Time']
    gdd.loc[gdd[0]<0, 0] = 0

    # Save GDD data
    year = df['Year'][0]
    prefix = infile.split('.')[0]
    outfile = prefix + '-GDD' + '.csv'
    gdd.to_csv(outfile, sep=',')
