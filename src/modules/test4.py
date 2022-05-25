import csv_handler as csv_handler
import json_handler as json_handler
from main_menu import main_menu

# program files
products = csv_handler.load_products()
couriers = csv_handler.load_couriers()
orders = json_handler.load_orders()
order_count = max(orders.keys())


main_menu(products, couriers, orders)
