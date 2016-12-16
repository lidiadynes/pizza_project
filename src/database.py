import unicodedata
import xlrd
from xlutils.copy import copy
from customer import Customer
import datetime

from src.util.bst import BinarySearchTree

PHONE_COL = 3
MONEY_COL = 7
DATE_COL = 1
TOTAL_COL = 4


# Class for managing database
class Database:
    def __init__(self, filename):
        self.filename = filename
        self.order_number = xlrd.open_workbook(self.filename).sheet_by_index(2).nrows

    # Boolean that checks if phone number is in customer database
    def does_customer_exist(self, phone):
        w_sheet = xlrd.open_workbook(self.filename).sheet_by_index(1)
        for row in range(1, w_sheet.nrows):
            number = w_sheet.cell_value(row, PHONE_COL)
            if number == phone:
                return True
        return False

    # Returns row of customer in customer database if phone exists, otherwise -1
    def find_customer_row(self, phone):
        read_book = xlrd.open_workbook(self.filename)
        w_sheet = read_book.sheet_by_index(1)
        for row in range(1, w_sheet.nrows):
            number = w_sheet.cell_value(row, PHONE_COL)
            if number == phone:
                return row
        return -1

    # Create bst representing menu
    def get_menu_bst(self):
        menu_bst = BinarySearchTree()
        menu = xlrd.open_workbook(self.filename).sheet_by_index(0)
        for item in range(1, menu.nrows):
            name, price = menu.row_values(item)
            name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
            menu_bst.put(name, price)
        return menu_bst

    # Creates customer object from database
    def get_customer(self, phone):
        read_book = xlrd.open_workbook(self.filename)
        w_sheet = read_book.sheet_by_index(1)
        row = self.find_customer_row(phone)
        first_name, last_name, postcode, phone, email, order_numbers, total_orders, money_spent = w_sheet.row_values(
            row)
        if not order_numbers:
            order_numbers = []
        else:
            order_numbers = str(int(order_numbers))
            order_numbers = map(int, order_numbers.split(","))
        return Customer(first_name, last_name, postcode, phone, email,
                        order_numbers, int(total_orders), float(money_spent))

    # Add new customer to customer database with an initial order if customer isn't in customer database
    def add_customer(self, customer, order):
        if not self.does_customer_exist(customer.phone):
            customer.add_customer_order(order)
            read_book = xlrd.open_workbook(self.filename)
            row = read_book.sheet_by_index(1).nrows
            write_book = copy(read_book)
            w_sheet = write_book.get_sheet(1)
            customer.order_numbers = [order.order_number]
            w_sheet.write(row, 0, customer.first_name)
            w_sheet.write(row, 1, customer.last_name)
            w_sheet.write(row, 2, customer.postcode)
            w_sheet.write(row, 3, customer.phone)
            w_sheet.write(row, 4, customer.email)
            w_sheet.write(row, 5, customer.order_numbers[0])
            w_sheet.write(row, 6, customer.total_orders)
            w_sheet.write(row, 7, customer.money_spent)
            write_book.save(self.filename.replace('xlsx', 'xls'))

    # Add order to customer in customer database
    def add_customer_order(self, customer, order):
        customer.add_customer_order(order)
        read_book = xlrd.open_workbook(self.filename)
        row = self.find_customer_row(customer.phone)
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(1)
        w_sheet.write(row, 5, ', '.join([str(i) for i in customer.order_numbers]))
        w_sheet.write(row, 6, customer.total_orders)
        w_sheet.write(row, 7, customer.money_spent)
        write_book.save(self.filename.replace('xlsx', 'xls'))

    # Add order to order database
    def add_order(self, order):
        read_book = xlrd.open_workbook(self.filename)
        row = read_book.sheet_by_index(2).nrows
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(2)
        w_sheet.write(row, 0, order.order_number)
        w_sheet.write(row, 1, str(order.day_ordered))
        w_sheet.write(row, 2, str(order.time_ordered))
        w_sheet.write(row, 3, ', '.join(['{0} ({1})'.format(name, qty) for name, qty in order.items.iteritems()]))
        w_sheet.write(row, 4, order.cost)
        write_book.save(self.filename.replace('xlsx', 'xls'))

    # Re-write customer database with values in customer_table
    def update_customer_info(self, customer_table):
        read_book = xlrd.open_workbook(self.filename)
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(1)
        row_count = read_book.sheet_by_index(1).nrows
        for row in range(0, max(row_count, customer_table.rowCount())):
            if row < customer_table.rowCount():
                w_sheet.write(row + 1, 0, customer_table.item(row, 0).text())
                w_sheet.write(row + 1, 1, customer_table.item(row, 1).text())
                w_sheet.write(row + 1, 2, customer_table.item(row, 2).text())
                w_sheet.write(row + 1, 3, customer_table.item(row, 3).text())
                w_sheet.write(row + 1, 4, customer_table.item(row, 4).text())
                w_sheet.write(row + 1, 5, customer_table.item(row, 5).text())
                w_sheet.write(row + 1, 6, int(float(customer_table.item(row, 6).text())))
                w_sheet.write(row + 1, 7, float(customer_table.item(row, 7).text()))
            else:
                for column in range(0, 8):
                    w_sheet.write(row + 1, column, "")
        write_book.save(self.filename.replace('xlsx', 'xls'))

    # Re-write order database with values in customer_table
    def update_order_info(self, order_table):
        read_book = xlrd.open_workbook(self.filename)
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(2)
        row_count = read_book.sheet_by_index(2).nrows
        for row in range(0, max(row_count, order_table.rowCount())):
            if row < order_table.rowCount():
                w_sheet.write(row + 1, 0, int(order_table.item(row, 0).text()))
                w_sheet.write(row + 1, 1, order_table.item(row, 1).text())
                w_sheet.write(row + 1, 2, order_table.item(row, 2).text())
                w_sheet.write(row + 1, 3, order_table.item(row, 3).text())
                w_sheet.write(row + 1, 4, float(order_table.item(row, 4).text()))
            else:
                for column in range(0, 5):
                    w_sheet.write(row + 1, column, "")
        write_book.save(self.filename.replace('xlsx', 'xls'))

    # Re-write menu database with values in customer_table
    def update_menu_info(self, menu_table):
        read_book = xlrd.open_workbook(self.filename)
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(0)
        row_count = read_book.sheet_by_index(0).nrows
        for row in range(0, max(row_count, menu_table.rowCount())):
            if row < menu_table.rowCount():
                w_sheet.write(row + 1, 0, menu_table.item(row, 0).text())
                w_sheet.write(row + 1, 1, float(menu_table.item(row, 1).text()))
            else:
                for column in range(0, 2):
                    w_sheet.write(row + 1, column, "")
        write_book.save(self.filename.replace('xlsx', 'xls'))

    # =======================================================
    # STATISTICS SECTION
    # =======================================================

    # Get name of customer with most money spent. Private
    def _get_best_customer(self):
        max_money = 0
        best_customer_row = 0
        read_sheet = xlrd.open_workbook(self.filename).sheet_by_index(1)
        for row in range(1, read_sheet.nrows):
            money_spent = read_sheet.cell_value(row, MONEY_COL)
            if money_spent > max_money:
                max_money = money_spent
                best_customer_row = row
        return str(read_sheet.cell_value(best_customer_row, 0)) + " " + str(read_sheet.cell_value(best_customer_row, 1))

    # Get number of orders made today. Private
    def _get_orders_made_today(self):
        read_sheet = xlrd.open_workbook(self.filename).sheet_by_index(2)
        orders = 0
        todays_date = "%02d / %02d / %04d" % (
            int(datetime.datetime.now().day), int(datetime.datetime.now().month), int(datetime.datetime.now().year))
        for row in range(1, read_sheet.nrows):
            order_date = read_sheet.cell_value(row, DATE_COL)
            if order_date == todays_date:
                orders += 1
        return str(orders)

    # Get number of orders in last week. Private
    def _get_orders_made_this_week(self):
        read_sheet = xlrd.open_workbook(self.filename).sheet_by_index(2)
        orders = 0
        todays_date = datetime.date.today()
        start_week = todays_date - datetime.timedelta(todays_date.weekday())
        end_week = start_week + datetime.timedelta(7)
        for row in range(1, read_sheet.nrows):
            day, month, year = map(int, read_sheet.cell_value(row, DATE_COL).split("/"))
            order_date = datetime.date(year, month, day)
            if start_week <= order_date <= end_week:
                orders += 1
        return str(orders)

    # Get amount made today. Private
    def _get_amount_made_today(self):
        read_sheet = xlrd.open_workbook(self.filename).sheet_by_index(2)
        amount_made = 0
        todays_date = datetime.datetime.now().date()
        for row in range(1, read_sheet.nrows):
            day, month, year = map(int, read_sheet.cell_value(row, DATE_COL).split("/"))
            order_date = datetime.date(year, month, day)
            if order_date == todays_date:
                order_total = read_sheet.cell_value(row, TOTAL_COL)
                amount_made += order_total
        return str(amount_made)

    # Get amount made in past week. Private
    def _get_amount_made_this_week(self):
        read_sheet = xlrd.open_workbook(self.filename).sheet_by_index(2)
        amount_made = 0
        todays_date = datetime.datetime.now().date()
        start_week = todays_date - datetime.timedelta(todays_date.weekday())
        end_week = start_week + datetime.timedelta(7)
        for row in range(1, read_sheet.nrows):
            day, month, year = map(int, read_sheet.cell_value(row, DATE_COL).split("/"))
            order_date = datetime.date(year, month, day)
            if start_week <= order_date <= end_week:
                order_total = read_sheet.cell_value(row, TOTAL_COL)
                amount_made += order_total
        return str(amount_made)

    # Return list of tuples containing name of statistic + statistic value
    def get_all_statistics(self):
        statistics = [("Best Customer", self._get_best_customer()),
                      ("Orders Made Today", self._get_orders_made_today()),
                      ("Orders Made This Week", self._get_orders_made_this_week()),
                      ("Amount Made Today", self._get_amount_made_today()),
                      ("Amount Made This Week", self._get_amount_made_this_week())]
        return statistics
