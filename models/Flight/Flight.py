class Flight:
    outbound = ''
    inbound = ''
    price = 100
    url = 'www.example.com'

    def __init__(self, obj, legDict):
        self.outbound = legDict.get(obj['OutboundLegId'])
        self.inbound = legDict.get(obj['InboundLegId'])
        self.price = obj['PricingOptions'][0]['Price']
        self.url = obj['PricingOptions'][0]['DeeplinkUrl']

    def jsonable(self):
        return self.__dict__