from src.gui.qt_py import employeeUI
from src.gui.qt_py import restaurantUI
import xlrd

from src.database import Database

from PySide.QtCore import *
from PySide.QtGui import *
import unicodedata

FILENAME = '..\..\data_storage\data.xls'
DETAILS_ROW = 0
ENABLE_EDITING = "Enable Editing"
SAVE_INFORMATION = "Save Information"

# Employee login window
class EmployeeLogin(QWidget, employeeUI.Ui_Form):
    def __init__(self, parent=None):
        super(EmployeeLogin, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.backBtn, SIGNAL("clicked()"), self.show_welcome)
        self.connect(self.confirmBtn, SIGNAL("clicked()"), self.show_restaurant)

    # Show welcome window if Back pressed
    def show_welcome(self):
        self.hide()
        from customerUI import Welcome
        self.window = Welcome()
        self.window.show()

    # Check login ID is valid by searching for it in database
    def check_login(self):
        w_sheet = xlrd.open_workbook(FILENAME).sheet_by_index(3)
        for row in range(1, w_sheet.nrows):
            details = w_sheet.cell_value(row, DETAILS_ROW)
            if details == self.employeeLineEdit.text():
                return True
        return False

    # Show restaurant page if login is valid. Otherwise message box saying wrong login
    def show_restaurant(self):
        if self.check_login():
            self.hide()
            self.window = Restaurant()
            self.window.show()
        else:
            QMessageBox.information(self, "Error", "Invalid login. Please try again.")


# Restaurant window; shows all data information about menu, customers, orders and statistics
class Restaurant(QTabWidget, restaurantUI.Ui_Form):
    def __init__(self, parent=None):
        super(Restaurant, self).__init__(parent)
        self.setupUi(self)

        self.database = Database(FILENAME)

        self.customer_editable = False
        self.order_editable = False
        self.menu_editable = False

        self.addCustomerBtn.setEnabled(False)
        self.deleteCustomerBtn.setEnabled(False)
        self.addOrderBtn.setEnabled(False)
        self.deleteOrderBtn.setEnabled(False)
        self.addItemBtn.setEnabled(False)
        self.deleteItemBtn.setEnabled(False)

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

        self.connect(self.customerEditButton, SIGNAL('clicked()'), self.edit_customer_info)
        self.connect(self.orderEditButton, SIGNAL('clicked()'), self.edit_order_info)
        self.connect(self.menuEditButton, SIGNAL('clicked()'), self.edit_menu_info)

    # Fill customer table with information from database
    def fill_customer_table(self):
        customers = xlrd.open_workbook(FILENAME).sheet_by_index(1)
        for row in range(1, customers.nrows):
            row_data = customers.row_values(row)
            row -= 1
            self.customerTable.removeRow(row)
            self.customerTable.insertRow(row)
            row_data = map(str, row_data)
            row_items = map(QTableWidgetItem, row_data)
            if not self.customer_editable:
                for item in row_items:
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            column = 0
            for item in row_items:
                self.customerTable.setItem(row, column, item)
                column += 1

    # Fill order table with information from database
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
            if not self.order_editable:
                for item in row_items:
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            column = 0
            for item in row_items:
                self.orderTable.setItem(row, column, item)
                column += 1

    # Fill customer table with information from database
    def fill_menu_table(self):
        menu_entries = self.database.get_menu_bst().entry_set()
        max_row_count = len(menu_entries)
        for row in range(0, max_row_count):
            self.menuTable.removeRow(row)
            self.menuTable.insertRow(row)
            name_item = QTableWidgetItem(menu_entries[row][0])
            price_item = QTableWidgetItem(str(menu_entries[row][1]))
            if not self.menu_editable:
                price_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.menuTable.setItem(row, 0, name_item)
            self.menuTable.setItem(row, 1, price_item)

    # Calculate statistics from database information and fill window
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

    # Toggle editable + fill customer page. Update info if editable unchecked + update statistics
    def edit_customer_info(self):
        self.customer_editable = not self.customer_editable
        if not self.customer_editable:
            self.customerEditButton.setText(ENABLE_EDITING)
            self.addCustomerBtn.setEnabled(False)
            self.deleteCustomerBtn.setEnabled(False)
            self.database.update_customer_info(self.customerTable)
            self.fill_statistics_table()
        else:
            self.customerEditButton.setText(SAVE_INFORMATION)
            self.addCustomerBtn.setEnabled(True)
            self.deleteCustomerBtn.setEnabled(True)
        self.fill_customer_table()

    # Toggle editable + fill order page. Update info if editable unchecked + update statistics
    def edit_order_info(self):
        self.order_editable = not self.order_editable
        if not self.order_editable:
            self.orderEditButton.setText(ENABLE_EDITING)
            self.addOrderBtn.setEnabled(False)
            self.deleteOrderBtn.setEnabled(False)
            self.database.update_order_info(self.orderTable)
        else:
            self.orderEditButton.setText(SAVE_INFORMATION)
            self.addOrderBtn.setEnabled(True)
            self.deleteOrderBtn.setEnabled(True)
        self.fill_order_table()
        self.fill_statistics_table()

    # Toggle editable + fill menu page. Update info if editable unchecked + update statistics
    def edit_menu_info(self):
        self.menu_editable = not self.menu_editable
        if not self.menu_editable:
            self.menuEditButton.setText(ENABLE_EDITING)
            self.addItemBtn.setEnabled(False)
            self.deleteItemBtn.setEnabled(False)
            self.database.update_menu_info(self.menuTable)
        else:
            self.menuEditButton.setText(SAVE_INFORMATION)
            self.addItemBtn.setEnabled(True)
            self.deleteItemBtn.setEnabled(True)
        self.fill_menu_table()
        self.fill_statistics_table()

    # Add customer to selected row with default values
    def add_customer(self):
        if self.customer_editable:
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

    # Add order to selected row with default values
    def add_order(self):
        if self.order_editable:
            selected_row = self.orderTable.currentRow()
            self.orderTable.insertRow(selected_row + 1)
            self.orderTable.setItem(selected_row + 1, 0, QTableWidgetItem("0"))
            self.orderTable.setItem(selected_row + 1, 1, QTableWidgetItem("00/00/0000"))
            self.orderTable.setItem(selected_row + 1, 2, QTableWidgetItem("00:00"))
            self.orderTable.setItem(selected_row + 1, 3, QTableWidgetItem(" "))
            self.orderTable.setItem(selected_row + 1, 4, QTableWidgetItem("0"))

    # Add menu item to selected row with default values
    def add_menu_item(self):
        if self.menu_editable:
            selected_row = self.menuTable.currentRow()
            self.menuTable.insertRow(selected_row + 1)
            self.menuTable.setItem(selected_row + 1, 0, QTableWidgetItem("Item"))
            self.menuTable.setItem(selected_row + 1, 1, QTableWidgetItem("0"))

    # Delete customer from selectd row
    def delete_customer(self):
        if self.customer_editable:
            selected_row = self.customerTable.currentRow()
            self.customerTable.removeRow(selected_row)

    # Delete order from selected row
    def delete_order(self):
        if self.order_editable:
            selected_row = self.orderTable.currentRow()
            self.orderTable.removeRow(selected_row)

    # Delete menu item from selected row
    def delete_menu_item(self):
        if self.menu_editable:
            selected_row = self.menuTable.currentRow()
            self.menuTable.removeRow(selected_row)
