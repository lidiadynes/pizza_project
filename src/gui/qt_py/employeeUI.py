# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Employee_Login.ui'
#
# Created: Thu Dec 15 13:59:03 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.employeeLineEdit = QtGui.QLineEdit(Form)
        self.employeeLineEdit.setObjectName("employeeLineEdit")
        self.verticalLayout.addWidget(self.employeeLineEdit)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backBtn = QtGui.QPushButton(Form)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.confirmBtn = QtGui.QPushButton(Form)
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout.addWidget(self.confirmBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Enter your employee login", None, QtGui.QApplication.UnicodeUTF8))
        self.backBtn.setText(QtGui.QApplication.translate("Form", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.confirmBtn.setText(QtGui.QApplication.translate("Form", "Confirm", None, QtGui.QApplication.UnicodeUTF8))

