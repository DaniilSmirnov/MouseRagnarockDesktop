# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from pymsgbox import *
from xml.dom import minidom
from random import *
from threading import Thread
import time
from yattag import Doc, indent
from PIL import Image
import xml.etree.cElementTree as ET

exec = False


class Ui_MainWindow(QtCore.QObject):
    updateProgress = QtCore.pyqtSignal(int)

    def setupUi(self, MainWindow):

        self.window_width = 600
        self.window_height = 800

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.energybar = QtWidgets.QProgressBar(self.layoutWidget)
        self.energybar.setProperty("value", 10)
        self.energybar.setFormat("")
        self.energybar.setObjectName("energybar")
        self.gridLayout.addWidget(self.energybar, 2, 1, 1, 2)
        self.questsbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.questsbutton.setEnabled(False)
        self.questsbutton.setObjectName("questsbutton")
        self.gridLayout.addWidget(self.questsbutton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 3, 2)
        self.move = QtWidgets.QPushButton(self.layoutWidget)
        self.move.setEnabled(False)
        self.move.setObjectName("move")
        self.gridLayout.addWidget(self.move, 4, 1, 1, 1)
        self.inventory = QtWidgets.QPushButton(self.layoutWidget)
        self.inventory.setEnabled(True)
        self.inventory.setObjectName("inventory")
        self.gridLayout.addWidget(self.inventory, 4, 0, 1, 1)
        self.shop = QtWidgets.QPushButton(self.layoutWidget)
        self.shop.setEnabled(True)
        self.shop.setObjectName("shop")
        self.gridLayout.addWidget(self.shop, 4, 2, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.energybar = QtWidgets.QProgressBar(self.layoutWidget)
        self.energybar.setProperty("value", 10)
        self.energybar.setFormat("")
        self.energybar.setObjectName("energybar")
        self.gridLayout.addWidget(self.energybar, 2, 1, 1, 2)
        self.questsbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.questsbutton.setEnabled(False)
        self.questsbutton.setObjectName("questsbutton")
        self.gridLayout.addWidget(self.questsbutton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 3, 2)
        self.move = QtWidgets.QPushButton(self.layoutWidget)
        self.move.setEnabled(False)
        self.move.setObjectName("move")
        self.gridLayout.addWidget(self.move, 4, 1, 1, 1)
        self.inventory = QtWidgets.QPushButton(self.layoutWidget)
        self.inventory.setEnabled(True)
        self.inventory.setObjectName("inventory")
        self.gridLayout.addWidget(self.inventory, 4, 0, 1, 1)
        self.shop = QtWidgets.QPushButton(self.layoutWidget)
        self.shop.setEnabled(True)
        self.shop.setObjectName("shop")
        self.gridLayout.addWidget(self.shop, 4, 2, 1, 1)
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
        self.pipe.setIcon(QtGui.QIcon('pipe.png'))
        self.pipe.setIconSize(QtCore.QSize(392, 101))

        self.bossesbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.bossesbutton.setEnabled(False)
        self.bossesbutton.setObjectName("bossesbutton")
        self.gridLayout.addWidget(self.bossesbutton, 2, 3, 1, 1)
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
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.location_label = QtWidgets.QLabel(self.groupBox)
        self.location_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.location_label.setObjectName("location_label")
        self.gridLayout_3.addWidget(self.location_label, 0, 0, 1, 1)
        self.about_location_button = QtWidgets.QPushButton(self.groupBox)
        self.about_location_button.setObjectName("about_location_button")
        self.gridLayout_3.addWidget(self.about_location_button, 1, 0, 1, 1)
        self.location_label.raise_()
        self.location_label.raise_()
        self.about_location_button.raise_()
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
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

        self.init()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mouse Ragnarok"))
        self.questsbutton.setText(_translate("MainWindow", "Quests"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.move.setText(_translate("MainWindow", "Locations"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))
        self.shop.setText(_translate("MainWindow", "Shop"))
        self.clans.setText(_translate("MainWindow", "Clans"))
        self.pipe.setText(_translate("MainWindow", " "))
        self.bossesbutton.setText(_translate("MainWindow", "Bosses"))
        self.mouseview.setTitle(_translate("MainWindow", "Journal"))
        self.mouseattachment.setText(_translate("MainWindow", "TextLabel"))
        self.journal_button.setText(_translate("MainWindow", "Open Journal"))
        self.mousename.setText(_translate("MainWindow", "TextLabel"))
        self.mousecost.setText(_translate("MainWindow", "TextLabel"))
        self.mouse_image.setText(_translate("MainWindow", "TextLabel"))
        self.devicesbox.setTitle(_translate("MainWindow", "Devices"))
        self.cheese_label.setText(_translate("MainWindow", " "))
        self.board_label.setText(_translate("MainWindow", " "))
        self.device_label.setText(_translate("MainWindow", " "))
        self.switchbox.setTitle(_translate("MainWindow", "Devices"))
        self.cheese_button.setText(_translate("MainWindow", "Cheese"))
        self.board_button.setText(_translate("MainWindow", "Board"))
        self.device_button.setText(_translate("MainWindow", "Device"))
        self.MoneyBox.setTitle(_translate("MainWindow", "Money"))
        self.moneylabel.setText(_translate("MainWindow", " "))
        self.diamondslabel.setText(_translate("MainWindow", " "))
        self.groupBox.setTitle(_translate("MainWindow", "Location Info"))
        self.location_label.setText(_translate("MainWindow", " "))
        self.about_location_button.setText(_translate("MainWindow", "About Location"))

        self.pipe.clicked.connect(self.pipe_click)
        self.shop.clicked.connect(self.open_shop)
        self.journal_button.clicked.connect(self.open_journal)
        self.inventory.clicked.connect(self.open_inventory)

        self.updateProgress.connect(self.energybar.setValue)

    def init(self):
        global login, password

        try:
            login = LoginData.ReadFile(LoginData, "login", 0)
            password = LoginData.ReadFile(LoginData, "password", 0)
        except BaseException:
            login = LoginWindow()
            login.exec_()

        device_img = Image.open(device + ".png")
        back_img = Image.open(location_name + ".jpg")

        back_img.paste(device_img, (0, 0), device_img)
        back_img.save('result.png')
        devpix = QtGui.QPixmap("result.png")

        self.label.setPixmap(devpix)

        self.update_ui()

    def catch_mouse(self):
        global money, cheese_amount, mouse_name, mouse_cost, location, mouse_drop, mouse_icon

        amount = int(GameLogic.ReadDataFromXML(self, "locations.xml", "location", "amount", location, 0))
        number = int(GameLogic.ReadDataFromXML(self, "locations.xml", "location", "start", location, 0)) + int(random()*(amount))

        if (((number != 1) and (location == 1)) or ((number != 12) and (location == 2))) and (1+int(random()*5) > 4):
            mouse_drop = GameLogic.ReadDataFromXML(self, "locations.xml", "mice", "drop", number, 0)

            thread = InventoryThread()
            thread.start()

        else:
            mouse_drop = " "

        mouse_name = GameLogic.ReadDataFromXML(self, "locations.xml", "mice", "name", number, 0)
        mouse_cost = GameLogic.ReadDataFromXML(self, "locations.xml", "mice", "cost", number, 0)
        mouse_icon = GameLogic.ReadDataFromXML(self, "locations.xml", "mice", "icon", number, 0)
        self.mousename.setText(mouse_name)
        self.mousecost.setText(mouse_cost)
        self.mouseattachment.setText(mouse_drop)
        pixmap = QtGui.QPixmap(mouse_icon)
        self.mouse_image.setPixmap(pixmap)
        money += int(mouse_cost)
        self.moneylabel.setText(str(money))
        if number != 1:
            GameLogic.editXML(GameLogic,"shop.xml", "item", cheese_index, -1)
        Journal.Write(self, mouse_name, mouse_cost, mouse_drop)

    def update_ui(self):

        global energy, cheese_index, cheese_amount
        self.energybar.setMaximum(energy_max)
        self.energybar.setValue(energy)
        self.cheese_label.setText(cheese + " " + GameLogic.ReadDataFromXML(GameLogic, "shop.xml", "item", "amount", cheese_index, 0))
        self.diamondslabel.setText(str(diamonds))
        self.moneylabel.setText(str(money))
        self.mousename.setText(mouse_name)
        self.mousecost.setText(mouse_cost)
        self.location_label.setText(location_name)
        self.mouseattachment.setText(mouse_drop)
        pixmap = QtGui.QPixmap(mouse_icon)
        self.mouse_image.setPixmap(pixmap)
        self.board_label.setText("Board: " + str(board))
        self.device_label.setText("Device: " + device)

    def pipe_click(self):

        global energy, energy_max

        if energy > 0 and int((GameLogic.ReadDataFromXML(GameLogic, "shop.xml", "item", "amount", cheese_index, 0))) > 0:
            energy -= 1
            self.catch_mouse()
        else:
            alert(text='Not enough energy or cheese', title='Alert', button='OK')

        self.update_ui()

    def open_shop(self):

        shop = ShopWindow()
        shop.exec_()
        self.update_ui()

    def open_journal(self):

        journal = JournalWindow()
        journal.exec_()
        self.update_ui()

    def open_inventory(self):
        inventory = InventoryWindow()
        inventory.exec_()
        self.update_ui()


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 106)
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 106))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password = QtWidgets.QLabel(self.widget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 0, 1, 1)
        self.login_enter = QtWidgets.QLineEdit(self.widget)
        self.login_enter.setObjectName("login_enter")
        self.gridLayout.addWidget(self.login_enter, 0, 1, 1, 2)
        self.password_login = QtWidgets.QLineEdit(self.widget)
        self.password_login.setObjectName("password_login")
        self.gridLayout.addWidget(self.password_login, 1, 1, 1, 2)
        self.login = QtWidgets.QLabel(self.widget)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 0, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.widget)
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 2, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.terms_button = QtWidgets.QPushButton(self.widget)
        self.terms_button.setObjectName("terms_button")
        self.gridLayout.addWidget(self.terms_button, 2, 1, 1, 1)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.password.setText(_translate("Login", "Password"))
        self.login.setText(_translate("Login", "Login"))
        self.login_button.setText(_translate("Login", "Login"))
        self.checkBox.setText(_translate("Login", "Agree"))
        self.terms_button.setText(_translate("Login", "Terms"))


