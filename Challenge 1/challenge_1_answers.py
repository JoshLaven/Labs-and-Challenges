# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks and available bikes at each station
num_docks = 0

for i in range(len(divvy_stations)):
    num_docks += divvy_stations[i]['num_docks_available']

average_docks = num_docks / len(divvy_stations)
average_docks

num_bikes = 0

for i in range(len(divvy_stations)):
    num_bikes += divvy_stations[i]['num_bikes_available']

average_bikes = num_bikes / len(divvy_stations)
average_bikes

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system
total_docks = 0

for i in range(len(divvy_stations)):
    total_docks += divvy_stations[i]['num_docks_available'] + \
                   divvy_stations[i]['num_bikes_available']

proportion_rented = 1 - (num_docks / total_docks)
proportion_rented

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station. 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

for d in divvy_stations:
    d['percent_bikes_remaining'] = '{0:.{1}f}%'.format(((d['num_bikes_available'] / \
                          (d['num_docks_available'] + d['num_bikes_available']))) * 100, 2)

divvy_stations[0]
