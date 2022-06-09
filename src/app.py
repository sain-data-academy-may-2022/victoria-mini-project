### imports
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products
from file_handlers.json_handler import load_orders, write_orders
from db.db import db_query, get_connection, close_connection
from modules.main_menu import main_menu

# load database connection
connection = get_connection()

# load files
# products = load_products()
products = db_query('SELECT * FROM products', connection)
# couriers = load_couriers()
couriers = db_query('SELECT * FROM couriers', connection)
customers = db_query('SELECT * FROM customers', connection)
orders = load_orders()
# orders = db_query('SELECT * FROM orders', connection)

# main program file
products, couriers, orders = main_menu(products, couriers, orders)

# save files and exit
close_connection(connection)
# write_products(products)
# write_couriers(couriers)
# write_orders(orders)
print('\nClosing program, goodbye!\n')


## DEV AREA
