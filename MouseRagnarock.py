# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from pymsgbox import *
from xml.dom import minidom
from random import *
from threading import Thread
import time
from yattag import Doc, indent

energy_max = 100


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.devicesbox = QtWidgets.QGroupBox(self.layoutWidget)
        self.devicesbox.setObjectName("devicesbox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.devicesbox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cheese_label = QtWidgets.QLabel(self.devicesbox)
        self.cheese_label.setObjectName("cheese_label")
        self.gridLayout_4.addWidget(self.cheese_label, 0, 0, 1, 1)
        self.board_label = QtWidgets.QLabel(self.devicesbox)
        self.board_label.setObjectName("board_label")
        self.gridLayout_4.addWidget(self.board_label, 1, 0, 1, 1)
        self.device_label = QtWidgets.QLabel(self.devicesbox)
        self.device_label.setObjectName("device_label")
        self.gridLayout_4.addWidget(self.device_label, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.devicesbox, 5, 3, 1, 1)
        self.MoneyBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.MoneyBox.setObjectName("MoneyBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MoneyBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.moneylabel = QtWidgets.QLabel(self.MoneyBox)
        self.moneylabel.setObjectName("moneylabel")
        self.gridLayout_2.addWidget(self.moneylabel, 1, 0, 1, 1)
        self.diamondslabel = QtWidgets.QLabel(self.MoneyBox)
        self.diamondslabel.setObjectName("diamondslabel")
        self.gridLayout_2.addWidget(self.diamondslabel, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.MoneyBox, 0, 3, 1, 1)
        self.switchbox = QtWidgets.QGroupBox(self.layoutWidget)
        self.switchbox.setObjectName("switchbox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.switchbox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cheese_button = QtWidgets.QPushButton(self.switchbox)
        self.cheese_button.setEnabled(False)
        self.cheese_button.setObjectName("cheese_button")
        self.gridLayout_5.addWidget(self.cheese_button, 0, 0, 1, 1)
        self.board_button = QtWidgets.QPushButton(self.switchbox)
        self.board_button.setEnabled(False)
        self.board_button.setObjectName("board_button")
        self.gridLayout_5.addWidget(self.board_button, 1, 0, 1, 1)
        self.device_button = QtWidgets.QPushButton(self.switchbox)
        self.device_button.setEnabled(False)
        self.device_button.setObjectName("device_button")
        self.gridLayout_5.addWidget(self.device_button, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.switchbox, 5, 2, 1, 1)
        self.mouseview = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouseview.sizePolicy().hasHeightForWidth())
        self.mouseview.setSizePolicy(sizePolicy)
        self.mouseview.setObjectName("mouseview")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.mouseview)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.mousecost = QtWidgets.QLabel(self.mouseview)
        self.mousecost.setObjectName("mousecost")
        self.gridLayout_6.addWidget(self.mousecost, 1, 1, 1, 1)
        self.mouse_image = QtWidgets.QGraphicsView(self.mouseview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouse_image.sizePolicy().hasHeightForWidth())
        self.mouse_image.setSizePolicy(sizePolicy)
        self.mouse_image.setObjectName("mouse_image")
        self.gridLayout_6.addWidget(self.mouse_image, 0, 0, 1, 1)
        self.mousename = QtWidgets.QLabel(self.mouseview)
        self.mousename.setObjectName("mousename")
        self.gridLayout_6.addWidget(self.mousename, 0, 1, 1, 1)
        self.mouseattachment = QtWidgets.QLabel(self.mouseview)
        self.mouseattachment.setObjectName("mouseattachment")
        self.gridLayout_6.addWidget(self.mouseattachment, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.mouseview, 7, 2, 1, 2)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 5, 0, 3, 2)
        self.clans = QtWidgets.QPushButton(self.layoutWidget)
        self.clans.setEnabled(False)
        self.clans.setObjectName("clans")
        self.gridLayout.addWidget(self.clans, 4, 3, 1, 1)
        self.pipe = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pipe.sizePolicy().hasHeightForWidth())
        self.pipe.setSizePolicy(sizePolicy)
        self.pipe.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pipe.setObjectName("pipe")
        self.gridLayout.addWidget(self.pipe, 0, 1, 1, 2)
        self.location_label = QtWidgets.QLabel(self.layoutWidget)
        self.location_label.setSizePolicy(sizePolicy)
        self.location_label.setMaximumSize(QtCore.QSize(6777215, 16777215))
        self.location_label.setObjectName("location_label")
        self.gridLayout.addWidget(self.location_label, 2, 0, 1, 2)
        self.energybar = QtWidgets.QProgressBar(self.layoutWidget)
        self.energybar.setProperty("value", 10)
        self.energybar.setObjectName("energybar")
        self.gridLayout.addWidget(self.energybar, 2, 1, 1, 2)
        self.move = QtWidgets.QPushButton(self.layoutWidget)
        self.move.setEnabled(False)
        self.move.setObjectName("move")
        self.gridLayout.addWidget(self.move, 4, 1, 1, 1)
        self.shop = QtWidgets.QPushButton(self.layoutWidget)
        self.shop.setObjectName("shop")
        self.gridLayout.addWidget(self.shop, 4, 2, 1, 1)
        self.inventory = QtWidgets.QPushButton(self.layoutWidget)
        self.inventory.setEnabled(False)
        self.inventory.setObjectName("inventory")
        self.gridLayout.addWidget(self.inventory, 4, 0, 1, 1)
        self.filler = QtWidgets.QLabel(self.layoutWidget)
        self.filler.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filler.sizePolicy().hasHeightForWidth())
        self.filler.setSizePolicy(sizePolicy)
        self.filler.setText("")
        self.filler.setObjectName("filler")
        self.gridLayout.addWidget(self.filler, 6, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.update_ui()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.devicesbox.setTitle(_translate("MainWindow", "Devices"))
        self.cheese_label.setText(_translate("MainWindow", "TextLabel"))
        self.board_label.setText(_translate("MainWindow", "TextLabel"))
        self.device_label.setText(_translate("MainWindow", "TextLabel"))
        self.MoneyBox.setTitle(_translate("MainWindow", "Money"))
        self.moneylabel.setText(_translate("MainWindow", "TextLabel"))
        self.diamondslabel.setText(_translate("MainWindow", "TextLabel"))
        self.switchbox.setTitle(_translate("MainWindow", "Devices"))
        self.cheese_button.setText(_translate("MainWindow", "Cheese"))
        self.board_button.setText(_translate("MainWindow", "Board"))
        self.device_button.setText(_translate("MainWindow", "Device"))
        self.mouseview.setTitle(_translate("MainWindow", "Journal"))
        self.mousecost.setText(_translate("MainWindow", "TextLabel"))
        self.mousename.setText(_translate("MainWindow", "TextLabel"))
        self.mouseattachment.setText(_translate("MainWindow", "TextLabel"))
        self.clans.setText(_translate("MainWindow", "Clans"))
        self.pipe.setText(_translate("MainWindow", "pipe"))
        self.move.setText(_translate("MainWindow", "Locations"))
        self.shop.setText(_translate("MainWindow", "Shop"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))
        self.location_label.setText(_translate("MainWindow", "Location"))

        self.pipe.clicked.connect(self.pipe_click)

    def catch_mouse(self):
        global money, cheese_amount, mouse_name, mouse_cost

        number = 1 + int(random()*10)

        mouse_name =  GameLogic.ReadXML(self, "mice", "name", number, 0)
        mouse_cost = GameLogic.ReadXML(self, "mice", "cost", number, 0)
        self.mousename.setText(mouse_name)
        self.mousecost.setText(mouse_cost)
        money += int(mouse_cost)
        self.moneylabel.setText(str(money))
        if money != 10:
            cheese_amount -= 1

    def update_ui(self):

        global energy
        self.energybar.setValue(energy)
        self.cheese_label.setText(cheese+" "+str(cheese_amount))
        self.diamondslabel.setText(str(diamonds))
        self.moneylabel.setText(str(money))
        self.mousename.setText(mouse_name)
        self.mousecost.setText(mouse_cost)
        self.location_label.setText(location_name)

    def pipe_click(self):

        global energy, energy_max

        if energy > 0 and cheese_amount > 0:
            energy -= 1
            self.catch_mouse()
        else:
            alert(text='Not enough energy or cheese', title='Alert', button='OK')

        if energy < energy_max:
            thread = EnergyThread()
            thread.start()

        self.update_ui()


class GameLogic(object):

    global energy, money

    def ReadXML(self, tag, name, number, index):
        xmldoc = minidom.parse('locations.xml')
        itemlist = xmldoc.getElementsByTagName(str(tag) + str(number))
        return itemlist[index].attributes[str(name)].value

    def ReadFile(self, position, index):
        xmldoc = minidom.parse('userdata.xml')
        itemlist = xmldoc.getElementsByTagName(str("user"))
        return itemlist[index].attributes[position].value

    def WriteFile(self):
        doc, tag, text = Doc().tagtext()
        with tag('user', energy=str(energy), location=str(location), money=str(money),
                 diamonds=str(diamonds), cheese=cheese,
                 cheese_amount=str(cheese_amount),
                 last_mouse=mouse_name, last_cost=mouse_cost):
            text(str(energy))

        result = indent(
            doc.getvalue(),
            indentation=' ' * 4,
            newline='\r\n')

        filename = 'userdata.xml'
        myfile = open(filename, 'w')
        myfile.write(result)
        myfile.close()
        print(result)


class EnergyThread(Thread):

    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        """Запуск потока"""
        global energy
        time.sleep(1)
        energy += 1
        #Ui_MainWindow.energybar.setText(str(energy))


energy = int(GameLogic.ReadFile(GameLogic, "energy", 0))
money = int(GameLogic.ReadFile(GameLogic, "money", 0))
diamonds = int(GameLogic.ReadFile(GameLogic, "diamonds", 0))
cheese = GameLogic.ReadFile(GameLogic, "cheese", 0)
cheese_amount = int(GameLogic.ReadFile(GameLogic, "cheese_amount", 0))
mouse_cost = GameLogic.ReadFile(GameLogic, "last_cost", 0)
mouse_name = GameLogic.ReadFile(GameLogic, "last_mouse", 0)
location = int(GameLogic.ReadFile(GameLogic, "location", 0))
location_name = GameLogic.ReadXML(GameLogic, "location", "name", location, 0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_(), GameLogic.WriteFile(GameLogic))
