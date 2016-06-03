from Roslina import *
class Jagody(Roslina):
    def __init__(self,swiat):
        self.swiat = swiat
        self.inicjatywa = 0
        self.sila = 99
        self.name = "Wilcze Jagody"
        self.color = "#0FF"

    def kolizja(self):
        org = self.swiat.podajOrganizm(self.posX, self.posY)
        if (org.id != self.id):
            self.swiat.info.insert(len(self.swiat.info), "Organizm - " + self.name + " zabija " + org.name)
            self.swiat.deleteOrganizm(org.id)
            self.swiat.deleteOrganizm(self.id)