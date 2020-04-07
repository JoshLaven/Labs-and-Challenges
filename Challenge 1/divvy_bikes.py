import json
import requests

gbfs_resp = requests.get('https://gbfs.divvybikes.com/gbfs/fr/station_status.json')
gbfs_json = json.loads(gbfs_resp.text)

divvy_stations = gbfs_json['data']['stations']

with open('divvy_bikes.txt', 'w') as json_file:
  json.dump(divvy_stations, json_file)


# find average number of empty docks and available bikes


# find ratio of bikes that are currently rented to total bikes in the system
