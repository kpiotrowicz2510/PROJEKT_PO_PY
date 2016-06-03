from Zwierze import *
class Antylopa(Zwierze):
    def __init__(self,swiat):
        self.swiat = swiat
        self.inicjatywa = 4
        self.sila = 4
        self.color = "#FA0"
    def akcja(self):
        x = random.randint(0, 2)
        if (x == 1):
            self.SetX(self.posX - 2)
        if (x == 1):
            self.SetX(self.posX + 2)
        y = random.randint(0, 2)
        if (y == 1):
            self.SetY(self.posY - 2)
        if (y == 1):
            self.SetY(self.posY + 2)
        pass
    def kolizja(self):
        org = self.swiat.podajOrganizm(self.posX,self.posY)
        if(self.swiat.FreeSpace(self.posX,self.posY)==False):
            if(self.id!=org.id):
                if(org.color==self.color):
                    self.rozmnazanie()
                else:
                    x = random.randint(0, 2)
                    if(x==1):
                        self.walka(org)
                    else:
                        xGo,yGo = self.swiat.FreeSpaceP(self.posX,self.posY)
                        self.SetX(xGo)
                        self.SetY(yGo)
