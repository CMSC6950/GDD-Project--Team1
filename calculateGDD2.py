import pandas as pd
import os
import numpy as np
filepath = (os.getcwd()+'/Data/')
tbase = 10

def getAllFiles():
    files = os.listdir(filepath)
    return files

def calculateGDD(maxTemp, minTemp):
    GDD = [None] * len(maxTemp)
    GDD = ((maxTemp + minTemp)/2 -tbase)
    return GDD
    
def parseData(data, fileName):
    df = pd.DataFrame(data)
    maxTemp = df['Max_Temp']
    minTemp = df['Min_Temp']
    filepath = os.getcwd()+'/GDDResults/'
    GDDFileName = filepath + fileName + '.csv'
    GDDCalcTemp = []
    GDDRes = calculateGDD(maxTemp, minTemp)
    df["GDDCalcTemp"] = GDDRes
    with open(GDDFileName, 'w+') as datafile:
        df.to_csv(GDDFileName, sep=',', encoding='utf-8')       
    


def main():
    files = getAllFiles()
    if not os.path.exists('/GDDResults/'):
        os.mkdir('/GDDResults/')
    filepathNew = (os.getcwd()+'/GDDResults/')
    fileList = os.listdir(filepathNew)
    for filename in fileList:
        os.remove(filepathNew + "/"+filename)
    for file in files:
        data = pd.read_csv(filepath+file, header=0)
        df = pd.DataFrame(data)
        fileName = file.split('.')[0]
        parseData(data, fileName)
        
        
if __name__=='__main__':
    main()
