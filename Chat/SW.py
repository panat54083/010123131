# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SW_Chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SW2 import *


class Ui_MainWindow1(object):
    def connect(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
        # SW_Chat.hide()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Icon = QtWidgets.QLabel(self.centralwidget)
        self.Icon.setGeometry(QtCore.QRect(260, 90, 251, 231))
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("mail-send.png"))
        self.Icon.setScaledContents(True)
        self.Icon.setOpenExternalLinks(False)
        self.Icon.setObjectName("Icon")
        self.EnterUsername = QtWidgets.QLabel(self.centralwidget)
        self.EnterUsername.setGeometry(QtCore.QRect(80, 310, 311, 81))
        self.EnterUsername.setObjectName("EnterUsername")
        self.InputUser = QtWidgets.QLineEdit(self.centralwidget)
        self.InputUser.setGeometry(QtCore.QRect(400, 320, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.InputUser.setFont(font)
        self.InputUser.setObjectName("InputUser")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 800, 530))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("Background.png"))
        self.Background.setObjectName("Background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 301, 141))
        self.label.setObjectName("label")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(360, 410, 93, 28))
        self.connectButton.setObjectName("ConnectButton")
        self.Background.raise_()
        self.Icon.raise_()
        self.EnterUsername.raise_()
        self.InputUser.raise_()
        self.label.raise_()
        self.connectButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SW-Chat", "SW-Chat"))
        self.EnterUsername.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Enter Username :</span></p></body></html>"))
        self.InputUser.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">SW-CHAT</span></p></body></html>"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SW_Chat = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(SW_Chat)
    SW_Chat.show()
    sys.exit(app.exec_())

