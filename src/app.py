'''Main program file'''

### imports
from db.db import db_command, db_query, get_connection, close_connection
from modules.funcs_file_handlers import get_products, get_couriers
from file_handlers.csv_handler import write_products, write_couriers, write_orders
from modules.menu_main import main_menu

### load database connection
connection = get_connection()

### load files
products = get_products()
couriers = get_couriers()
orders = db_query('SELECT * FROM orders', connection)

### main program file
products, couriers, orders = main_menu(products, couriers, orders, connection)    #### add returns for products/couriers???


### DEV







### save files amd exit
write_products(products)
write_couriers(couriers)
close_connection(connection)

print('\nClosing program, goodbye!\n')