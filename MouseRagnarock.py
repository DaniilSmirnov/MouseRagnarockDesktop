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
        self.mouseview = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouseview.sizePolicy().hasHeightForWidth())
        self.mouseview.setSizePolicy(sizePolicy)
        self.mouseview.setObjectName("mouseview")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.mouseview)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.mouseattachment = QtWidgets.QLabel(self.mouseview)
        self.mouseattachment.setObjectName("mouseattachment")
        self.gridLayout_6.addWidget(self.mouseattachment, 4, 0, 1, 1)
        self.filler1 = QtWidgets.QLabel(self.mouseview)
        self.filler1.setText("")
        self.filler1.setObjectName("filler1")
        self.gridLayout_6.addWidget(self.filler1, 1, 1, 1, 1)
        self.filler2 = QtWidgets.QLabel(self.mouseview)
        self.filler2.setText("")
        self.filler2.setObjectName("filler2")
        self.gridLayout_6.addWidget(self.filler2, 2, 1, 1, 1)
        self.journal_button = QtWidgets.QPushButton(self.mouseview)
        self.journal_button.setObjectName("journal_button")
        self.gridLayout_6.addWidget(self.journal_button, 5, 1, 1, 1)
        self.mousename = QtWidgets.QLabel(self.mouseview)
        self.mousename.setObjectName("mousename")
        self.gridLayout_6.addWidget(self.mousename, 0, 1, 1, 1)
        self.mousecost = QtWidgets.QLabel(self.mouseview)
        self.mousecost.setObjectName("mousecost")
        self.gridLayout_6.addWidget(self.mousecost, 4, 1, 1, 1)
        self.filler3 = QtWidgets.QLabel(self.mouseview)
        self.filler3.setText("")
        self.filler3.setObjectName("filler3")
        self.gridLayout_6.addWidget(self.filler3, 3, 1, 1, 1)
        self.mouse_image = QtWidgets.QLabel(self.mouseview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouse_image.sizePolicy().hasHeightForWidth())
        self.mouse_image.setSizePolicy(sizePolicy)
        self.mouse_image.setObjectName("mouse_image")
        self.gridLayout_6.addWidget(self.mouse_image, 0, 0, 4, 1)
        self.gridLayout.addWidget(self.mouseview, 7, 2, 1, 2)
        self.clans = QtWidgets.QPushButton(self.layoutWidget)
        self.clans.setEnabled(False)
        self.clans.setObjectName("clans")
        self.gridLayout.addWidget(self.clans, 4, 3, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 5, 0, 3, 2)
        self.pipe = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pipe.sizePolicy().hasHeightForWidth())
        self.pipe.setSizePolicy(sizePolicy)
        self.pipe.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pipe.setObjectName("pipe")
        self.gridLayout.addWidget(self.pipe, 0, 1, 1, 2)
        self.energybar = QtWidgets.QProgressBar(self.layoutWidget)
        self.energybar.setProperty("value", 10)
        self.energybar.setObjectName("energybar")
        self.gridLayout.addWidget(self.energybar, 2, 1, 1, 2)
        self.move = QtWidgets.QPushButton(self.layoutWidget)
        self.move.setEnabled(False)
        self.move.setObjectName("move")
        self.gridLayout.addWidget(self.move, 4, 1, 1, 1)
        self.shop = QtWidgets.QPushButton(self.layoutWidget)
        self.shop.setEnabled(True)
        self.shop.setObjectName("shop")
        self.gridLayout.addWidget(self.shop, 4, 2, 1, 1)
        self.inventory = QtWidgets.QPushButton(self.layoutWidget)
        self.inventory.setEnabled(False)
        self.inventory.setObjectName("inventory")
        self.gridLayout.addWidget(self.inventory, 4, 0, 1, 1)
        self.location_label = QtWidgets.QLabel(self.layoutWidget)
        self.location_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.location_label.setObjectName("location_label")
        self.gridLayout.addWidget(self.location_label, 2, 0, 1, 1)
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
        self.gridLayout.addWidget(self.devicesbox, 5, 3, 2, 1)
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
        self.gridLayout.addWidget(self.switchbox, 5, 2, 2, 1)
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
        self.MoneyBox.setTitle(_translate("MainWindow", "Money"))
        self.moneylabel.setText(_translate("MainWindow", "TextLabel"))
        self.diamondslabel.setText(_translate("MainWindow", "TextLabel"))
        self.mouseview.setTitle(_translate("MainWindow", "Journal"))
        self.mouseattachment.setText(_translate("MainWindow", "TextLabel"))
        self.journal_button.setText(_translate("MainWindow", "Open Journal"))
        self.mousename.setText(_translate("MainWindow", "TextLabel"))
        self.mousecost.setText(_translate("MainWindow", "TextLabel"))
        self.mouse_image.setText(_translate("MainWindow", "TextLabel"))
        self.clans.setText(_translate("MainWindow", "Clans"))
        self.pipe.setText(_translate("MainWindow", "pipe"))
        self.move.setText(_translate("MainWindow", "Locations"))
        self.shop.setText(_translate("MainWindow", "Shop"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))
        self.location_label.setText(_translate("MainWindow", "TextLabel"))
        self.devicesbox.setTitle(_translate("MainWindow", "Devices"))
        self.cheese_label.setText(_translate("MainWindow", "TextLabel"))
        self.board_label.setText(_translate("MainWindow", "TextLabel"))
        self.device_label.setText(_translate("MainWindow", "TextLabel"))
        self.switchbox.setTitle(_translate("MainWindow", "Devices"))
        self.cheese_button.setText(_translate("MainWindow", "Cheese"))
        self.board_button.setText(_translate("MainWindow", "Board"))
        self.device_button.setText(_translate("MainWindow", "Device"))

        self.pipe.clicked.connect(self.pipe_click)
        self.shop.clicked.connect(self.open_shop)
        self.journal_button.clicked.connect(self.open_journal)

    def catch_mouse(self):
        global money, cheese_amount, mouse_name, mouse_cost, location

        amount = int(GameLogic.ReadMiceDataFromXML(self, "location", "amount", location, 0))
        number = 1 + int(random()*(amount-1))

        mouse_name =  GameLogic.ReadMiceDataFromXML(self, "mice", "name", number, 0)
        mouse_cost = GameLogic.ReadMiceDataFromXML(self, "mice", "cost", number, 0)
        self.mousename.setText(mouse_name)
        self.mousecost.setText(mouse_cost)
        money += int(mouse_cost)
        self.moneylabel.setText(str(money))
        if number != 10:
            cheese_amount -= 1
        Journal.Write(self, mouse_name, mouse_cost)

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

    def open_shop(self):

        shop = Shop()
        shop.exec_()
        self.update_ui()

    def open_journal(self):

        journal = JournalWindow()
        journal.exec_()
        self.update_ui()


