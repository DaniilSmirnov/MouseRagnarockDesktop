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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.energybar = QtWidgets.QProgressBar(self.layoutWidget)
        self.energybar.setProperty("value", 10)
        self.energybar.setFormat("")
        self.energybar.setObjectName("energybar")
        self.gridLayout.addWidget(self.energybar, 2, 1, 1, 2)
        self.questsbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.questsbutton.setEnabled(True)
        self.questsbutton.setObjectName("questsbutton")
        self.gridLayout.addWidget(self.questsbutton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 3, 2)
        self.move = QtWidgets.QPushButton(self.layoutWidget)
        self.move.setEnabled(True)
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
        self.move.clicked.connect(self.open_locations)
        self.about_location_button.clicked.connect(self.open_about_locations)
        self.questsbutton.clicked.connect(self.open_quests)

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
        number = int(GameLogic.ReadDataFromXML(self, "locations.xml", "location", "start", location, 0)) + int(random()*amount)

        if (((number != 1) and (location == 1)) or ((number != 12) and (location == 2))) and (1+int(random()*5) > 4):
            mouse_drop = GameLogic.ReadDataFromXML(self, "locations.xml", "mice", "drop", number, 0)

            if mouse_drop.find("Coins") != -1:
                money += 100
            elif mouse_drop.find("Russian Cheese x10") != -1:
                GameLogic.editXML(GameLogic, "shop.xml", "item", cheese_index, 10)
            elif mouse_drop.find("Russian Cheese x5") != -1:
                GameLogic.editXML(GameLogic, "shop.xml", "item", cheese_index, 5)
            elif mouse_drop.find("Key") != -1:
                thread = InventoryThread()
                thread.start()
                frag_xml_tree = ET.parse("locations.xml")
                root = frag_xml_tree.getroot()
                for elem in root.iter("mice" + "11"):
                    elem.set('drop', "Coins")
                frag_xml_tree.write("locations.xml")
            else:
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
        self.cheese_label.setText(cheese + ": " + GameLogic.ReadDataFromXML(GameLogic, "shop.xml", "item", "amount", cheese_index, 0))
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
            alert_exec = alert(text='Not enough energy or cheese', title='Alert', button='OK')

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

    def open_locations(self):
        locations = LocationsWindow()
        locations.exec_()
        self.update_ui()

    def open_about_locations(self):
        locations = AboutLocationWindow()
        locations.exec_()
        self.update_ui()

    def open_quests(self):
        locations = QuestsWindow()
        locations.exec_()
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
        JournalWindowUi.setWindowTitle(_translate("JournalWindowUi", "Journal"))
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
        self.gridLayout.addWidget(self.ok_button, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
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
            self.item_label = QtWidgets.QLabel(Inventory.Read(Inventory, "item", j) + " " + Inventory.Read(Inventory, "amount", j) + "x")
            self.item_label.setSizePolicy(self.sizePolicy)
            self.verticalLayout.addWidget(self.item_label)

            j += 1
        Inventory.Init(Inventory)


class AboutLocationWindowUi(object):

    def setupUi(self, AboutLocationWindowUi):
        AboutLocationWindowUi.setObjectName("JournalWindowUi")
        AboutLocationWindowUi.resize(600, 564)
        self.gridLayout = QtWidgets.QGridLayout(AboutLocationWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_button = QtWidgets.QPushButton(AboutLocationWindowUi)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.retranslateUi(AboutLocationWindowUi)
        QtCore.QMetaObject.connectSlotsByName(AboutLocationWindowUi)

    def retranslateUi(self, AboutLocationWindowUi):
        _translate = QtCore.QCoreApplication.translate
        AboutLocationWindowUi.setWindowTitle(_translate("JournalWindowUi", "Dialog"))
        self.ok_button.setText(_translate("JournalWindowUi", "OK"))


class AboutLocationWindow(QtWidgets.QDialog, AboutLocationWindowUi):
    def __init__(self, parent=None):
        super(AboutLocationWindow, self).__init__(parent)
        self.setupUi(self)

        self.ok_button.clicked.connect(self.close)

        i = int(GameLogic.ReadDataFromXML(self, "locations.xml", "location", "amount", location, 0))

        j = 1
        while j <= i:
            self.item_label = QtWidgets.QLabel(GameLogic.ReadDataFromXML(GameLogic, "locations.xml", "mice", "name", j, 0) + " " + GameLogic.ReadDataFromXML(GameLogic, "locations.xml", "location", "cheese", location, 0))

            self.item_label.setSizePolicy(self.sizePolicy)
            self.verticalLayout.addWidget(self.item_label)

            j += 1


class Ui_Quests(object):
    def setupUi(self, Quests):
        Quests.setObjectName("Quests")
        Quests.resize(438, 104)
        self.gridLayout = QtWidgets.QGridLayout(Quests)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(Quests)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.condition_label = QtWidgets.QLabel(Quests)
        self.condition_label.setObjectName("condition_label")
        self.gridLayout.addWidget(self.condition_label, 0, 1, 1, 1)
        self.ok_button = QtWidgets.QPushButton(Quests)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 1, 2, 1, 1)

        self.retranslateUi(Quests)
        QtCore.QMetaObject.connectSlotsByName(Quests)

    def retranslateUi(self, Quests):
        _translate = QtCore.QCoreApplication.translate
        Quests.setWindowTitle(_translate("Quests", "Dialog"))
        self.name_label.setText(_translate("Quests", "TextLabel"))
        self.condition_label.setText(_translate("Quests", "TextLabel"))
        self.ok_button.setText(_translate("Quests", "OK"))


class QuestsWindow(QtWidgets.QDialog, Ui_Quests):
    def __init__(self, parent=None):
        super(QuestsWindow, self).__init__(parent)
        self.setupUi(self)

        self.ok_button.clicked.connect(self.close)

        self.name_label.setText(Quests.LoadQuest(Quests, "name"))
        self.condition_label.setText(Quests.LoadQuest(Quests, "condition"))



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
                 device=device, board=board, quest=str(quest)):
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


