import random
from window import *
from Wilk import *
from Antylope import *
from Czlowiek import *
from Gurana import *
from Jagody import *
from Lis import *
from Mlecz import *
from Owca import *
from Trawa import *
from Zolw import *

class Swiat:
    pressedKey = -1
    turaNumer = 0
    sRX = 30
    sRY = 30
    newId = 0
    organizmy = []
    czlowiek = 0
    def __init__(self):
        self.organizmy = []
        self.info = []
    def SetR(self,x,y):
        if x < 1 or y < 1:
            raise RuntimeError
            return
        self.sRX = x
        self.sRY = y
        self.window.setSize(x,y)
    def SetWindow(self, wind):
        self.window = wind
    def Save(self):
        file_ = open('world.txt', 'w')
        file_.write(str(self.sRX) + " ")
        file_.write(str(self.sRY) + " ")
        file_.write(str(self.newId)+" ")
        file_.write(str(self.turaNumer) + " ")
        file_.write(str(len(self.organizmy))+" ")
        for i in range(0, len(self.organizmy)):
            file_.write(str(self.organizmy[i].id)+ " ")
            file_.write(str(self.organizmy[i].name) + " ")
            file_.write(str(self.organizmy[i].color) + " ")
            file_.write(str(self.organizmy[i].inicjatywa) + " ")
            file_.write(str(self.organizmy[i].sila) + " ")
            file_.write(str(self.organizmy[i].posX) + " ")
            file_.write(str(self.organizmy[i].posY) + " ")
        file_.close()
        self.info.insert(len(self.info), "Zapisano do pliku!")
    def Load(self):
        file_ = open('world.txt','r')
        text = file_.read()
        lista = text.split(" ")
        del self.organizmy[:]
        del self.info[:]
        rx = int(lista[0])
        ry = int(lista[1])
        self.SetR(rx,ry)

        nid = int(lista[2])
        tura = int(lista[3])
        os = int(lista[4])
        self.turaNumer = tura
        self.newId = nid
        start = 5
        for i in range(0,os):
            id = int(lista[start])
            name = lista[start+1]
            color = lista[start+2]
            inicjatywa = int(lista[start+3])
            sila = int(lista[start+4])
            x = int(lista[start+5])
            y = int(lista[start+6])

            o = None
            if (name == "Antylopa"):
                o = Antylopa(self)
            if (name == "Guarana"):
                o = Guarana(self)
            if (name == "Jagody"):
                o = Jagody(self)
            if (name == "Lis"):
                o = Lis(self)
            if (name == "Mlecz"):
                o = Mlecz(self)
            if (name == "Owca"):
                o = Owca(self)
            if (name == "Trawa"):
                o = Trawa(self)
            if (name == "Wilk"):
                o = Wilk(self)
            if (name == "Zolw"):
                o = Zolw(self)
            if(name=="Czlowiek"):
                o=Czlowiek(self)
                self.czlowiek = o
            if (o != None):
                o.sila = sila
                o.posX = x
                o.id = id
                o.posY = y
                self.AddOrganizm(o, x, y)
            start+=7
        self.info.insert(len(self.info), "Wczytano z pliku!")
        self.window=None
        mywin = MyWindow()
        self.SetWindow(mywin)
        self.window.swiat = self
        self.window.setSize(rx, ry)
        self.window.run()
        self.RysujSwiat()
        self.UpdateLog()

    def AddName(self,name,x,y):
        o = None
        if (name == "A"):
            o = Antylopa(self)
        if (name == "G"):
            o = Guarana(self)
        if (name == "J"):
            o = Jagody(self)
        if (name == "L"):
            o = Lis(self)
        if (name == "M"):
            o = Mlecz(self)
        if (name == "O"):
            o = Owca(self)
        if (name == "T"):
            o = Trawa(self)
        if (name == "W"):
            o = Wilk(self)
        if (name == "Z"):
            o = Zolw(self)
        if(o!=None):
            self.AddOrganizm(o, x,y)
        self.RysujSwiat()
    def AddOrganizm(self,org):
        x = random.randint(0,self.sRX-1)
        y = random.randint(0,self.sRY-1)
        if (self.FreeSpace(x, y) == False):
            return
        org.posX = x
        org.posY = y
        org.id = self.newId
        self.organizmy.insert(self.newId,org)
        self.newId+=1
        self.info.insert(len(self.info), "Dodano organizm - " + org.name)

    def AddOrganizm(self, org,x=-1,y=-1):
        if(x>-1 and y>-1):
            org.posX = x
            org.posY = y
        else:
            x = random.randint(0, self.sRX-1)
            y = random.randint(0, self.sRY-1)
            org.posX = x
            org.posY = y
        if(self.FreeSpace(x,y)==False):
            return
        org.id = self.newId
        self.organizmy.insert(self.newId,org)
        self.newId += 1
        self.info.insert(len(self.info), "Dodano organizm - " + org.name)
    def FreeSpace(self,x,y):
        for i in range(len(self.organizmy)):
            if(self.organizmy[i].posX==x and self.organizmy[i].posY==y):
                return False
        return True
    def FreeSpaceP(self,x2,y2):
        xs = 0;
        ys = 0;
        if (x2 == 0):
            xs = 1

        if (y2 == 0):
            ys = 1

        for y in range(-1+ys, 2+ys):
            for x in range(-1+xs, 2+xs):
                if (self.FreeSpace((x2 + x), (y2 + y))):
                    yield x2+x
                    yield y2+y
                    return

        yield -1
        yield -1

    def podajOrganizm(self,x,y):
        for i in range(0,len(self.organizmy)):
            if(self.organizmy[i].posX==x and self.organizmy[i].posY==y):
                return self.organizmy[i]
        return False
    def UpdateLoop(self, key):
        self.WykonajTure(key)
        self.UpdateLog()
        self.window.Clear()
        self.RysujSwiat()
    def WykonajTure(self, key):
        if(key==65):
            self.pressedKey = 2
        if key == 68:
            self.pressedKey = 3
        if (key == 87):
            self.pressedKey = 0
        if (key == 83):
            self.pressedKey = 1
        if (key == 85):
            self.pressedKey = 4
        k = len(self.organizmy)-1
        try:
            for i in range(0,k):
                self.organizmy[i].akcja()
                self.organizmy[i].kolizja()
                k = len(self.organizmy)-1
        except IndexError:
            print "Cos poszlo nie tak"
        self.turaNumer += 1
        return True
    def RysujSwiat(self):
        #print len(self.organizmy)
        for i in range(0,len(self.organizmy)):
            if(self.window.hbox.itemAtPosition(self.organizmy[i].posX,self.organizmy[i].posY)!=None):
                self.window.hbox.itemAtPosition(self.organizmy[i].posX,self.organizmy[i].posY).widget().setStyleSheet("background-color: "+self.organizmy[i].color)
        return True
    def UpdateLog(self):
        #print "INFO" + str(len(self.info))
        self.window.list.clear()
        for i in range(0,len(self.info)):
            self.window.list.addItem( QListWidgetItem(self.info[i]))
        self.window.list.scrollToBottom()
    def deleteOrganizm(self,org):
        self.organizmy.remove(org)