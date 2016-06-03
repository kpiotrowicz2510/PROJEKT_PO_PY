from Zwierze import *
class Lis(Zwierze):
    def __init__(self,swiat):
        self.swiat = swiat
        self.inicjatywa = 7
        self.sila = 3
        self.name = "Lis"
        self.color = "#00F"

    def akcja(self):
        moveX = 0
        moveY = 0
        x = random.randint(0, 2)
        if (x == 0):
          moveX = self.posX - 1
        if (x == 1):
           moveX  = self.posX + 1
        y = random.randint(0, 2)
        if (y == 0):
           moveY = self.posY - 1
        if (y == 1):
           moveY = self.posY + 1
        org = self.swiat.podajOrganizm(moveX, moveY)
        if(org==False):
            self.SetX(moveX)
            self.SetY(moveY)
        else:
            if(org.sila > self.sila):
                self.akcja()
            else:
                self.SetX(moveX)
                self.SetY(moveY)
