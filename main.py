#!/usr/bin/python

# Import PySide classes
import sys
from Swiat import *
from Organizm import *
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it

mywin = MyWindow()
swiat = Swiat()
swiat.SetWindow(mywin)
swiat.SetR(20,20)
mywin.run()


o = Organizm(swiat)
o.posX = 1
o.posY = 2
swiat.AddOrganizm(o,1,2)

o = Organizm(swiat)
o.posX = 1
o.posY = 4
swiat.AddOrganizm(o,1,4)

swiat.UpdateLoop(1)

# Enter Qt application main loop
app.exec_()
sys.exit()