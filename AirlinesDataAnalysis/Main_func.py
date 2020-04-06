# -*- coding: utf-8 -*-
"""
Employee Name: Ashish Kalra
Employee ID: 142968
Batch: GENESIS | Feb 2020
Date: 17 Feb 2020
"""
from Module import *

FILE = 'AirlinesData.csv'
DF = pd.read_csv(FILE, index_col=0)

print(DF.head(5))
print(DF.describe())
print(DF.columns)


def main():
    """
    This is the main function consisting of all the test cases
    """
    graph()
    assert len(findby_ID(5)) != 0, "Data does not exist"
    assert len(findby_Country("India")) != 0, "Data does not exist"
    assert len(findby_City("Delhi")) != 0, "Data does not exist"
    assert avail_Airports("India") > 0, "Data does not exist"
    assert max_Altitude("India") > 0, "Data does not exist"
    assert len(max_Airports()) != 0, "Data does not exist"
    assert air_Distance("Delhi", "Washington") > 0, "Data Does not exist"
    
    print("findbyID", findby_ID(5))
    #print(findby_ID(5))
    print("findbyCountry", findby_Country("India"))
    #print(findby_Country("India"))
    print("findbyCity", findby_City("Delhi"))
    #print(findby_City("Delhi"))
    print("Number of airports available in the country: ", avail_Airports("India"))
    #print(avail_Airports("India"))
    print("Number of airports available in the city: ", avail_Airports("Mumbai"))
    #print(avail_Airports("Mumbai"))
    print("Maximum number of Airports in:", max_Airports())
    #print(max_Airports())
    print("Highest altitude of an Airport in the country (feet): ", max_Altitude("India"))
    #print(max_Altitude("India"))
    print("Distance between Airports in the city(KM): ", air_Distance("Agra", "New York"))
    #print(air_Distance("Agra", "New York"))
    
if __name__ == '__main__':
    main()
