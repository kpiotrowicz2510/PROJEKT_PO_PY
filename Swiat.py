import random
from window import *
class Swiat:
    pressedKey = -1
    turaNumer = 0
    sRX = 30
    sRY = 30
    newId = 0
    organizmy = []
    def __init__(self):
        self.organizmy = []
        self.info = []
    def SetR(self,x,y):
        self.sRX = x
        self.sRY = y
        self.window.setSize(x,y)
    def SetWindow(self, wind):
        self.window = wind

    def AddOrganizm(self,org):
        x = random.randint(0,self.sRX)
        y = random.randint(0,self.sRY)

    def AddOrganizm(self, org,x,y):
        org.posX = x
        org.posY = y
        org.id = self.newId
        self.organizmy.insert(self.newId,org)
        self.newId += 1
    def FreeSpace(self,x,y):
        ret = True
        for i in range(self.organizmy.count):
            if(self.organizmy[i].x==x and self.organizmy[i].y==y):
                ret=False
        return ret
    def UpdateLoop(self, key):
        self.WykonajTure(1)
        self.UpdateLog()
        self.RysujSwiat()
    def WykonajTure(self, key):
        return True
    def RysujSwiat(self):
        print len(self.organizmy)
        for i in range(0,len(self.organizmy)):
            self.window.hbox.itemAtPosition(self.organizmy[i].posX,self.organizmy[i].posY).widget().setStyleSheet("background-color: "+self.organizmy[i].color)
        return True
    def UpdateLog(self):
        return True

