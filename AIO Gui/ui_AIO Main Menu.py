# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Ollie\source\repos\The-All-In-One-Project\AIO Gui\AIO Main Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 530)
        Dialog.setMinimumSize(QtCore.QSize(491, 530))
        Dialog.setMaximumSize(QtCore.QSize(491, 530))
        font = QtGui.QFont()
        font.setPointSize(30)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setGeometry(QtCore.QRect(0, 10, 491, 526))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 451, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(230, 200, 85);")
        self.label.setObjectName("label")
        self.Personal = QtWidgets.QPushButton(self.centralwidget)
        self.Personal.setGeometry(QtCore.QRect(130, 90, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Personal.setFont(font)
        self.Personal.setStyleSheet("color: rgb(230, 200, 85);\n"
"background-color: rgb(42, 74, 89);")
        self.Personal.setObjectName("Personal")
        self.Caculations = QtWidgets.QPushButton(self.centralwidget)
        self.Caculations.setGeometry(QtCore.QRect(130, 160, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Caculations.setFont(font)
        self.Caculations.setStyleSheet("background-color: rgb(42, 74, 89);\n"
"color: rgb(230, 200, 85);")
        self.Caculations.setObjectName("Caculations")
        self.Games = QtWidgets.QPushButton(self.centralwidget)
        self.Games.setGeometry(QtCore.QRect(130, 300, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Games.setFont(font)
        self.Games.setStyleSheet("background-color: rgb(42, 74, 89);\n"
"color: rgb(230, 200, 85);")
        self.Games.setObjectName("Games")
        self.Errors = QtWidgets.QPushButton(self.centralwidget)
        self.Errors.setGeometry(QtCore.QRect(130, 370, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Errors.setFont(font)
        self.Errors.setStyleSheet("background-color: rgb(42, 74, 89);\n"
"color: rgb(230, 200, 85);")
        self.Errors.setObjectName("Errors")
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(0, 470, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Close.setFont(font)
        self.Close.setStyleSheet("background-color: rgb(213, 0, 0);")
        self.Close.setAutoDefault(False)
        self.Close.setDefault(False)
        self.Close.setObjectName("Close")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 500, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 491, 20))
        self.line.setMaximumSize(QtCore.QSize(491, 150))
        self.line.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Errors_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Errors_2.setGeometry(QtCore.QRect(130, 230, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Errors_2.setFont(font)
        self.Errors_2.setStyleSheet("background-color: rgb(42, 74, 89);\n"
"color: rgb(230, 200, 85);")
        self.Errors_2.setObjectName("Errors_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIO | Main Menu"))
        Dialog.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Dialog</p></body></html>"))
        self.label.setText(_translate("Dialog", "Welcome To AIO"))
        self.Personal.setText(_translate("Dialog", "Personal"))
        self.Caculations.setText(_translate("Dialog", "Caculations"))
        self.Games.setText(_translate("Dialog", "\"Games Comming Soon\""))
        self.Errors.setText(_translate("Dialog", "Error Codes"))
        self.Close.setText(_translate("Dialog", "Close"))
        self.label_3.setText(_translate("Dialog", "AIO \"GUI Edittion\" | Version: v-2.1.1 REV-3 | GUI Version:Alpha 0.0.4 | Copyright AIO 2022"))
        self.Errors_2.setText(_translate("Dialog", "Notepad"))
