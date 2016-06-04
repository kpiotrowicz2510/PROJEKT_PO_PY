from abc import abstractmethod, ABCMeta
class Organizm(object):
    sila=0
    inicjatywa=0
    color=0
    id=0
    posX=0
    posY=0
    last_posX=0
    last_posY=0
    name=""

    def __init__(self, swiatd):
        self.swiat = swiatd
        self.posX = 0
        self.posY = 0
        self.color = "#00F"
    def SetX(self,x):
        if(x>-1 and self.swiat.sRX >= x):
            self.last_posX = self.posX
            self.posX = x

    def SetY(self, y):
        if (y > -1 and self.swiat.sRY >= y):
            self.last_posY = self.posY
            self.posY = y
    @abstractmethod
    def akcja(self):
        pass
    @abstractmethod
    def kolizja(self):
        pass