from src.gui.qt_py import welcomeUI
from src.gui.qt_py import existingCustomerUI
from src.gui.qt_py import messageUI
from src.gui.qt_py import newCustomerUI
from src.gui.qt_py import orderMenuUI
from src.gui.qt_py import orderSummaryUI
from src.gui.qt_py import finalMessageUI

from src.order import Order
from src.customer import Customer
from src.database import Database
from employeeUI import EmployeeLogin

from PySide.QtCore import *
from PySide.QtGui import *
import datetime

FILENAME = '..\..\data_storage\data.xls'

# Welcome screen
class Welcome(QWidget, welcomeUI.Ui_Form):
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.yesButton, SIGNAL('clicked()'), self.show_existing_customer)
        self.connect(self.noButton, SIGNAL('clicked()'), self.show_new_customer)
        self.connect(self.employeeBtn, SIGNAL('clicked()'), self.show_login)

    # Show login screen if employee login pressed
    def show_login(self):
        self.hide()
        self.window = EmployeeLogin()
        self.window.show()

    # Show existing customer screen if Yes pressed
    def show_existing_customer(self):
        self.hide()
        self.window = ExistingCustomer()
        self.window.show()

    # Show new customer screen if No pressed
    def show_new_customer(self):
        self.hide()
        self.window = NewCustomer()
        self.window.show()

# Screen for existing customers
class ExistingCustomer(QWidget, existingCustomerUI.Ui_Form):
    def __init__(self, parent=None):
        super(ExistingCustomer, self).__init__(parent)
        self.setupUi(self)
        self.database = Database(FILENAME)

        self.connect(self.confirmButton, SIGNAL('clicked()'), self.show_order_menu)
        self.connect(self.previousButton, SIGNAL('clicked()'), self.show_welcome)

    # Check phone input and show menu page if details are correct.
    # Otherwise shows message box with error msg/NotInDatabase window
    def show_order_menu(self):
        if not self.phoneInput.text():
            QMessageBox.information(self, "Error",
                                    "Please fill in your phone number before pressing the confirm button")
        elif len(self.phoneInput.text()) != 11 or not self.phoneInput.text().isdigit():
            QMessageBox.information(self, "Error", "Please enter an 11 digit number")
        else:
            if self.database.does_customer_exist(self.phoneInput.text()):
                self.hide()
                self.window = OrderMenu(self.database.get_customer(self.phoneInput.text()), self.database)
                self.window.show()
            else:
                self.window = NotInDatabase(self.phoneInput.text(), self)
                self.window.show()

    # Show welcome page if Back button pressed
    def show_welcome(self):
        self.hide()
        self.window = Welcome()
        self.window.show()

# Window that lets customer know phone number is already in database on NewCustomer page
class ExistsInDatabase(QWidget, messageUI.Ui_Form):
    def __init__(self, number, database, background_window, parent=None):
        super(ExistsInDatabase, self).__init__(parent)
        self.setupUi(self)
        self.number = number
        self.database = database
        self.background_window = background_window
        self.messageLabel.setText("<html><head/><body><p align=\"center\">" + str(
            self.number) + " is in our database. </p><p align=\"center\">Would you like to make an order using this number?</p></body></html>")

        self.connect(self.yesButton, SIGNAL('clicked()'), self.show_new_customer)
        self.connect(self.noButton, SIGNAL('clicked()'), self.show_order_menu)

    # Hide screen
    def show_order_menu(self):
        self.hide()

    # Show new customer screen
    def show_new_customer(self):
        self.hide()
        self.background_window.hide()
        self.window = OrderMenu(self.database.get_customer(self.number), self.database)
        self.window.show()


# Window that lets customer know phone number is not in database on ExistingCustomer page
class NotInDatabase(QWidget, messageUI.Ui_Form):
    def __init__(self, number, background_window, parent=None):
        super(NotInDatabase, self).__init__(parent)
        self.setupUi(self)
        self.number = number
        self.background_window = background_window
        self.messageLabel.setText("<html><head/><body><p align=\"center\">" + str(
            self.number) + " is not in our database. </p><p align=\"center\">Would you like to go to the new customer page?</p></body></html>")

        self.connect(self.yesButton, SIGNAL('clicked()'), self.show_existing_customer)
        self.connect(self.noButton, SIGNAL('clicked()'), self.show_new_customer)

    # Show NewCustomer page
    def show_new_customer(self):
        self.hide()

    # Show ExistingCustomer page
    def show_existing_customer(self):
        self.hide()
        self.background_window.hide()
        self.window = NewCustomer()
        self.window.show()

# Page for new customers to fill in details. Checks for blank fields + if phone number is already in database
class NewCustomer(QWidget, newCustomerUI.Ui_Form):
    def __init__(self, parent=None):
        super(NewCustomer, self).__init__(parent)
        self.setupUi(self)
        self.database = Database(FILENAME)

        self.connect(self.confirmButton, SIGNAL('clicked()'), self.show_order_menu)
        self.connect(self.previousButton, SIGNAL('clicked()'), self.show_welcome)

    # Checks fields + shows menu if correct. Otherwise shows error message/ExistsInDatabase screen
    def show_order_menu(self):
        if not self.firstNameInput.text() or not self.lastNameInput.text() or not self.postcodeInput.text() \
                or not self.phoneInput.text() or not self.emailInput.text():
            QMessageBox.information(self, "Error", "Please fill in your details before pressing the confirm button")
        elif not self.firstNameInput.text().isalpha() or not self.lastNameInput.text().isalpha():
            QMessageBox.information(self, "Error", "Please fill in your name using only letters (no spaces or symbols)")
        elif len(self.phoneInput.text()) != 11 or not self.phoneInput.text().isdigit():
            QMessageBox.information(self, "Error", "Please enter an 11 digit phone number")
        else:
            if not self.database.does_customer_exist(self.phoneInput.text()):
                customer, database = self.make_customer()
                self.hide()
                self.window = OrderMenu(customer, database)
                self.window.show()
            else:
                self.window = ExistsInDatabase(self.phoneInput.text(), self.database, self)
                self.window.show()

    # Create customer object + initialise database
    def make_customer(self):
        first_name = self.firstNameInput.text()
        last_name = self.lastNameInput.text()
        postcode = self.postcodeInput.text()
        phone = self.phoneInput.text()
        email = self.emailInput.text()
        customer = Customer(first_name, last_name, postcode, phone, email)
        database = Database(FILENAME)
        return customer, database

    # Show welcome screen if Back pressed
    def show_welcome(self):
        self.hide()
        self.window = Welcome()
        self.window.show()

