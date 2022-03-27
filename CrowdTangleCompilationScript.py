### Aaraj Vij
### 03/25/2022
### This script compiles CrowdTangle data of the
### same Country AND Topic/Tag into one .csv file

import csv
import os
from unittest import result
import pandas as pd

os.chdir("FILE PATH HERE") # Set directory to location of CrowdTangle data files

dfList = [] # Used at end to construct compiled DF

for file in os.listdir(os.curdir): # Iterate through each file in directory
    print(file)
    dataDF = pd.read_csv(file, header = 3) # Create a DataFrame from that file
    
    with open(file, encoding="utf-8") as csv_file: # Propagate DataFrame with Article Link and Facebook interaction data
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        dataDF["Article Link"] = csv_reader[0][0].split(": ")[1]
        dataDF[csv_reader[1][0]] = csv_reader[2][0]
        dataDF[csv_reader[1][1]] = csv_reader[2][1]
        dataDF[csv_reader[1][2]] = csv_reader[2][2]
        dataDF[csv_reader[1][3]] = csv_reader[2][3]
    
    dfList.append(dataDF) # Add dataframe to compiled list
    print(dfList)

resultDF = pd.concat(dfList) # Concatenate to form compiled DataFrame

resultDF.to_csv("FILE PATH HERE") # Save compiled DataFrame as .csv file