from Roslina import *
import random
class Mlecz(Roslina):
    def __init__(self,swiat):
        self.swiat = swiat
        self.inicjatywa = 0
        self.sila = 0
        self.name = "Mlecz"
        self.color = "#FC0"
    def akcja(self):
        for i in range(0,3):
            x = random.randint(0, 100)
            if(x==20):
                x, y = self.swiat.FreeSpaceP(self.posX, self.posY)
                orgType = type(self)
                org = orgType(self.swiat)
                self.swiat.AddOrganizm(org,x,y)
                return True