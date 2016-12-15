import unicodedata
import xlrd
from util.bst import BinarySearchTree


class Menu:
    def __init__(self, filename):
        self.menu_bst = self._get_menu_bst(filename)

    def _get_menu_bst(self, filename):
        menu_bst = BinarySearchTree()
        menu = xlrd.open_workbook(filename).sheet_by_index(0)
        for item in range(1, menu.nrows):
            name, price = menu.row_values(item)
            name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
            menu_bst.put(name, price)
        return menu_bst

    def print_menu(self):
        for name, price in self.menu_bst.entry_set():
            print name, price

    def get_menu_price(self, name):
        return self.menu_bst.get(name)
