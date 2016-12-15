# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Order_Summary.ui'
#
# Created: Thu Dec 08 23:13:15 2016
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
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.headerLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.orderLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.orderLabel.setFont(font)
        self.orderLabel.setObjectName("orderLabel")
        self.verticalLayout.addWidget(self.orderLabel)
        self.totalLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.totalLabel.setFont(font)
        self.totalLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.totalLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout.addWidget(self.totalLabel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
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
        self.label.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p>You have ordered:</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.headerLabel.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.orderLabel.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.totalLabel.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("Form", "Edit Order", None, QtGui.QApplication.UnicodeUTF8))
        self.confirmButton.setText(QtGui.QApplication.translate("Form", "Confirm Order", None, QtGui.QApplication.UnicodeUTF8))

