from Organizm import *
import random
class Roslina(Organizm):
    @abstractmethod
    def akcja(self):
        x = random.randint(0, 100)
        if (x == 20):
            x, y = self.swiat.FreeSpaceP(self.posX, self.posY)
            orgType = type(self)
            org = orgType(self.swiat)
            self.swiat.AddOrganizm(org, x, y)
            return True
        pass
    @abstractmethod
    def kolizja(self):
        org = self.swiat.podajOrganizm(self.posX, self.posY)
        if (org.id != self.id):
            self.swiat.info.insert(len(self.swiat.info), "Organizm - " + org.name + " zjada " + self.name)
            #self.swiat.deleteOrganizm(org)
            self.swiat.deleteOrganizm(self)
        pass