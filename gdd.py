import pandas as pd
import numpy as np
import sys

if __name__ == "__main__":
    tbase = int(sys.argv[2])
    tupper = int(sys.argv[3])
    infile = sys.argv[1]
    
    df = pd.read_csv(infile,index_col=0)
    date = df['Date/Time']
    
    higher_than_upper_index = (df['Max_Temp']>tupper)
    lower_than_base_index = (df['Min_Temp']<tbase)
    
    df.loc[higher_than_upper_index,'Min_Temp'] = tupper
    df.loc[lower_than_base_index,'Min_Temp'] = tbase
    
    gdd = ((df['Max_Temp'] + df['Min_Temp'])/2 - tbase).to_frame()
    cumgdd = gdd.cumsum()
    cumgdd.columns = ['Cumulative GDD']
    cumgdd.index = date
    
    year = df['Year'][0]
    descrp = 'Cumulative_GDD_' + str(year)
    cumgdd.to_hdf('Data/' + descrp + '.h5', descrp, format='table', mode='w')
