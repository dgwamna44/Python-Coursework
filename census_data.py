"""
Program: census_data.py
Author: Duroje Gwamna
Last Date Modified: 11/20/2021

This program will collect census data from a CSV file and
stores each record into a class based on the file's categories.

"""

import csv

def find_pop_and_household(data, county):
        print("The population for ", county, " County is: ", data[county]._population)
        print("The # of households for ", county, " County is: ", data[county]._households)

class County:
    def __init__(self, rank, county, per_capita, median_household_income,
                 median_family_income, population, households):

        self._rank = rank
        self._county = county
        self._per_capita = per_capita
        self._median_household_income = median_household_income
        self._median_family_income = median_family_income
        self._population = population
        self._households = households

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county_data={}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0 or row[1] == "United States" or row[1] == "Iowa State": # skip record altogether if United States/Iowa State is detected
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and its resspective rows as the data
        county_data[str(row[1])] = County(row[0],row[1],row[2],
                                          row[3],row[4],row[5],row[6])
        
    """finding population and # of households for Dallas county"""
    find_pop_and_household(county_data, "Dallas")

    """finding total population for Iowa"""
    pop_sum = 0
    for key in county_data:
        pop_sum += int(county_data[key]._population.replace(',','')) # removes commas replaces with nothing
    print("Total population is: ", pop_sum)

    

    
