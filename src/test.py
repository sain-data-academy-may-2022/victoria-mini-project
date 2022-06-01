### imports
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products, \
                                            load_orders, write_orders
from file_handlers.json_handler import load_orders, write_orders
# from modules.main_menu import main_menu
from modules.utilities import get_string_input


# load files
products = load_products()
# couriers = load_couriers()
# orders = load_orders()

# print(products)
# print(couriers)
# print(orders)

# a_string = ''
# for each in orders:
#     print(f'Order Number: {each}')
#     for line in orders[each]:
#         print(f'{line.capitalize():>12}: {orders[each][line]}')
