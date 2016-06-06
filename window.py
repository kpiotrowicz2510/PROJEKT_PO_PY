from PySide.QtCore import QRect
from PySide.QtGui import *
from Swiat import *
class MyWindow(QWidget):
    sx = 10
    sy = 10

    def buttonSave(self):
        self.swiat.Save()
    def buttonLoad(self):
        self.swiat.Load()
        self.close()
    def buttonClick(self):
        addOrg, ok = QInputDialog.getText(self, 'Dodaj organizm', 'Podaj nazwe organizmu:')
        number = int(self.sender().objectName())
        nx = 0
        ny = 0
        ny = int(number/self.sizeX)
        nx = number - ny*self.sizeX
        self.swiat.AddName(addOrg,ny, nx)
    def __init__(self):
        super(MyWindow, self).__init__()
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
        #label = QLabel('dupa')
        #self.lbox.addWidget(label)
        self.hbox.setSpacing(0)
        self.list = QListWidget(self)
        self.list.setMaximumHeight(150)
        self.list.scrollToBottom()
        self.setWindowTitle("Krzysztof Piotrowicz 160873")
        self.list.clear()
        for j in range(0, self.sizeY):
            for i in range(0, self.sizeX):
                button = QPushButton()
                button.setGeometry(QRect(0, 20, 20, 20))
                button.setStyleSheet("background-color: #FFF")
                button.setObjectName(str(j * self.sizeX + i))
                button.setMaximumWidth(20)
                button.setMaximumHeight(20)
                #button.setFlat(True)
                button.clicked.connect(self.buttonClick)
                self.hbox.addWidget(button, i, j)
        self.mbox.addItem(self.hbox, 0, 0)
        self.mbox.addItem(self.lbox, 0, 1)
        button = QPushButton()
        button.setText("Wczytaj")
        button.setMaximumWidth(150)
        button.clicked.connect(self.buttonLoad)
        self.lbox.addWidget(button,0,0)
        button = QPushButton()
        button.setText("Zapisz")
        button.setMaximumWidth(150)
        button.clicked.connect(self.buttonSave)
        self.lbox.addWidget(button, 1, 0)
        self.lbox.addWidget(self.list,2,0)
        self.setLayout(self.mbox)
        self.show()
        self.setFocus()
