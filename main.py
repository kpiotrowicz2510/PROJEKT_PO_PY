#!/usr/bin/python

# Import PySide classes
import sys

from Swiat import *
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

def initialize():
    o = Wilk(swiat)
    swiat.AddOrganizm(o)
    o = Wilk(swiat)
    swiat.AddOrganizm(o)
    o = Antylopa(swiat)
    swiat.AddOrganizm(o)
    o = Antylopa(swiat)
    swiat.AddOrganizm(o)
    o = Guarana(swiat)
    swiat.AddOrganizm(o)
    o = Guarana(swiat)
    swiat.AddOrganizm(o)
    o = Jagody(swiat)
    swiat.AddOrganizm(o)
    o = Jagody(swiat)
    swiat.AddOrganizm(o)
    o = Lis(swiat)
    swiat.AddOrganizm(o)
    o = Lis(swiat)
    swiat.AddOrganizm(o)
    o = Mlecz(swiat)
    swiat.AddOrganizm(o)
    o = Mlecz(swiat)
    swiat.AddOrganizm(o)
    o = Owca(swiat)
    swiat.AddOrganizm(o)
    o = Owca(swiat)
    swiat.AddOrganizm(o)
    o = Trawa(swiat)
    swiat.AddOrganizm(o)
    o = Trawa(swiat)
    swiat.AddOrganizm(o)
    o = Zolw(swiat)
    swiat.AddOrganizm(o)
    o = Zolw(swiat)
    swiat.AddOrganizm(o)

    o = Czlowiek(swiat)
    swiat.AddOrganizm(o)
    swiat.czlowiek = o
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it

mywin = MyWindow()
swiat = Swiat()
swiat.SetWindow(mywin)
mywin.swiat = swiat
swiat.SetR(20,20)
mywin.run()

initialize()
swiat.UpdateLoop(1)

# Enter Qt application main loop
app.exec_()
sys.exit()