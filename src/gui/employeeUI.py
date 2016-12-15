from src.gui.qt_py import employeeUI
from src.gui.qt_py import restaurantUI
import xlrd

from src.menu import Menu
from src.database import Database

from PySide.QtCore import *
from PySide.QtGui import *
import unicodedata

FILENAME = '..\..\data_storage\data.xls'
DETAILS_ROW = 0


class EmployeeLogin(QWidget, employeeUI.Ui_Form):
    def __init__(self, parent=None):
        super(EmployeeLogin, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.backBtn, SIGNAL("clicked()"), self.show_welcome)
        self.connect(self.confirmBtn, SIGNAL("clicked()"), self.show_restaurant)

    def show_welcome(self):
        self.hide()
        from customerUI import Welcome
        self.window = Welcome()
        self.window.show()

    def check_login(self):
        w_sheet = xlrd.open_workbook(FILENAME).sheet_by_index(3)
        for row in range(1, w_sheet.nrows):
            details = w_sheet.cell_value(row, DETAILS_ROW)
            if details == self.employeeLineEdit.text():
                return True
        return False

    def show_restaurant(self):
        if self.check_login():
            self.hide()
            self.window = Restaurant()
            self.window.show()
        else:
            QMessageBox.information(self, "Error", "Wrong login. Please try again.")


