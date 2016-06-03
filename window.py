from PySide.QtCore import QRect
from PySide.QtGui import *
from Swiat import *
class MyWindow(QWidget):
    sx = 10
    sy = 10
    def buttonClick(self):
        print self.sender().objectName()
    def __init__(self):
        super(MyWindow, self).__init__()
        #self.installEventFilter(self)
    def keyPressEvent(self, event):
        key = event.key()
        print key
        self.swiat.UpdateLoop(key)
    def setSize(self,x,y):
        self.sizeX = x
        self.sizeY = y
    def Clear(self):
        for j in range(0, self.sizeY):
            for i in range(0, self.sizeX):
                self.hbox.itemAtPosition(i, j).widget().setStyleSheet(
                    "background-color: #FFF")
    def run(self):
        self.mbox = QGridLayout()
        self.hbox = QGridLayout()
        self.lbox = QGridLayout()
        label = QLabel('dupa')
        self.lbox.addWidget(label)
        self.hbox.setSpacing(0)

        for j in range(0, self.sizeY):
            for i in range(0, self.sizeX):
                button = QPushButton()
                button.setGeometry(QRect(0, 20, 20, 20))
                button.setStyleSheet("background-color: #FFF")
                button.setObjectName(str(j * 10 + i))
                button.setMaximumWidth(20)
                button.setMaximumHeight(20)
                #button.setFlat(True)
                button.clicked.connect(self.buttonClick)
                self.hbox.addWidget(button, j, i)
        self.mbox.addItem(self.hbox, 0, 0)
        self.mbox.addItem(self.lbox, 0, 1)
        self.setLayout(self.mbox)
        self.show()
