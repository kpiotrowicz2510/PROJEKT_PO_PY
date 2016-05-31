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

    def __init__(self, swiatd):
        self.swiat = swiatd
        self.posX = 0
        self.posY = 0
        self.color = "#00F"
    @abstractmethod
    def akcja(self):
        pass
    @abstractmethod
    def kolizja(self):
        pass