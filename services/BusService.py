from models.Bus.Trip import Trip
from models.Bus.Station import Station

from constants.urls import route_url, station_url

import requests
import json


class BusService:

    def getRoute(self, source, destination, date, adults, children):
        trips = requests.get(route_url(source, destination, date, adults, children))
        allTrips = []
        for trip in json.loads(trips.text):
            allTrips.append(Trip.object_decoder(trip))

        return json.dumps(allTrips, default=ComplexHandler)

    def getStationId(self, name):
        stations = requests.get(station_url(name))
        allStations = []
        for station in json.loads(stations.text):
            allStations.append(Station.object_decoder(station))

        allStations.sort(key=lambda x: x.weight, reverse=True)
        return allStations[0].id if allStations else 0


def ComplexHandler(Obj):
    if hasattr(Obj, 'jsonable'):
        return Obj.jsonable()
