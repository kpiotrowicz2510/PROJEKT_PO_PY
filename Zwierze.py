from Organizm import *
from abc import abstractmethod, ABCMeta
import random
class Zwierze(Organizm):
    @abstractmethod
    def akcja(self):
        x = random.randint(0,2)
        if(x==0):
            self.SetX(self.posX-1)
        if (x == 1):
            self.SetX(self.posX + 1)
        y = random.randint(0, 2)
        if (y == 0):
            self.SetY(self.posY - 1)
        if (y == 1):
            self.SetY(self.posY + 1)
        pass

    @abstractmethod
    def kolizja(self):
        org = self.swiat.podajOrganizm(self.posX, self.posY)
        if (self.swiat.FreeSpace(self.posX, self.posY) == False):
            if (self.id != org.id):
                if (org.color == self.color):
                    self.rozmnazanie()
                else:
                    self.walka(org)
    def rozmnazanie(self):
        x, y = self.swiat.FreeSpaceP(self.posX, self.posY)
        orgType = type(self)
        org = orgType(self.swiat)
        self.swiat.AddOrganizm(org,x,y)
        return True
    def walka(self,org):
        if(self.sila > org.sila):
            self.swiat.deleteOrganizm(org)
            self.swiat.info.insert(len(self.swiat.info), "Organizm - " + self.name + " zabija " +org.name)
        if (self.sila < org.sila):
            self.swiat.deleteOrganizm(self)
            self.swiat.info.insert(len(self.swiat.info),"Organizm - " + org.name + " zabija " +self.name)
        if (self.sila == org.sila):
            self.swiat.deleteOrganizm(org)
            self.swiat.info.insert(len(self.swiat.info),"Organizm - " + self.name + " zabija " +org.name)
    def uciekaj(self):
        self.SetX(self.last_posX)
        self.SetY(self.last_posY)