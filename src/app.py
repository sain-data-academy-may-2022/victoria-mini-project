'''Main program file'''

### imports
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products
from file_handlers.json_handler import load_orders, write_orders
from db.db import db_query, get_connection, close_connection
from modules.menu_main import main_menu

### load database connection
connection = get_connection()

### load files


### main program file


### save files amd exit

close_connection(connection)

print('\nClosing program, goodbye!\n')