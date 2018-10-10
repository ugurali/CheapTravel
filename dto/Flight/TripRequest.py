class TripRequest:
    country = 'DE'
    currency = 'USD'
    locale = 'de-DE'
    origin = 'Munich'
    destination = 'Istanbul'
    outboundDate = '2018-04-13T10:30:00'
    inboundDate = '2018-04-13T10:30:00'
    cabinClass = 'economy'
    adults = '1'
    children = '0'
    infants = '0'

    @staticmethod
    def object_decoder(obj):
        tripRequest = TripRequest()
        tripRequest.country = obj["country"]
        tripRequest.currency = obj["currency"]
        tripRequest.locale = obj["locale"]
        tripRequest.origin = obj["origin"]
        tripRequest.destination = obj["destination"]
        tripRequest.outboundDate = obj["outboundDate"]
        tripRequest.inboundDate = obj["inboundDate"]
        tripRequest.cabinClass = obj["cabinClass"]
        tripRequest.adults = obj["adults"]
        tripRequest.children = obj["children"]
        tripRequest.infants = obj["infants"]
        return tripRequest
