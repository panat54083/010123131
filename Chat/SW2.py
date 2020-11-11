# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SW2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Background.png"))
        self.label.setObjectName("label")
        self.Disconnect = QtWidgets.QPushButton(self.centralwidget)
        self.Disconnect.setGeometry(QtCore.QRect(70, 430, 93, 28))
        self.Disconnect.setObjectName("Disconnect")
        self.TypeHere = QtWidgets.QTextEdit(self.centralwidget)
        self.TypeHere.setGeometry(QtCore.QRect(310, 340, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TypeHere.setFont(font)
        self.TypeHere.setObjectName("TypeHere")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(640, 430, 93, 28))
        self.Send.setObjectName("Send")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 20, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border: 0;")
        self.textBrowser.setObjectName("textBrowser")
        self.Usernamedisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.Usernamedisplay.setGeometry(QtCore.QRect(70, 350, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Usernamedisplay.setFont(font)
        self.Usernamedisplay.setStyleSheet("border: 0;")
        self.Usernamedisplay.setObjectName("Usernamedisplay")
        self.user_online = QtWidgets.QTextBrowser(self.centralwidget)
        self.user_online.setGeometry(QtCore.QRect(70, 80, 211, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.user_online.setFont(font)
        self.user_online.setObjectName("user_online")
        self.showText = QtWidgets.QTextBrowser(self.centralwidget)
        self.showText.setGeometry(QtCore.QRect(70, 80, 661, 231))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showText.setFont(font)
        self.showText.setObjectName("showText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Online</span></p></body></html>"))
        self.Usernamedisplay.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">I Here Too</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SW_Chat = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(SW_Chat)
    SW_Chat.show()
    sys.exit(app.exec_())
