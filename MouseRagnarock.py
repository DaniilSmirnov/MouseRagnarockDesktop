# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from pymsgbox import *
from xml.dom import minidom
from random import *
from threading import Thread
import time
from yattag import Doc, indent

#energy = 1
energy_max = 100


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.devicesbox = QtWidgets.QGroupBox(self.widget)
        self.devicesbox.setObjectName("devicesbox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.devicesbox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.devicesbox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.devicesbox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.devicesbox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.gridLayout.addWidget(self.devicesbox, 5, 3, 1, 1)
        self.MoneyBox = QtWidgets.QGroupBox(self.widget)
        self.MoneyBox.setObjectName("MoneyBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MoneyBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.moneylabel = QtWidgets.QLabel(self.MoneyBox)
        self.moneylabel.setObjectName("label")
        self.gridLayout_2.addWidget(self.moneylabel, 1, 0, 1, 1)
        self.diamondslabel = QtWidgets.QLabel(self.MoneyBox)
        self.diamondslabel.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.diamondslabel, 2, 0, 1, 1)
        self.diamondslabel.raise_()
        self.moneylabel.raise_()
        self.diamondslabel.raise_()
        self.gridLayout.addWidget(self.MoneyBox, 0, 3, 1, 1)
        self.switchbox = QtWidgets.QGroupBox(self.widget)
        self.switchbox.setObjectName("switchbox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.switchbox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.switchbox)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_5.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.switchbox)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.switchbox)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_5.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.switchbox, 5, 2, 1, 1)
        self.mouseview = QtWidgets.QGroupBox(self.widget)
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
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 5, 0, 3, 2)
        self.clans = QtWidgets.QPushButton(self.widget)
        self.clans.setEnabled(False)
        self.clans.setObjectName("clans")
        self.gridLayout.addWidget(self.clans, 4, 3, 1, 1)
        self.pipe = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pipe.sizePolicy().hasHeightForWidth())
        self.pipe.setSizePolicy(sizePolicy)
        self.pipe.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pipe.setObjectName("pipe")
        self.gridLayout.addWidget(self.pipe, 0, 1, 1, 2)
        self.energybar = QtWidgets.QProgressBar(self.widget)
        self.energybar.setProperty("value", 10)
        self.energybar.setObjectName("energybar")
        self.gridLayout.addWidget(self.energybar, 2, 1, 1, 2)
        self.move = QtWidgets.QPushButton(self.widget)
        self.move.setObjectName("move")
        self.gridLayout.addWidget(self.move, 4, 1, 1, 1)
        self.shop = QtWidgets.QPushButton(self.widget)
        self.shop.setEnabled(False)
        self.shop.setObjectName("shop")
        self.gridLayout.addWidget(self.shop, 4, 2, 1, 1)
        self.inventory = QtWidgets.QPushButton(self.widget)
        self.inventory.setEnabled(False)
        self.inventory.setObjectName("inventory")
        self.gridLayout.addWidget(self.inventory, 4, 0, 1, 1)
        self.filler = QtWidgets.QLabel(self.widget)
        self.filler.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filler.sizePolicy().hasHeightForWidth())
        self.filler.setSizePolicy(sizePolicy)
        self.filler.setText("")
        self.filler.setObjectName("filler")
        self.gridLayout.addWidget(self.filler, 6, 2, 1, 2)
        self.mouseview.raise_()
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.devicesbox.setTitle(_translate("MainWindow", "Devices"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.MoneyBox.setTitle(_translate("MainWindow", "Money"))
        self.moneylabel.setText(_translate("MainWindow", " "))
        self.diamondslabel.setText(_translate("MainWindow", " "))
        self.switchbox.setTitle(_translate("MainWindow", "Devices"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.mouseview.setTitle(_translate("MainWindow", "Journal"))
        self.mousecost.setText(_translate("MainWindow", " "))
        self.mousename.setText(_translate("MainWindow", " "))
        self.mouseattachment.setText(_translate("MainWindow", "TextLabel"))
        self.clans.setText(_translate("MainWindow", "Clans"))
        self.pipe.setText(_translate("MainWindow", "pipe"))
        self.move.setText(_translate("MainWindow", "Locations"))
        self.shop.setText(_translate("MainWindow", "Shop"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))

        self.pipe.clicked.connect(self.pipe_click)

    def catch_mouse(self):
        global money

        number = 1 + int(random()*10)

        self.mousename.setText(GameLogic.ReadXML(self, "mice", "name", number, 0))
        self.mousecost.setText(GameLogic.ReadXML(self, "mice", "cost", number, 0))
        money += int(GameLogic.ReadXML(self, "mice", "cost", number, 0))
        self.moneylabel.setText(str(money))

    def update_ui(self):

        global energy
        self.energybar.setValue(energy)

    def pipe_click(self):

        global energy, energy_max

        if energy > 0:
            energy -= 1
            self.catch_mouse()
        else:
            self.diamondslabel.setText("Not enough energy")
            #alert(text='Not enough energy', title='Energsy info', button='OK')

        if energy < energy_max:
            thread = EnergyThread()
            thread.start()

        self.update_ui()


class GameLogic(object):

    def ReadXML(self, tag, name, number, index):
        xmldoc = minidom.parse('locations.xml')
        itemlist = xmldoc.getElementsByTagName(str(tag) + str(number))
        return itemlist[index].attributes[str(name)].value


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


def ReadFile(position, index):
    xmldoc = minidom.parse('userdata.xml')
    itemlist = xmldoc.getElementsByTagName(str("user"))
    return itemlist[index].attributes[position].value


def WriteFile():
    doc, tag, text = Doc().tagtext()
    with tag('user', energy=str(energy), money=str(money)):
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


energy = int(ReadFile("energy", 0))
money = int(ReadFile("money", 0))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_(), WriteFile())
