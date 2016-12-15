# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Message.ui'
#
# Created: Thu Dec 08 21:50:57 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 250)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.messageLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.messageLabel.setFont(font)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout.addWidget(self.messageLabel)
        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yesButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.yesButton.setFont(font)
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout.addWidget(self.yesButton)
        self.noButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.noButton.setFont(font)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.messageLabel.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">is not in our database. </p><p align=\"center\">Would you like to go to the new customer page?</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.yesButton.setText(QtGui.QApplication.translate("Form", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.noButton.setText(QtGui.QApplication.translate("Form", "No", None, QtGui.QApplication.UnicodeUTF8))

