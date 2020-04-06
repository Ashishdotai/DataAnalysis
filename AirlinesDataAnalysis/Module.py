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
import seaborn as sns
import matplotlib.pyplot as plt
#from matplotlib.ticker import FuncFormatter

FILE = 'AirlinesData.csv'
DF = pd.read_csv(FILE, index_col=0)

def graph():
    L1 = []    
    L2 = []
    def number_Airports():
        listCountry = DF['Country'].unique()
        for i in listCountry:
            L1.append(i)
            L2.append(avail_Airports(i))
    number_Airports()
    #print(L1)
    #print(L2)
    #print(len(L1))
    #print(len(L2))
    #print(np.max(L2))
    #x = np.arange(len(L1))
    x = np.linspace(0, len(L1), len(L1))
    plt.bar(x, height = L2, tick_label=L1, width=1.8, bottom=None, align='center', data=None)
    plt.xlabel("Country")
    plt.xticks(rotation = 90)
    plt.ylabel("Number of Airports")
    sns.barplot(x, L2)
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