class QuestsThread(Thread):
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        """Запуск потока"""
        global quest, energy_exec
        while energy_exec:
            if quest == 1 and GameLogic.ReadI(GameLogic, "journal.xml") > 0:
                quest += 1
            if quest == 2 and Inventory.Check(Inventory, "Key"):
                quest += 2
                frag_xml_tree = ET.parse("locations.xml")
                root = frag_xml_tree.getroot()
                for elem in root.iter("location" + "2"):
                    elem.set('state', "open")
                frag_xml_tree.write("locations.xml")


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

    def Check(self, item):
        filename = 'inventory.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        index = 0

        i = 0

        for line in lines:
            if line.find(item) != -1:
                return True
            index += 1
            i += 1
        return False


class Ui_Locations(object):
    def setupUi(self, Locations):
        Locations.setObjectName("Locations")
        Locations.resize(651, 601)
        self.scrollArea = QtWidgets.QScrollArea(Locations)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 651, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1148, 572))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 1, 11, 1, 2)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 9, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 0, 10, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 11, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 0, 12, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 2, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 5, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 2, 8, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_27 = QtWidgets.QLabel(self.groupBox_5)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 2, 1, 1, 1)
        self.location12 = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location12.sizePolicy().hasHeightForWidth())
        self.location12.setSizePolicy(sizePolicy)
        self.location12.setObjectName("location12")
        self.gridLayout_7.addWidget(self.location12, 2, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_5)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_5)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 1, 0, 1, 1)
        self.location13 = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location13.sizePolicy().hasHeightForWidth())
        self.location13.setSizePolicy(sizePolicy)
        self.location13.setObjectName("location13")
        self.gridLayout_7.addWidget(self.location13, 0, 1, 2, 1)
        self.gridLayout.addWidget(self.groupBox_5, 0, 6, 2, 4)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.location1 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location1.sizePolicy().hasHeightForWidth())
        self.location1.setSizePolicy(sizePolicy)
        self.location1.setObjectName("location1")
        self.gridLayout_2.addWidget(self.location1, 0, 0, 3, 1)
        self.location2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location2.sizePolicy().hasHeightForWidth())
        self.location2.setSizePolicy(sizePolicy)
        self.location2.setDefault(False)
        self.location2.setFlat(False)
        self.location2.setObjectName("location2")
        self.gridLayout_2.addWidget(self.location2, 1, 2, 3, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.location4 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location4.sizePolicy().hasHeightForWidth())
        self.location4.setSizePolicy(sizePolicy)
        self.location4.setObjectName("location4")
        self.gridLayout_3.addWidget(self.location4, 1, 2, 2, 1)
        self.location3 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location3.sizePolicy().hasHeightForWidth())
        self.location3.setSizePolicy(sizePolicy)
        self.location3.setObjectName("location3")
        self.gridLayout_3.addWidget(self.location3, 0, 0, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 2, 1, 1, 1)
        self.location11 = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location11.sizePolicy().hasHeightForWidth())
        self.location11.setSizePolicy(sizePolicy)
        self.location11.setObjectName("location11")
        self.gridLayout_6.addWidget(self.location11, 1, 2, 2, 1)
        self.location10 = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location10.sizePolicy().hasHeightForWidth())
        self.location10.setSizePolicy(sizePolicy)
        self.location10.setObjectName("location10")
        self.gridLayout_6.addWidget(self.location10, 0, 1, 2, 1)
        self.gridLayout.addWidget(self.groupBox_6, 4, 3, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.location5 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location5.sizePolicy().hasHeightForWidth())
        self.location5.setSizePolicy(sizePolicy)
        self.location5.setObjectName("location5")
        self.gridLayout_4.addWidget(self.location5, 0, 0, 2, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)
        self.location6 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location6.sizePolicy().hasHeightForWidth())
        self.location6.setSizePolicy(sizePolicy)
        self.location6.setObjectName("location6")
        self.gridLayout_4.addWidget(self.location6, 1, 2, 2, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.location7 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location7.sizePolicy().hasHeightForWidth())
        self.location7.setSizePolicy(sizePolicy)
        self.location7.setObjectName("location7")
        self.gridLayout_5.addWidget(self.location7, 1, 0, 4, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 1, 1, 1, 1)
        self.location8 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location8.sizePolicy().hasHeightForWidth())
        self.location8.setSizePolicy(sizePolicy)
        self.location8.setObjectName("location8")
        self.gridLayout_5.addWidget(self.location8, 2, 1, 4, 1)
        self.gridLayout.addWidget(self.groupBox_4, 3, 2, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Svartalheim = QtWidgets.QPushButton(self.groupBox_7)
        self.Svartalheim.setObjectName("Svartalheim")
        self.gridLayout_8.addWidget(self.Svartalheim, 0, 2, 1, 1)
        self.Niflheim = QtWidgets.QPushButton(self.groupBox_7)
        self.Niflheim.setObjectName("Niflheim")
        self.gridLayout_8.addWidget(self.Niflheim, 5, 1, 1, 1)
        self.Asgard = QtWidgets.QPushButton(self.groupBox_7)
        self.Asgard.setObjectName("Asgard")
        self.gridLayout_8.addWidget(self.Asgard, 0, 1, 1, 1)
        self.Midgard = QtWidgets.QPushButton(self.groupBox_7)
        self.Midgard.setObjectName("Midgard")
        self.gridLayout_8.addWidget(self.Midgard, 2, 1, 1, 1)
        self.Vanaheim = QtWidgets.QPushButton(self.groupBox_7)
        self.Vanaheim.setObjectName("Vanaheim")
        self.gridLayout_8.addWidget(self.Vanaheim, 0, 0, 1, 1)
        self.Aluheim = QtWidgets.QPushButton(self.groupBox_7)
        self.Aluheim.setObjectName("Aluheim")
        self.gridLayout_8.addWidget(self.Aluheim, 2, 0, 1, 1)
        self.Jotunheim = QtWidgets.QPushButton(self.groupBox_7)
        self.Jotunheim.setObjectName("Jotunheim")
        self.gridLayout_8.addWidget(self.Jotunheim, 2, 2, 1, 1)
        self.Nidavelir = QtWidgets.QPushButton(self.groupBox_7)
        self.Nidavelir.setObjectName("Nidavelir")
        self.gridLayout_8.addWidget(self.Nidavelir, 5, 0, 1, 1)
        self.Muspelheim = QtWidgets.QPushButton(self.groupBox_7)
        self.Muspelheim.setObjectName("Muspelheim")
        self.gridLayout_8.addWidget(self.Muspelheim, 5, 2, 1, 1)
        self.Musheim = QtWidgets.QPushButton(self.groupBox_7)
        self.Musheim.setObjectName("Musheim")
        self.gridLayout_8.addWidget(self.Musheim, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_7, 0, 13, 6, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Locations)
        QtCore.QMetaObject.connectSlotsByName(Locations)

    def retranslateUi(self, Locations):
        _translate = QtCore.QCoreApplication.translate
        Locations.setWindowTitle(_translate("Locations", "Dialog"))
        self.location12.setText(_translate("Locations", "Metro Station \"Begovaya\""))
        self.location13.setText(_translate("Locations", "Lahta Centre"))
        self.location1.setText(_translate("Locations", "Apartment"))
        self.location2.setText(_translate("Locations", "Outdoor"))
        self.location4.setText(_translate("Locations", "Shopping centre"))
        self.location3.setText(_translate("Locations", "Park"))
        self.location11.setText(_translate("Locations", "Air Gate"))
        self.location10.setText(_translate("Locations", "Platform"))
        self.location5.setText(_translate("Locations", "Metro"))
        self.location6.setText(_translate("Locations", "Entrance"))
        self.location7.setText(_translate("Locations", "Catacombs"))
        self.location8.setText(_translate("Locations", "Underground lake"))
        self.groupBox_7.setTitle(_translate("Locations", "Yiggdrassil"))
        self.Svartalheim.setText(_translate("Locations", "Svartalheim"))
        self.Niflheim.setText(_translate("Locations", "Niflheim"))
        self.Asgard.setText(_translate("Locations", "Asgard"))
        self.Midgard.setText(_translate("Locations", "Midgard"))
        self.Vanaheim.setText(_translate("Locations", "Vanaheim"))
        self.Aluheim.setText(_translate("Locations", "Aluheim"))
        self.Jotunheim.setText(_translate("Locations", "Jotunheim"))
        self.Nidavelir.setText(_translate("Locations", "Nidavelir"))
        self.Muspelheim.setText(_translate("Locations", "Muspelheim"))
        self.Musheim.setText(_translate("Locations", "Musheim"))


class LocationsWindow(QtWidgets.QDialog, Ui_Locations):
    def __init__(self, parent=None):
        super(LocationsWindow, self).__init__(parent)
        self.setupUi(self)


class Quests(object):

    def LoadQuest(self, attr):
        xmldoc = minidom.parse('quests.xml')
        itemlist = xmldoc.getElementsByTagName(str("quest")+str(quest))
        return itemlist[0].attributes[str(attr)].value


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
mouse_cost = GameLogic.ReadUserData(GameLogic, "last_cost", 0)
mouse_name = GameLogic.ReadUserData(GameLogic, "last_mouse", 0)
mouse_drop = GameLogic.ReadUserData(GameLogic, "last_drop", 0)
location = int(GameLogic.ReadUserData(GameLogic, "location", 0))
location_name = GameLogic.ReadDataFromXML(GameLogic,"locations.xml", "location", "name", location, 0)
mouse_icon = GameLogic.ReadUserData(GameLogic, "last_icon", 0)
device = GameLogic.ReadUserData(GameLogic, "device", 0)
energy_max = int(GameLogic.ReadUserData(GameLogic, "energy_max", 0))
board = GameLogic.ReadUserData(GameLogic, "board", 0)
quest = int(GameLogic.ReadUserData(GameLogic, "quest", 0))


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

thread = QuestsThread()
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
