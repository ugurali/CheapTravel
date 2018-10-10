class Trip:
    origin = ''
    destination = ''
    direct = True
    departure = '2018-09-13T00:30:00.000Z'
    arrival = '2018-09-13T12:00:00.000Z'
    legs = []
    price = 100
    currency = 'EUR'
    available = True

    def __init__(self):
        self.legs = []

    def jsonable(self):
        return self.__dict__

    @staticmethod
    def object_decoder(obj):
        busTrip = Trip()
        busTrip.origin = obj["origin"]["name"]
        busTrip.destination = obj["destination"]["name"]
        busTrip.direct = obj["direct"]
        busTrip.departure = obj["departure"]
        busTrip.arrival = obj["arrival"]
        busTrip.price = obj["price"]["amount"]
        busTrip.currency = obj["price"]["currency"]
        busTrip.available = obj["price"]["available"]
        for legTrip in obj["legs"]:
            busTrip.legs.append(Leg.object_decoder(legTrip))
        return busTrip


class Leg:
    origin = ''
    destination = ''
    departure = ''
    arrival = ''
    operator = ''

    def jsonable(self):
        return self.__dict__

    @staticmethod
    def object_decoder(obj):
        legTrip = Leg()
        legTrip.origin = obj["origin"]["name"]
        legTrip.destination = obj["destination"]["name"]
        legTrip.departure = obj["departure"]
        legTrip.arrival = obj["arrival"]
        legTrip.operator = obj["operator"]["name"]
        return legTrip
