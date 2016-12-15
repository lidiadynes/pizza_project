# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_Message.ui'
#
# Created: Mon Dec 12 10:24:31 2016
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
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Your order was made at .</p><p align=\"center\">Please come and collect your order in 45 minutes.</p><p align=\"center\"><br/></p><p align=\"center\">The location of our restaurant is:</p><p align=\"center\">Lidia\'s Pizza Palace</p><p align=\"center\">752 Earls Court Road</p><p align=\"center\">London</p><p align=\"center\">SW8 9TQ</p><p align=\"center\"><br/></p><p align=\"center\">Should there be any problem with your order</p><p align=\"center\">please call 02088776453</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