class LoginWindow(QtWidgets.QDialog, Ui_Login):

    def __init__(self, parent=None):

        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.login_button.clicked.connect(self.write_login)
        self.checkBox.stateChanged.connect(self.set_state)

    def set_state(self, state):
        global exec

        if state == QtCore.Qt.Checked:
            exec = True
        else:
            exec = False

    def write_login(self):
        global login, password, exec
        login = self.login_enter.text()
        password = self.password_login.text()
        if exec:
            LoginData.WriteFile(LoginData)
            self.close()


class ShopWindowUi(object):

    def setupUi(self, ShopWindowUi):
        ShopWindowUi.setObjectName("ShopWindowUi")
        ShopWindowUi.resize(289, 479)
        self.gridLayout = QtWidgets.QGridLayout(ShopWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_button = QtWidgets.QPushButton(ShopWindowUi)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)
        self.amount_label = QtWidgets.QLabel(ShopWindowUi)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.amount_label.sizePolicy().hasHeightForWidth())
        self.amount_label.setSizePolicy(self.sizePolicy)
        self.amount_label.setObjectName("amount_label")
        self.gridLayout.addWidget(self.amount_label, 0, 0, 1, 2)

        self.retranslateUi(ShopWindowUi)
        QtCore.QMetaObject.connectSlotsByName(ShopWindowUi)

    def retranslateUi(self, ShopWindowUi):
        _translate = QtCore.QCoreApplication.translate
        ShopWindowUi.setWindowTitle(_translate("ShopWindowUi", "Dialog"))
        self.ok_button.setText(_translate("ShopWindowUi", "OK"))
        self.amount_label.setText(_translate("ShopWindowUi", "TextLabel"))


