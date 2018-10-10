from constants.urls import flight_url, flights_from_session, flight_city_url
from constants.keys import MASHAPE_HOST, MASHAPE_KEY

from models.Flight.Leg import Leg
from models.Flight.Flight import Flight

import json
import requests
import re


class FlightService:

    def getCityCode(self, cityName, country, currency, locale):

        headers = {"X-Mashape-Key": MASHAPE_KEY,
                   "X-Mashape-Host": MASHAPE_HOST}

        cityResponse = json.loads(requests.get(flight_city_url(country, currency, locale, cityName), headers=headers).text)

        if len(cityResponse['Places']) > 0:
            return cityResponse['Places'][0]['PlaceId']
        return 'Invalid City'


    def createSession(self, country, currency, locale, origin, destination, outboundDate, inboundDate, cabinClass, adults, children, infants):

        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   "X-Mashape-Key": MASHAPE_KEY,
                   "X-Mashape-Host": MASHAPE_HOST}

        origin = self.getCityCode(origin, country, currency, locale)
        destination = self.getCityCode(destination, country, currency, locale)

        params = {'country': country,
                  'currency': currency,
                  'locale': locale,
                  'originPlace': origin,
                  'destinationPlace': destination,
                  'outboundDate': outboundDate,
                  'inboundDate': inboundDate,
                  'cabinClass': cabinClass,
                  'adults': adults,
                  'children': children,
                  'infants': infants,
                  'includeCarriers': '',
                  'excludeCarriers': ''}

        sessionResponse = requests.post(flight_url(), data=params, headers=headers)
        sessionId = re.search(r'/v1.0/(.*?)$', sessionResponse.headers.get('location')).group(1)
        return sessionId

    def getRoutesFromSession(self, sessionId):
        headers = {"X-Mashape-Key": MASHAPE_KEY,
                   "X-Mashape-Host": MASHAPE_HOST}

        flightsResponse = json.loads(requests.get(flights_from_session(sessionId), headers=headers).text)

        legs = {}
        for leg in flightsResponse["Legs"]:
            flightLeg = Leg(leg)
            for i in range(len(flightLeg.stops)):
                stop = flightLeg.stops[i]
                flightLeg.stops[i] = list(filter(lambda x: x['Id'] == stop, flightsResponse['Places']))[0]['Name']
            legs[leg["Id"]] = Leg(leg)

        response = {}
        flights = []
        for flight in flightsResponse["Itineraries"]:
            flights.append(Flight(flight, legs))

        response['flights'] = flights
        response['carriers'] = flightsResponse['Carriers']

        return json.dumps(response, default=ComplexHandler)


def ComplexHandler(Obj):
    if hasattr(Obj, 'jsonable'):
        return Obj.jsonable()


