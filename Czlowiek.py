from Zwierze import *
class Czlowiek(Zwierze):
    key = 0
    turaAktywacji = 0
    coolDown = 0
    special = False
    def __init__(self,swiat):
        self.swiat = swiat
        self.inicjatywa = 4
        self.sila = 5
        self.name = "Czlowiek"
        self.color = "#F00"
    def akcja(self):
        key = self.swiat.pressedKey
        if(key==4 and self.special == False and self.coolDown):
            self.swiat.info.insert(len(self.swiat.info),"Tarcza Alzura aktywowana!")
            self.special = True
            self.turaAktywacji = self.swiat.turaNumer
        if(self.swiat.turaNumer - self.turaAktywacji > 5 and self.special == True):
            self.special = False
            self.coolDown = 5
            self.swiat.info.insert(len(self.swiat.info), "Tarcza Alzura dezaktywowana!")
        if(self.coolDown > 0):
            self.coolDown -= 1

        x = self.posX
        y = self.posY
        gx = self.posX
        gy = self.posY

        if(x-1 > 0 and key==0):
            self.SetX(gx-1)
            return
        if(x+1 <= self.swiat.sRX):
            self.SetX(gx+1)
            return
        if (y - 1 >= 0):
            self.SetY(gy - 1)
            return
        if (y + 1 <= self.swiat.sRY):
            self.SetY(gy + 1)
            return