### imports
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products, \
                                            load_orders, write_orders
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
