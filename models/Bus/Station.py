class Station:
    id = ''
    relevance = 1.0
    name = 'Main Station'
    weight = 100

    @staticmethod
    def object_decoder(obj):
        station = Station()
        station.id = obj["id"]
        station.relevance = obj["relevance"]
        station.name = obj["name"]
        station.weight = obj["weight"]
        return station