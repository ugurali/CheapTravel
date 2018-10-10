# Busses
BUS_STATION_URL = 'https://1.flixbus.transport.rest/stations/?query={0}'
BUS_ROUTE_URL = 'https://1.flixbus.transport.rest/journeys/?origin={0}&destination={1}&date={2}&adults={3}&children={4}'

# Flights
CREATE_FLIGHT_SESSION = 'https://skyscanner-skyscanner-flight-search-v1.p.mashape.com/apiservices/pricing/v1.0/'
FLIGHTS_FROM_SESSION = 'https://skyscanner-skyscanner-flight-search-v1.p.mashape.com/apiservices/pricing/uk2/v1.0/{0}?pageIndex=0&pageSize=10'
FLIGHT_CITY_CODE = 'https://skyscanner-skyscanner-flight-search-v1.p.mashape.com/apiservices/autosuggest/v1.0/{0}/{1}/{2}/?query={3}'

def flight_city_url(country, currency, locale, cityName):
    return FLIGHT_CITY_CODE.format(country, currency, locale, cityName)

def flight_url():
    return CREATE_FLIGHT_SESSION


def flights_from_session(sessionId):
    return FLIGHTS_FROM_SESSION.format(sessionId)


def route_url(origin, destination, date, adults, children):
    return BUS_ROUTE_URL.format(origin, destination, date, adults, children)


def station_url(name):
    return BUS_STATION_URL.format(name)


