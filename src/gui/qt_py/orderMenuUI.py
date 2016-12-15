# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Order_Menu.ui'
#
# Created: Thu Dec 08 23:07:26 2016
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
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtGui.QTableWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.confirmButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.verticalLayout_2.addWidget(self.confirmButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Change the quantities to complete your order</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Item", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.confirmButton.setText(QtGui.QApplication.translate("Form", "Confirm Order", None, QtGui.QApplication.UnicodeUTF8))

