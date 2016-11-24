from bst import BinarySearchTree
import xlrd
import unicodedata


class Menu:
    def __init__(self, filename):
        self.menu_dictionary = self._read_menu(filename)
        self.menu_bst = self._get_menu_bst()
        self.toppings_bst = self._get_toppings_bst()

    def _read_menu(path):
        menu = xlrd.open_workbook(path).sheet_by_index(0)
        info = {}
        for value in range(1, menu.nrows):
            number, name, price = menu.row_values(value)
            name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
            info[value] = (name, price)
        return info

    def _get_menu_bst(self):
        menu_bst = BinarySearchTree()
        for  in info:
            for item, price in list:
                menu_bst.put(item, price)
        return menu_bst

    def _get_toppings_bst(self):
        toppings_bst = BinarySearchTree()
        for pizza, toppings in PIZZA_MENU:
            toppings_bst.put(pizza, toppings)
        return toppings_bst

    def get_menu(self):
        return self.menu_bst

    def get_toppings_menu(self):
        return self.toppings_bst

    def get_price(self, item_no):
        name, price = self.menu_bst.get(item_no)
        return price

    def get_toppings(self, pizza_no):
        return self.toppings_bst.get(pizza_no)