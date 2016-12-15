import xlrd
from xlutils.copy import copy
from customer import Customer
import datetime

PHONE_COL = 3
MONEY_COL = 7
DATE_COL = 1
TOTAL_COL = 4


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.order_number = xlrd.open_workbook(self.filename).sheet_by_index(2).nrows

    def does_customer_exist(self, phone):
        w_sheet = xlrd.open_workbook(self.filename).sheet_by_index(1)
        for row in range(1, w_sheet.nrows):
            number = w_sheet.cell_value(row, PHONE_COL)
            if number == phone:
                return True
        return False

    def find_customer_row(self, phone):
        read_book = xlrd.open_workbook(self.filename)
        w_sheet = read_book.sheet_by_index(1)
        for row in range(1, w_sheet.nrows):
            number = w_sheet.cell_value(row, PHONE_COL)
            if number == phone:
                return row

    def get_customer(self, phone):
        read_book = xlrd.open_workbook(self.filename)
        w_sheet = read_book.sheet_by_index(1)
        row = self.find_customer_row(phone)
        first_name, last_name, postcode, phone, email, order_numbers, total_orders, money_spent = w_sheet.row_values(row)
        if not order_numbers:
            order_numbers = []
        else:
            order_numbers = map(int, order_numbers.split(","))
        return Customer(first_name, last_name, postcode, phone, email, order_numbers, int(total_orders), float(money_spent))

    def add_customer(self, customer, order):
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

    def update_customer_info(self, customer_table):
        read_book = xlrd.open_workbook(self.filename)
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(1)
        row_count = read_book.sheet_by_index(1).nrows
        for row in range(0, row_count):
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

    def update_order_info(self, order_table):
        read_book = xlrd.open_workbook(self.filename)
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(2)
        row_count = read_book.sheet_by_index(2).nrows
        for row in range(0, row_count):
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

    def update_menu_info(self, menu_table):
        read_book = xlrd.open_workbook(self.filename)
        write_book = copy(read_book)
        w_sheet = write_book.get_sheet(0)
        row_count = read_book.sheet_by_index(1).nrows
        for row in range(0, row_count):
            if row < menu_table.rowCount():
                w_sheet.write(row + 1, 0, menu_table.item(row, 0).text())
                w_sheet.write(row + 1, 1, float(menu_table.item(row, 1).text()))
            else:
                for column in range(0, 2):
                    w_sheet.write(row + 1, column, "")
        write_book.save(self.filename.replace('xlsx', 'xls'))

    def get_best_customer(self):
        max_money = 0
        best_customer_row = 0
        read_sheet = xlrd.open_workbook(self.filename).sheet_by_index(1)
        for row in range(1, read_sheet.nrows):
            money_spent = read_sheet.cell_value(row, MONEY_COL)
            if money_spent > max_money:
                max_money = money_spent
                best_customer_row = row
        return str(read_sheet.cell_value(best_customer_row, 0)) + " " + str(read_sheet.cell_value(best_customer_row, 1))

    def get_orders_made_today(self):
        read_sheet = xlrd.open_workbook(self.filename).sheet_by_index(2)
        orders = 0
        todays_date = "%02d / %02d / %04d" % (
            int(datetime.datetime.now().day), int(datetime.datetime.now().month), int(datetime.datetime.now().year))
        for row in range(1, read_sheet.nrows):
            order_date = read_sheet.cell_value(row, DATE_COL)
            if order_date == todays_date:
                orders += 1
        return str(orders)

    def get_orders_made_this_week(self):
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

    def get_amount_made_today(self):
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

    def get_amount_made_this_week(self):
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

    def get_all_statistics(self):
        statistics = []
        statistics.append(("Best Customer", self.get_best_customer()))
        statistics.append(("Orders Made Today", self.get_orders_made_today()))
        statistics.append(("Orders Made This Week", self.get_orders_made_this_week()))
        statistics.append(("Amount Made Today", self.get_amount_made_today()))
        statistics.append(("Amount Made This Week", self.get_amount_made_this_week()))
        return statistics