# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Existing_Customer.ui'
#
# Created: Thu Dec 08 21:51:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 750)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.questionLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.questionLabel.setFont(font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName("questionLabel")
        self.verticalLayout.addWidget(self.questionLabel)
        self.phoneInput = QtGui.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.phoneInput.setFont(font)
        self.phoneInput.setObjectName("phoneInput")
        self.verticalLayout.addWidget(self.phoneInput)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.empty1 = QtGui.QLabel(Form)
        self.empty1.setText("")
        self.empty1.setObjectName("empty1")
        self.verticalLayout.addWidget(self.empty1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.previousButton.setFont(font)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.confirmButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.questionLabel.setText(QtGui.QApplication.translate("Form", "What is your phone number?", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setText(QtGui.QApplication.translate("Form", "Previous Page", None, QtGui.QApplication.UnicodeUTF8))
        self.confirmButton.setText(QtGui.QApplication.translate("Form", "Confirm Number", None, QtGui.QApplication.UnicodeUTF8))

