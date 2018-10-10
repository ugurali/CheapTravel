class TripRequest:
    source = ''
    destination = ''
    roundTrip = True
    departureDate = '2018-04-13T10:30:00'
    returnDate = '2018-04-13T10:30:00'
    adults = 1
    children = 0

    @staticmethod
    def object_decoder(obj):
        tripRequest = TripRequest()
        tripRequest.source = obj["source"]
        tripRequest.destination = obj["destination"]
        tripRequest.roundTrip = obj["roundTrip"]
        tripRequest.departureDate = obj["departureDate"]
        tripRequest.returnDate = obj["returnDate"]
        tripRequest.adults = obj["adults"]
        tripRequest.children = obj["children"]
        return tripRequest
