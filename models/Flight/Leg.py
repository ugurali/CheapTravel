class Leg:
    id = '12312-1231231-123123'
    direction = 'Outbound' #Inbound
    stops = []
    flightNumbers = []
    duration = 120
    departure = '2018-11-01T14:45:00'
    arrival = '2018-11-01T14:45:00'
    name = 'Turkish Airlines'
    imageUrl = 'http://s1.apideeplink.com/images/airlines/TK.png'

    def __init__(self, obj):
        self.id = obj["Id"]
        self.flightNumbers = obj["FlightNumbers"]
        self.duration = obj["Duration"]
        self.stops = obj["Stops"]
        self.departure = obj["Departure"]
        self.arrival = obj["Arrival"]

    def jsonable(self):
        return self.__dict__