# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ogban\Desktop\The-All-In-One-Project\The-All-In-One-Project\AIO Gui\InchesToCm.ui'
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
        Dialog.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.Close = QtWidgets.QPushButton(Dialog)
        self.Close.setGeometry(QtCore.QRect(0, 480, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Close.setFont(font)
        self.Close.setStyleSheet("background-color: rgb(213, 0, 0);")
        self.Close.setAutoDefault(False)
        self.Close.setDefault(False)
        self.Close.setObjectName("Close")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 510, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.Input_1 = QtWidgets.QLineEdit(Dialog)
        self.Input_1.setGeometry(QtCore.QRect(210, 150, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Input_1.setFont(font)
        self.Input_1.setStyleSheet("color: rgb(230, 200, 85);")
        self.Input_1.setText("")
        self.Input_1.setObjectName("Input_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(46)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(230, 200, 85);")
        self.label.setObjectName("label")
        self.Submit = QtWidgets.QPushButton(Dialog)
        self.Submit.setGeometry(QtCore.QRect(130, 250, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Submit.setFont(font)
        self.Submit.setStyleSheet("color: rgb(230, 200, 85);\n"
"background-color: rgb(42, 74, 89);")
        self.Submit.setObjectName("Submit")
        self.Output_2 = QtWidgets.QLineEdit(Dialog)
        self.Output_2.setGeometry(QtCore.QRect(30, 350, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Output_2.setFont(font)
        self.Output_2.setStyleSheet("color: rgb(230, 200, 85);")
        self.Output_2.setText("")
        self.Output_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Output_2.setObjectName("Output_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIO | Age"))
        self.Close.setText(_translate("Dialog", "Close"))
        self.label_3.setText(_translate("Dialog", "AIO \"GUI Edittion\" | Version: v-2.1.1 REV-3 | GUI Version:Alpha 0.0.4 | Copyright AIO 2022"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Inches</p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Inches To Mc</p></body></html>"))
        self.Submit.setText(_translate("Dialog", "Submit"))