class ShopWindowUi(object):

    def setupUi(self, ShopWindowUi):
        ShopWindowUi.setObjectName("ShopWindowUi")
        ShopWindowUi.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ShopWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.amount_label = QtWidgets.QLabel(ShopWindowUi)
        self.amount_label.setObjectName("amount_label")
        self.gridLayout.addWidget(self.amount_label, 1, 3, 1, 1)
        self.ok_button = QtWidgets.QPushButton(ShopWindowUi)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 2, 1, 1, 1)
        self.buy_button = QtWidgets.QPushButton(ShopWindowUi)
        self.buy_button.setObjectName("buy_button")
        self.gridLayout.addWidget(self.buy_button, 1, 1, 1, 1)
        self.cost_label = QtWidgets.QLabel(ShopWindowUi)
        self.cost_label.setObjectName("cost_label")
        self.gridLayout.addWidget(self.cost_label, 1, 2, 1, 1)
        self.money_label = QtWidgets.QLabel(ShopWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.money_label.sizePolicy().hasHeightForWidth())
        self.money_label.setSizePolicy(sizePolicy)
        self.money_label.setObjectName("money_label")
        self.gridLayout.addWidget(self.money_label, 0, 3, 1, 1)

        self.retranslateUi(ShopWindowUi)
        QtCore.QMetaObject.connectSlotsByName(ShopWindowUi)

    def retranslateUi(self, ShopWindowUi):
        _translate = QtCore.QCoreApplication.translate
        ShopWindowUi.setWindowTitle(_translate("ShopWindowUi", "Dialog"))
        self.amount_label.setText(_translate("ShopWindowUi", "TextLabel"))
        self.ok_button.setText(_translate("ShopWindowUi", "OK"))
        self.buy_button.setText(_translate("ShopWindowUi", "Buy"))
        self.cost_label.setText(_translate("ShopWindowUi", "TextLabel"))
        self.money_label.setText(_translate("ShopWindowUi", "TextLabel"))


