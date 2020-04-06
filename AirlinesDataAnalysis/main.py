# -*- coding: utf-8 -*-
"""
Employee Name: Ashish Kalra
Employee ID: 142968
Batch: GENESIS | Feb 2020
Date: 17 Feb 2020

@author: Ashish
"""

import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
#import matplotlib.pyplot as plt


FILE = 'AirlinesData.csv'
DF = pd.read_csv(FILE, index_col=0)

print(DF.head(5))
print(DF.describe())
print(DF.columns)

def main():
    """
    This is the main function consisting of all the test cases
    """
    print("findbyID")
    print(findby_ID(5))
    print("findbyCountry")
    print(findby_Country("India"))
    print("findbyCity")
    print(findby_City("Delhi"))
    print("Number of airports available in the country: ")
    print(avail_Airports("India"))
    print("Number of airports available in the city: ")
    print(avail_Airports("Mumbai"))
    print("Maximum number of Airports in:")
    print(max_Airports())
    print("Highest altitude of an Airport in the country (feet): ")
    print(max_Altitude("India"))
    print("Distance between Airports in the city:")
    print(air_Distance("Agra", "New York"))

def findby_ID(ID):
    #ID = int(input("Enter the Airline ID: "))
    attr = DF.loc[DF['Airline ID'] == ID]
    return attr

def findby_Country(destination):
    if destination in DF['Country'].unique():
        return DF[DF['Country'] == destination]
    else:
        return "Not Available"

def findby_City(destination):
    if destination in DF['City'].unique():
        return DF[DF['City'] == destination]
    else:
        return "Not Available"

def avail_Airports(destination):
    source_1 = DF["Country"].unique()
    source_2 = DF['City'].unique()
    if destination in source_1:
        return len(DF.loc[DF["Country"] == destination, "Name"])
    elif destination in source_2:
        return len(DF.loc[DF["City"] == destination, "Name"])
    else:
        return "No Airports available"

def max_Airports():
    L1 = []
    L2 = []
    def number_Airports():
        listCountry = DF['Country'].unique()
        for i in listCountry:
            L1.append(i)
            L2.append(avail_Airports(i))
    number_Airports()
    max_Airports = np.max(np.array(L2))
    top = L1[L2.index(max_Airports)]
    return top

# highest airport in a country
def max_Altitude(destination):
    highest = np.max(DF.loc[DF['Country'] == destination, "Altitude"])
    return highest

def air_Distance(destination1, destination2):
    Lat1 = DF.loc[DF["City"] == destination1, "Latitude"].iloc[0]
    Long1 = DF.loc[DF["City"] == destination1, "Longitude"].iloc[0]
    Lat2 = DF.loc[DF["City"] == destination2, "Latitude"].iloc[0]
    Long2 = DF.loc[DF["City"] == destination2, "Latitude"].iloc[0]
    def distance(lat1, long1, lat2, long2):
        long1 = radians(long1)
        long2 = radians(long2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        dlong = long2 - long1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlong / 2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r
    airDistance = distance(Lat1, Long1, Lat2, Long2)
    return airDistance

if __name__ == '__main__':
    main()