class ShopWindow(QtWidgets.QDialog, ShopWindowUi):
    def __init__(self, parent=None):
        global cost

        super(ShopWindow, self).__init__(parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.close)
        self.amount_label.setText(str(money))

        self.items = {}
        self.list = []

        i = 0

        while i < int(GameLogic.ReadI(GameLogic, "shop.xml")):
            i += 1
            key = GameLogic.ReadDataFromXML(self, "shop.xml", "item", "name", i, 0)
            value = GameLogic.ReadDataFromXML(self, "shop.xml", "item", "cost", i, 0)
            self.items.update({str(key): str(value)})

        self.create()

    def create(self):

        i = 0
        for item in self.items:
            i += 1

            self.item_label = QtWidgets.QLabel(item + " Cost: " + self.items.get(item) + " You already have: " + GameLogic.ReadDataFromXML(GameLogic, "shop.xml", "item", "amount", i, 0))
            self.item_button = QtWidgets.QPushButton("Buy " + item)

            self.item_label.setSizePolicy(self.sizePolicy)
            self.item_button.setSizePolicy(self.sizePolicy)

            self.verticalLayout.addWidget(self.item_label)
            self.verticalLayout.addWidget(self.item_button)

            self.item_button.clicked.connect(lambda state, button=self.item_button: self.buy(button))

            self.list.append(self.item_button)
            self.list.append(self.item_label)

    def update_ui(self):
        self.amount_label.setText(str(money))

        for item in self.list:
            item.close()

        self.list.clear()

        self.create()

    def buy(self, button):

        global money, cheese_amount

        i = 0

        while i < int(GameLogic.ReadI(GameLogic, "shop.xml")):

            i += 1
            item = GameLogic.ReadDataFromXML(GameLogic, "shop.xml", "item", "name", i, 0)

            if (str(button.text())[4:]) == item:
                money -= int(self.items.get(item))
                GameLogic.editXML(self, "shop.xml", "item", i, 1)
                self.update_ui()