# Show Menu screen. Lists items + prices with quantities
class OrderMenu(QWidget, orderMenuUI.Ui_Form):
    def __init__(self, customer, database, order=None, parent=None):
        super(OrderMenu, self).__init__(parent)
        self.setupUi(self)
        self.customer = customer
        self.database = database
        self.order = order

        self.menu = self.database.get_menu_bst()
        self.entries = self.menu.entry_set()
        self.max_row_count = len(self.entries)

        self.fill_table()
        self.connect(self.confirmButton, SIGNAL('clicked()'), self.show_order_summary)

    # If order not initialised, initialises order with inputted item quantity values. Otherwise edits existing order.
    # Checks fields and shows error message if incorrect
    def show_order_summary(self):
        items = {}
        invalid_character = False

        for row in range(0, self.max_row_count):
            if not self.tableWidget.item(row, 2).text().isdigit():
                invalid_character = True
                QMessageBox.information(self, "Error", "Please enter a whole number")
                break
            else:
                qty = int(self.tableWidget.item(row, 2).text())
                name = self.entries[row][0]
                if not qty == 0:
                    if self.order == None:
                        items[name] = qty
                    else:
                        self.order.set_qty(name, qty)
                elif self.order != None and self.order.items.keys().count(name) == 1:
                    self.order.remove_item(name)
            if self.order == None:
                self.order = Order(self.menu, items, self.database.order_number)
        if not invalid_character:
            self.hide()
            self.window = OrderSummary(self.customer, self.database, self.order)
            self.window.show()

    # Fill Menu table with items from database
    def fill_table(self):
        for row in range(0, self.max_row_count):
            self.tableWidget.setColumnWidth(0, 420)
            self.tableWidget.setColumnWidth(1, 140)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.insertRow(row)

            name = self.entries[row][0]
            name_item = QTableWidgetItem(name)
            name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            price = unichr(163) + "%.2f" % self.menu.get(name)
            price_item = QTableWidgetItem(price)
            price_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.tableWidget.setItem(row, 0, name_item)
            self.tableWidget.setItem(row, 1, price_item)

            if self.order == None:
                self.tableWidget.setItem(row, 2, QTableWidgetItem('0'))
            else:
                self.tableWidget.setItem(row, 2,
                                         QTableWidgetItem(str(self.order.number_of_items(self.entries[row][0]))))

# Order summary window
class OrderSummary(QWidget, orderSummaryUI.Ui_Form):
    def __init__(self, customer, database, order, parent=None):
        super(OrderSummary, self).__init__(parent)
        self.setupUi(self)
        self.customer = customer
        self.database = database
        self.order = order
        self.headerLabel.setText("Item".ljust(28) + "Quantity".ljust(12) + "Price")
        self.orderLabel.setText(self.order.to_string())
        self.totalLabel.setText("Total cost is:".ljust(40) + unichr(163) + "%.2f" % self.order.cost)

        self.connect(self.editButton, SIGNAL("clicked()"), self.show_order_menu)
        self.connect(self.confirmButton, SIGNAL("clicked()"), self.show_final_message)

    # Show order menu if back pressed
    def show_order_menu(self):
        self.hide()
        self.window = OrderMenu(self.customer, self.database, self.order)
        self.window.show()

    # Show confirmation window if confirm pressed. Add order + customer info to database.
    def show_final_message(self):
        self.order.day_ordered = "%02d / %02d / %04d" % (
            int(datetime.datetime.now().day), int(datetime.datetime.now().month), int(datetime.datetime.now().year))
        self.order.time_ordered = "%02d : %02d" % (
            int(datetime.datetime.now().hour), int(datetime.datetime.now().minute))
        if self.database.does_customer_exist(self.customer.phone):
            self.database.add_customer_order(self.customer, self.order)
        else:
            self.database.add_customer(self.customer, self.order)
        self.database.add_order(self.order)
        self.hide()
        self.window = FinalMessage(self.order)
        self.window.show()

# Order confirmation window
class FinalMessage(QWidget, finalMessageUI.Ui_Form):
    def __init__(self, order, parent=None):
        super(FinalMessage, self).__init__(parent)
        self.setupUi(self)
        self.label.setText(
            "<html><head/><body><p align=\"center\">Your order was made at " + order.time_ordered + "." + "</p><p align=\"center\">Please come and collect your order in 45 minutes.</p><p align=\"center\"><br/></p><p align=\"center\">The location of our restaurant is:</p><p align=\"center\">Lidia\'s Pizza Palace</p><p align=\"center\">752 Earls Court Road</p><p align=\"center\">London</p><p align=\"center\">SW8 9TQ</p><p align=\"center\"><br/></p><p align=\"center\">Should there be any problem with your order</p><p align=\"center\">please call 02088776453</p></body></html>")
