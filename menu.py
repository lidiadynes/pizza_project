from bst import BinarySearchTree()

PIZZA_MENU = {'1': ['tomato', 'garlic', 'oregano'], '2': ['tomato', 'mozzarella', 'basil'], '3': ['broccoli', 'mozzarella', 'sausage'],
              '4': ['ham', 'mozzarella', 'ricotta', 'mushrooms'], '5': ['tomato', 'oregano', 'garlic', 'capers', 'olives', 'anchovies', 'mozarella'],
              '6': ['tomato', 'chorizo', 'mozarella']}

PIZZA_PRICES = {'1': 4.50, '2': 5.90, '3': 6.85, '4': 6.85, '5': 6.70, '6': 6.95}

TOPPING_PRICES = {'7': ('olives', 1.25), 'mozarella': 0.90, 'ham': 1.50, 'chorizo': 1.75, 'capers': 0.90}

DRINKS_PRICES = {'ten_bianco750': 14.95, 'ten_bianco175': 3.90, 'ten_rosso750': 14.95, 'ten_rosso175': 3.90,
                 'car_bianco750': 15.95, 'car_bianco175': 4.15, 'car_rosso750': 15.95, 'car_rosso175': 4.15,
                 'fra_bianco750': 17.95, 'fra_bianco175': 4.50, 'fra_rosso750': 17.95, 'fra_rosso175': 4.50, 'fra_rose750': 17.95, 'fra_rose175': 4.50,
                 'bub_bianco750': 19.50, 'bub_bianco175': 5.00, 'bub_lambrusco750': 19.50, 'bub_lambrusco175': 5.00,
                 'lemonade': 2.20, 'orange_juice': 2.55, 'apple_juice': 2.55, 'sparkling_water': 2.00, 'beans': 1.60}

SALAD_PRICES = {'mixed_salad': 2.45, 'franco_salad': 3.55}

MENU_ITEMS = [PIZZA_PRICES, TOPPING_PRICES, DRINKS_PRICES, SALAD_PRICES]

class Menu:
    def __init__(self):
        self.menu_bst = self._get_menu_bst()
        self.toppings_bst = self._get_toppings_bst()

    def _get_menu_bst(self):
        menu_bst = BinarySearchTree()
        for list in MENU_ITEMS:
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