class JournalWindowUi(object):

    def setupUi(self, JournalWindowUi):
        JournalWindowUi.setObjectName("JournalWindowUi")
        JournalWindowUi.resize(600, 564)
        self.gridLayout = QtWidgets.QGridLayout(JournalWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_button = QtWidgets.QPushButton(JournalWindowUi)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(JournalWindowUi)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

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

        self.ok_button.clicked.connect(self.close)

        Journal.Close(Journal)
        i = int(GameLogic.ReadI(GameLogic, 'journal.xml'))

        if i > 10:
            j = i-10
        else:
            j = 1
        while j <= i:
            self.textBrowser.append(Journal.Read(Journal, "mouse_name", j) + " " + Journal.Read(Journal, "mouse_cost", j) + " " + Journal.Read(Journal, "mouse_drop", j))
            j += 1
        Journal.Init(Journal)


class InventoryWindowUi(object):

    def setupUi(self, InventoryWindowUi):
        InventoryWindowUi.setObjectName("JournalWindowUi")
        InventoryWindowUi.resize(600, 564)
        self.gridLayout = QtWidgets.QGridLayout(InventoryWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_button = QtWidgets.QPushButton(InventoryWindowUi)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(InventoryWindowUi)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(InventoryWindowUi)
        QtCore.QMetaObject.connectSlotsByName(InventoryWindowUi)

    def retranslateUi(self, InventoryWindowUi):
        _translate = QtCore.QCoreApplication.translate
        InventoryWindowUi.setWindowTitle(_translate("JournalWindowUi", "Dialog"))
        self.ok_button.setText(_translate("JournalWindowUi", "OK"))


class InventoryWindow(QtWidgets.QDialog, InventoryWindowUi):
    def __init__(self, parent=None):
        super(InventoryWindow, self).__init__(parent)
        self.setupUi(self)

        self.ok_button.clicked.connect(self.close)

        Inventory.Close(Inventory)
        i = int(GameLogic.ReadI(GameLogic, "inventory.xml"))
        j = 1
        while j <= i:
            self.textBrowser.append(Inventory.Read(Inventory, "item", j) + " " + Inventory.Read(Inventory, "amount", j) + "x")
            j += 1
        Inventory.Init(Inventory)


class GameLogic(object):

    global energy, money

    def ReadDataFromXML(self, file, tag, name, number, index):
        xmldoc = minidom.parse(file)
        itemlist = xmldoc.getElementsByTagName(str(tag) + str(number))
        return itemlist[index].attributes[str(name)].value

    def ReadUserData(self, position, index):
        xmldoc = minidom.parse('userdata.xml')
        itemlist = xmldoc.getElementsByTagName(str("user"))
        return itemlist[index].attributes[position].value

    def WriteUserData(self):
        doc, tag, text = Doc().tagtext()
        with tag('user', energy=str(energy),energy_max=str(energy_max),
                 location=str(location), money=str(money),
                 diamonds=str(diamonds), cheese=cheese,
                 cheese_amount=str(cheese_amount),
                 last_mouse=mouse_name, last_cost=mouse_cost,
                 last_drop=mouse_drop, last_icon=mouse_icon,
                 device=device, board=board):
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

    def editXML(self, file, tag, index, sign):
        """
        Редактируем XML атрибут.
        """
        frag_xml_tree = ET.parse(file)
        root = frag_xml_tree.getroot()
        for elem in root.iter(tag+str(index)):
            amount = int(elem.get('amount'))
            amount += sign
            elem.set('amount', str(amount))
        frag_xml_tree.write(file)

    def ReadI(self, file):
        xmldoc = minidom.parse(file)
        itemlist = xmldoc.getElementsByTagName(str("res"))
        return itemlist[0].attributes["i"].value


class LoginData(object):

    def ReadFile(self, position, index):
        xmldoc = minidom.parse('logindata.xml')
        itemlist = xmldoc.getElementsByTagName(str("user"))
        return itemlist[index].attributes[position].value

    def WriteFile(self):
        doc, tag, text = Doc().tagtext()
        with tag('user', login=str(login), password=str(password)):
            text(str(energy))

        result = indent(
            doc.getvalue(),
            indentation=' ' * 4,
            newline='\r\n')

        filename = 'logindata.xml'
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
        global energy, energy_max, energy_exec
        while energy_exec:
            if energy <= energy_max:
                time.sleep(1)
                energy += 1
                #Ui_MainWindow.update_ui()


class InventoryThread(Thread):
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        """Запуск потока"""
        global mouse_drop

        filename = 'inventory.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        index = 0

        i = 0

        for line in lines:
            if line.find(mouse_drop) != -1:
                break
            index += 1
            i += 1

        if index == len(lines):
            Inventory.Write(Inventory, mouse_drop)
        else:
            Inventory.Close(Inventory)
            GameLogic.editXML(GameLogic, "inventory.xml", "position", index, 1)
            Inventory.Init(Inventory)


class Journal(object):
    global i

    def Read(self, position, index):
        xmldoc = minidom.parse('journal.xml')
        itemlist = xmldoc.getElementsByTagName("position"+str(index))
        return itemlist[0].attributes[str(position)].value

    def Write(self, name, cost, drop):
        global i
        i += 1
        doc, tag, text = Doc().tagtext()
        with tag('position'+str(i), mouse_name=name, mouse_cost=cost, mouse_drop=drop):
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
        i = int(GameLogic.ReadI(GameLogic, "journal.xml"))

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


class Inventory(object):

    def Read(self, position, index):
        xmldoc = minidom.parse('inventory.xml')
        itemlist = xmldoc.getElementsByTagName("position"+str(index))
        return itemlist[0].attributes[str(position)].value

    def Init(self):
        filename = 'inventory.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        global k
        k = int(GameLogic.ReadI(GameLogic, "inventory.xml"))

        myfile = open(filename, 'w')
        for line in lines:
            if line != "</res>":
                myfile.write(line)
        myfile.close()

    def Close(self):
        global k

        filename = 'inventory.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        myfile = open(filename, 'w')
        for line in lines:
            if line.find("<res") != -1:
                myfile.write("<res " + "i=" + '"' + str(k) + '"' + ">" + "\n")
            else:
                myfile.write(line)
        myfile.close()

        myfile = open(filename, 'a')
        myfile.write("</res>")
        myfile.close()

    def Write(self, drop):
        global k
        k += 1
        doc, tag, text = Doc().tagtext()
        with tag('position'+str(k), item=drop, amount="1"):
            text(str(energy))

        result = indent(
            doc.getvalue(),
            indentation=' ' * 4,
            newline='\r\n')

        filename = 'inventory.xml'
        myfile = open(filename, 'a')
        myfile.write(result)
        myfile.write("\n")
        myfile.close()
        print(result)


class Quests(object):

    def ReadI(self):

        xmldoc = minidom.parse('inventory.xml')
        itemlist = xmldoc.getElementsByTagName(str("res"))
        return itemlist[0].attributes["i"].value

    def Read(self, position, index):
        xmldoc = minidom.parse('inventory.xml')
        itemlist = xmldoc.getElementsByTagName("position"+str(index))
        return itemlist[0].attributes[str(position)].value

    def Init(self):
        filename = 'inventory.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        global k
        k = int(self.ReadI(Inventory))

        myfile = open(filename, 'w')
        for line in lines:
            if line != "</res>":
                myfile.write(line)
        myfile.close()

    def Close(self):
        global k

        filename = 'inventory.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        myfile = open(filename, 'w')
        for line in lines:
            if line.find("<res") != -1:
                myfile.write("<res " + "i=" + '"' + str(k) + '"' + ">" + "\n")
            else:
                myfile.write(line)
        myfile.close()

        myfile = open(filename, 'a')
        myfile.write("</res>")
        myfile.close()

    def Write(self, drop):
        global k
        k += 1
        doc, tag, text = Doc().tagtext()
        with tag('position'+str(k), mouse_drop=drop):
            text(str(energy))

        result = indent(
            doc.getvalue(),
            indentation=' ' * 4,
            newline='\r\n')

        filename = 'inventory.xml'
        myfile = open(filename, 'a')
        myfile.write(result)
        myfile.write("\n")
        myfile.close()
        print(result)


energy = int(GameLogic.ReadUserData(GameLogic, "energy", 0))
money = int(GameLogic.ReadUserData(GameLogic, "money", 0))
diamonds = int(GameLogic.ReadUserData(GameLogic, "diamonds", 0))
cheese = GameLogic.ReadUserData(GameLogic, "cheese", 0)

filename = 'shop.xml'
myfile = open(filename, 'r')
lines = myfile.readlines()
myfile.close()

cheese_index = 0

for line in lines:
    if line.find(cheese) != -1:
        break
    cheese_index += 1

cheese_amount = int(GameLogic.ReadDataFromXML(GameLogic, "shop.xml","item", "amount", cheese_index, 0))
mouse_cost = GameLogic.ReadData(GameLogic, "last_cost", 0)
mouse_name = GameLogic.ReadUserData(GameLogic, "last_mouse", 0)
mouse_drop = GameLogic.ReadUserData(GameLogic, "last_drop", 0)
location = int(GameLogic.ReadUserData(GameLogic, "location", 0))
location_name = GameLogic.ReadDataFromXML(GameLogic,"locations.xml", "location", "name", location, 0)
mouse_icon = GameLogic.ReadUserData(GameLogic, "last_icon", 0)
device = GameLogic.ReadUserData(GameLogic, "device", 0)
energy_max = int(GameLogic.ReadUserData(GameLogic, "energy_max", 0))
board = GameLogic.ReadUserData(GameLogic, "board", 0)

Journal.Init(Journal)
Inventory.Init(Inventory)


def setter(exec):
    global energy_exec
    if exec:
        return True
    else:
        energy_exec = False


energy_exec = setter(True)
thread = EnergyThread()
thread.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    oImage = QtGui.QImage("mainback.jpg")
    sImage = oImage.scaled(QtCore.QSize(800, 600))
    palette = QtGui.QPalette()
    palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))

    MainWindow.setPalette(palette)
    sys.exit(app.exec_(), GameLogic.WriteUserData(GameLogic), Journal.Close(Journal), Inventory.Close(Inventory), setter(False))
