#!/usr/bin/python

# Import PySide classes
import sys
from Swiat import *
def initialize():
    o = Czlowiek(swiat)
    swiat.AddOrganizm(o)
    swiat.czlowiek = o
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

# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it

mywin = MyWindow()

x, ok = QInputDialog.getText(mywin, 'Rozmiary', 'Podaj rozmiar X')
y, ok = QInputDialog.getText(mywin, 'Rozmiary', 'Podaj rozmiar Y')

swiat = Swiat()
swiat.SetWindow(mywin)
mywin.swiat = swiat
swiat.SetR(int(x),int(y))
mywin.run()
initialize()
swiat.UpdateLoop(1)

# Enter Qt application main loop
app.exec_()
sys.exit()