import schiene

class TrainService:
    def getRoute(self):
        s = schiene.Schiene()
        asd = s.stations('Hamburg')
        asd2 = s.connections("Stuttgart HbF", "Berlin HbF")
        return "Available Routes"