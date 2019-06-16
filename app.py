
import requests
import os
import sys
from datetime import datetime


bikeApi = requests.get("http://data.foli.fi/citybike")
try:
    bikeApi.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
# request api
bikeStations = bikeApi.json()

# while loop for keep program going
letsQuit = False
homeStation = "Merimiehenkatu"
timestamp = bikeStations["lastupdate"]
dt_object = datetime.fromtimestamp(timestamp)
print(f"Bikes info last updated: {dt_object}")
print("::::station name example: (Merimiehenkatu)")
print("::::all: check all stations")
print("::::home: check home station")
print("::::quit: quit program")
while letsQuit == False:
    print("Please type param")
    answer = input()
    if answer == "quit":
        letsQuit = True
        break
    elif answer == "all":
        for station in bikeStations["racks"]:
            stationName = bikeStations["racks"][station]["name"]
            bikesAvail = bikeStations["racks"][station]["bikes_avail"]
            slotsTotal = bikeStations["racks"][station]["slots_total"]
            print(f">>>>>{stationName} {bikesAvail}/{slotsTotal}")
    elif answer == "home":
        found = False
        for station in bikeStations["racks"]:
            stationName = bikeStations["racks"][station]["name"]
            if stationName == homeStation:
                bikesAvail = bikeStations["racks"][station]["bikes_avail"]
                slotsTotal = bikeStations["racks"][station]["slots_total"]
                print(f">>>>>{stationName} {bikesAvail}/{slotsTotal}")
                found = True
                break
        if found == False:
            print("home stattion not found")

    else:
        found = False
        for station in bikeStations["racks"]:
            stationName = bikeStations["racks"][station]["name"]
            if stationName == answer:
                bikesAvail = bikeStations["racks"][station]["bikes_avail"]
                slotsTotal = bikeStations["racks"][station]["slots_total"]
                print(f"{stationName} {bikesAvail}/{slotsTotal}")
                found = True
                break
        if found == False:
            print("Station not found")

    print(":::::::::::::::::")

""" for station in bikeStations.racks.values():
    print(station.name) """

# print(bikeStations)

# make list of all stations
