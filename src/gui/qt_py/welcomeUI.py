# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created: Thu Dec 15 13:49:22 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 750)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.employeeBtn = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.employeeBtn.setFont(font)
        self.employeeBtn.setObjectName("employeeBtn")
        self.horizontalLayout_2.addWidget(self.employeeBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.welcomeLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setWordWrap(True)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.verticalLayout_2.addWidget(self.welcomeLabel)
        self.questionLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.questionLabel.setFont(font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName("questionLabel")
        self.verticalLayout_2.addWidget(self.questionLabel)
        self.yesButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.yesButton.setFont(font)
        self.yesButton.setObjectName("yesButton")
        self.verticalLayout_2.addWidget(self.yesButton)
        self.noButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.noButton.setFont(font)
        self.noButton.setObjectName("noButton")
        self.verticalLayout_2.addWidget(self.noButton)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeBtn.setText(QtGui.QApplication.translate("Form", "Employee Login", None, QtGui.QApplication.UnicodeUTF8))
        self.welcomeLabel.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Lidia\'s Pizza Palace</span></p><p align=\"center\">Our pizza is made from slow-rising sourdough made daily and is covered with the finest ingredients. </p><p align=\"center\"><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.questionLabel.setText(QtGui.QApplication.translate("Form", "Are you an existing customer?", None, QtGui.QApplication.UnicodeUTF8))
        self.yesButton.setText(QtGui.QApplication.translate("Form", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.noButton.setText(QtGui.QApplication.translate("Form", "No", None, QtGui.QApplication.UnicodeUTF8))

