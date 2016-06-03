#!/usr/bin/python

# Import PySide classes
import sys

from Swiat import *
from Wilk import *
from Antylope import *
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it

mywin = MyWindow()
swiat = Swiat()
swiat.SetWindow(mywin)
swiat.SetR(20,20)
mywin.run()


o1 = Wilk(swiat)
o1.posX = 1
o1.posY = 2

swiat.AddOrganizm(o1,1,2)

o = Wilk(swiat)
o.posX = 1
o.posY = 4
swiat.AddOrganizm(o)

o = Antylopa(swiat)
swiat.AddOrganizm(o)

swiat.UpdateLoop(1)

# Enter Qt application main loop
app.exec_()
sys.exit()