class Restaurant(QTabWidget, restaurantUI.Ui_Form):
    def __init__(self, parent=None):
        super(Restaurant, self).__init__(parent)
        self.setupUi(self)

        self.menu = Menu(FILENAME)
        self.database = Database(FILENAME)
        self.entries = self.menu.menu_bst.entry_set()
        self.maxRowCount = len(self.entries)

        self.customerChecked = False
        self.orderChecked = False
        self.menuChecked = False

        self.fill_customer_table()
        self.fill_order_table()
        self.fill_menu_table()
        self.fill_statistics_table()

        self.connect(self.addCustomerBtn, SIGNAL('clicked()'), self.add_customer)
        self.connect(self.deleteCustomerBtn, SIGNAL('clicked()'), self.delete_customer)
        self.connect(self.addOrderBtn, SIGNAL('clicked()'), self.add_order)
        self.connect(self.deleteOrderBtn, SIGNAL('clicked()'), self.delete_order)
        self.connect(self.addItemBtn, SIGNAL('clicked()'), self.add_menu_item)
        self.connect(self.deleteItemBtn, SIGNAL('clicked()'), self.delete_menu_item)

        self.connect(self.customerCheckBox, SIGNAL('clicked()'), self.edit_customer_info)
        self.connect(self.orderCheckBox, SIGNAL('clicked()'), self.edit_order_info)
        self.connect(self.menuCheckBox, SIGNAL('clicked()'), self.edit_menu_info)

    def fill_customer_table(self):
        customers = xlrd.open_workbook(FILENAME).sheet_by_index(1)
        for row in range(1, customers.nrows):
            row_data = customers.row_values(row)
            row -= 1
            self.customerTable.removeRow(row)
            self.customerTable.insertRow(row)
            row_data = map(str, row_data)
            row_items = map(QTableWidgetItem, row_data)
            if not self.customerChecked:
                for item in row_items:
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            column = 0
            for item in row_items:
                self.customerTable.setItem(row, column, item)
                column += 1

    def fill_order_table(self):
        orders = xlrd.open_workbook(FILENAME).sheet_by_index(2)
        for row in range(1, orders.nrows):
            row_data = orders.row_values(row)
            row -= 1
            self.orderTable.removeRow(row)
            self.orderTable.insertRow(row)
            row_data[0] = int(row_data[0])
            row_data = map(str, row_data)
            row_items = map(QTableWidgetItem, row_data)
            if not self.orderChecked:
                for item in row_items:
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            column = 0
            for item in row_items:
                self.orderTable.setItem(row, column, item)
                column += 1

    def fill_menu_table(self):
        self.menu = Menu(FILENAME)
        self.entries = self.menu.menu_bst.entry_set()
        for row in range(0, self.maxRowCount):
            self.menuTable.removeRow(row)
            self.menuTable.insertRow(row)
            name_item = QTableWidgetItem(self.entries[row][0])
            price_item = QTableWidgetItem(str(self.entries[row][1]))
            if not self.menuChecked:
                price_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.menuTable.setItem(row, 0, name_item)
            self.menuTable.setItem(row, 1, price_item)

    def fill_statistics_table(self):
        statistics = self.database.get_all_statistics()
        for row in range(0, len(statistics)):
            statistic_name, statistic_value = statistics[row]
            self.statisticsTable.removeRow(row)
            self.statisticsTable.insertRow(row)
            statistic_name_item = QTableWidgetItem(statistic_name)
            statistic_value_item = QTableWidgetItem(statistic_value)
            statistic_name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            statistic_value_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.statisticsTable.setItem(row, 0, statistic_name_item)
            self.statisticsTable.setItem(row, 1, statistic_value_item)

    def edit_customer_info(self):
        self.customerChecked = not self.customerChecked
        if not self.customerChecked:
            self.database.update_customer_info(self.customerTable)
        self.fill_customer_table()
        self.fill_statistics_table()

    def edit_order_info(self):
        self.orderChecked = not self.orderChecked
        if not self.orderChecked:
            self.database.update_order_info(self.orderTable)
        self.fill_order_table()
        self.fill_statistics_table()

    def edit_menu_info(self):
        self.menuChecked = not self.menuChecked
        if not self.menuChecked:
            self.database.update_menu_info(self.menuTable)
        self.fill_menu_table()
        self.fill_statistics_table()

    def add_customer(self):
        if self.customerChecked:
            selected_row = self.customerTable.currentRow()
            self.customerTable.insertRow(selected_row + 1)
            self.customerTable.setItem(selected_row + 1, 0, QTableWidgetItem("First Name"))
            self.customerTable.setItem(selected_row + 1, 1, QTableWidgetItem("Last Name"))
            self.customerTable.setItem(selected_row + 1, 2, QTableWidgetItem("Postcode"))
            self.customerTable.setItem(selected_row + 1, 3, QTableWidgetItem("0"))
            self.customerTable.setItem(selected_row + 1, 4, QTableWidgetItem("Email"))
            self.customerTable.setItem(selected_row + 1, 5, QTableWidgetItem("0"))
            self.customerTable.setItem(selected_row + 1, 6, QTableWidgetItem("0"))
            self.customerTable.setItem(selected_row + 1, 7, QTableWidgetItem("0"))

    def add_order(self):
        if self.orderChecked:
            selected_row = self.orderTable.currentRow()
            self.orderTable.insertRow(selected_row + 1)
            self.orderTable.setItem(selected_row + 1, 0, QTableWidgetItem("0"))
            self.orderTable.setItem(selected_row + 1, 1, QTableWidgetItem("Date"))
            self.orderTable.setItem(selected_row + 1, 2, QTableWidgetItem("Time"))
            self.orderTable.setItem(selected_row + 1, 3, QTableWidgetItem("Items"))
            self.orderTable.setItem(selected_row + 1, 4, QTableWidgetItem("0"))

    def add_menu_item(self):
        if self.menuChecked:
            selected_row = self.menuTable.currentRow()
            self.menuTable.insertRow(selected_row + 1)
            self.menuTable.setItem(selected_row + 1, 0, QTableWidgetItem("Item"))
            self.menuTable.setItem(selected_row + 1, 1, QTableWidgetItem("0"))

    def delete_customer(self):
        if self.customerChecked:
            selected_row = self.customerTable.currentRow()
            self.customerTable.removeRow(selected_row)

    def delete_order(self):
        if self.orderChecked:
            selected_row = self.orderTable.currentRow()
            self.orderTable.removeRow(selected_row)

    def delete_menu_item(self):
        if self.menuChecked:
            selected_row = self.menuTable.currentRow()
            self.menuTable.removeRow(selected_row)
