class Carrier:
    id = '12312'
    code = 'TK'
    name = 'Turkish Airlines'
    imageUrl = 'http://s1.apideeplink.com/images/airlines/TK.png'

    def __init__(self, obj):
        self.id = obj["Id"]
        self.name = obj["Name"]
        self.imageUrl = obj["ImageUrl"]
        self.code = obj["DisplayCode"]

    def jsonable(self):
        return self.__dict__
