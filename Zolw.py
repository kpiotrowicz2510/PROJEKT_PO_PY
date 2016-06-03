from Zwierze import *
class Zolw(Zwierze):
    def __init__(self,swiat):
        self.swiat = swiat
        self.inicjatywa = 1
        self.sila = 2
        self.name = "Zolw"
        self.color = "#F6F"
    def akcja(self):
        x = random.randint(0, 8)
        if (x == 6):
            self.SetX(self.posX - 1)
        if (x == 7):
            self.SetX(self.posX + 1)
        y = random.randint(0, 8)
        if (y == 6):
            self.SetY(self.posY - 1)
        if (y == 7):
            self.SetY(self.posY + 1)
    def kolizja(self):
        org = self.swiat.podajOrganizm(self.posX, self.posY)
        if (self.swiat.FreeSpace(self.posX, self.posY) == False):
            if (self.id != org.id):
                if (org.color == self.color):
                    self.rozmnazanie()
                else:
                    if(org.sila < 5):
                        self.uciekaj()
                    else:
                        self.walka(org)