class Shop(QtWidgets.QDialog, ShopWindowUi):
    def __init__(self, parent=None):
        global cost

        super(Shop, self).__init__(parent)
        self.setupUi(self)
        self.update_ui()

        self.buy_button.clicked.connect(self.buy)
        self.ok_button.clicked.connect(self.close)

        cost = GameLogic.ReadCheeseDataFromXML(ShopWindowUi, "cheese", "cost", 1, 0)

    def update_ui(self):

        global cost, cheese_amount

        cost = GameLogic.ReadCheeseDataFromXML(ShopWindowUi, "cheese", "cost", 1, 0)

        self.money_label.setText("You have: " + str(money))
        self.amount_label.setText(GameLogic.ReadCheeseDataFromXML(ShopWindowUi, "cheese", "name", 1, 0) + ": " + str(cheese_amount))
        self.cost_label.setText(str(cost))

    def buy(self):

        global cost, money, cheese_amount

        if money - int(cost) > 0:
            money -= int(cost)
            cheese_amount += 1
        else:
            alert(text='Not enough money', title='Alert', button='OK')

        self.update_ui()


class JournalWindowUi(object):

    def setupUi(self, JournalWindowUi):
        JournalWindowUi.setObjectName("JournalWindowUi")
        JournalWindowUi.resize(600, 564)
        self.gridLayout = QtWidgets.QGridLayout(JournalWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_button = QtWidgets.QPushButton(JournalWindowUi)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 0, 0, 1, 1)

        self.retranslateUi(JournalWindowUi)
        QtCore.QMetaObject.connectSlotsByName(JournalWindowUi)

    def retranslateUi(self, JournalWindowUi):
        _translate = QtCore.QCoreApplication.translate
        JournalWindowUi.setWindowTitle(_translate("JournalWindowUi", "Dialog"))
        self.ok_button.setText(_translate("JournalWindowUi", "OK"))


class JournalWindow(QtWidgets.QDialog, JournalWindowUi):
    def __init__(self, parent=None):
        super(JournalWindow, self).__init__(parent)
        self.setupUi(self)


class GameLogic(object):

    global energy, money

    def ReadMiceDataFromXML(self, tag, name, number, index):
        xmldoc = minidom.parse('locations.xml')
        itemlist = xmldoc.getElementsByTagName(str(tag) + str(number))
        return itemlist[index].attributes[str(name)].value

    def ReadCheeseDataFromXML(self, tag, name, number, index):
        xmldoc = minidom.parse('cheese.xml')
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


class Journal(object):
    global i

    def Read(self, position, index):
        xmldoc = minidom.parse('journal.xml')
        itemlist = xmldoc.getElementsByTagName(str("position")+str(index))
        return itemlist[index].attributes[position].value

    def ReadI(self):

        xmldoc = minidom.parse('journal.xml')
        itemlist = xmldoc.getElementsByTagName(str("res"))
        return itemlist[0].attributes["i"].value

    def Write(self, name, cost):
        global i
        i += 1
        doc, tag, text = Doc().tagtext()
        with tag('position'+str(i), mouse_name=name, mouse_cost=cost):
            text(str(energy))

        result = indent(
            doc.getvalue(),
            indentation=' ' * 4,
            newline='\r\n')

        filename = 'journal.xml'
        myfile = open(filename, 'a')
        myfile.write(result)
        myfile.write("\n")
        myfile.close()
        print(result)

    def Init(self):
        filename = 'journal.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        global i
        i = int(self.ReadI(Journal))

        myfile = open(filename, 'w')
        for line in lines:
            if line != "</res>":
                myfile.write(line)
        myfile.close()

    def Close(self):
        global i

        filename = 'journal.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        myfile = open(filename, 'w')
        for line in lines:
            if line.find("<res") != -1:
                myfile.write("<res " + "i=" + '"' + str(i) + '"' + ">" + "\n")
            else:
                myfile.write(line)
        myfile.close()

        filename = 'journal.xml'
        myfile = open(filename, 'a')
        myfile.write("</res>")
        myfile.close()


energy = int(GameLogic.ReadFile(GameLogic, "energy", 0))
money = int(GameLogic.ReadFile(GameLogic, "money", 0))
diamonds = int(GameLogic.ReadFile(GameLogic, "diamonds", 0))
cheese = GameLogic.ReadFile(GameLogic, "cheese", 0)
cheese_amount = int(GameLogic.ReadFile(GameLogic, "cheese_amount", 0))
mouse_cost = GameLogic.ReadFile(GameLogic, "last_cost", 0)
mouse_name = GameLogic.ReadFile(GameLogic, "last_mouse", 0)
location = int(GameLogic.ReadFile(GameLogic, "location", 0))
location_name = GameLogic.ReadMiceDataFromXML(GameLogic, "location", "name", location, 0)

Journal.Init(Journal)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_(), GameLogic.WriteFile(GameLogic), Journal.Close(Journal))
