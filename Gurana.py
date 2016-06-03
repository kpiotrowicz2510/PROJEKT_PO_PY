from Roslina import *
class Guarana(Roslina):
    def __init__(self,swiat):
        self.swiat = swiat
        self.inicjatywa = 0
        self.sila = 0
        self.name = "Guarana"
        self.color = "#0AF"
    def kolizja(self):
        org = self.swiat.podajOrganizm(self.posX, self.posY)
        if(org.id!=self.id and org.color != self.color):
            org.sila += 3
            self.swiat.deleteOrganizm(self.id)