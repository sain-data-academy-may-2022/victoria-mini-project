### imports
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products
from file_handlers.json_handler import load_orders, write_orders
from modules.main_menu import main_menu

# load files
products = load_products()
couriers = load_couriers()
orders = load_orders()

# main program file
products, couriers, orders = main_menu(products, couriers, orders)

# save files and exit
# write_products(products)
# write_couriers(couriers)
# write_orders(orders)
print('\nClosing program, goodbye!\n')


## DEV AREA





def add_order(order_list, courier_list):
    order_count = int(max(order_list.keys())) + 1
    new_order = {}
    new_order['customer_name'] = input('fds') ## FORMAT TEXT 
    new_order['customer_address'] = input('\nPlease enter the customer\'s address:\n> ') ## FORMAT TEXT 
    new_order['customer_phone'] = input('\nPlease enter the customer\'s phone number:\n> ') ## FORMAT TEXT
    new_order['courier'] = input('enter courier id:')
    new_order['status'] = 0

    order_list[str(order_count)] = new_order

