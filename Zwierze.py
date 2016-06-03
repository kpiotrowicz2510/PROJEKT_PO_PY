from Organizm import *
from abc import abstractmethod, ABCMeta
import random
class Zwierze(Organizm):
    @abstractmethod
    def akcja(self):
        x = random.randint(0,2)
        if(x==1):
            self.SetX(self.posX-1)
        if (x == 1):
            self.SetX(self.posX + 1)
        y = random.randint(0, 2)
        if (y == 1):
            self.SetY(self.posY - 1)
        if (y == 1):
            self.SetY(self.posY + 1)
        pass

    @abstractmethod
    def kolizja(self):
        org = self.swiat
        pass
