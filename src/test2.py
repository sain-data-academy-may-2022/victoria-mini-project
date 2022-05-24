### imports

from modules.clear_screen import clear_screen
from file_handlers.csv import load_products, write_products
from file_handlers.json import load_orders, write_orders
from modules.product_management import prl

import sys


# Program Loop
products = load_products()
orders = load_orders()
order_count = int(max(orders.keys())) + 1

print(sys.path)

while True:
    user_input = input('> ')

    if user_input == '0':
        break

    elif user_input == '1':
        prl()

    elif user_input == '2':
        pass