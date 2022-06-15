'''Main program file'''

### imports
from db.db import db_query, get_connection, close_connection
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
# orders = main_menu(products, couriers, orders, connection)


### DEV

from modules import funcs_input as f_i
from modules import funcs_bool as f_b
from modules import funcs_print as f_p

f_p.print_plain_list('products', products)


def add_product(products: list, connection):

    name = f_i.get_string_input('\nEnter name of new product or press ENTER to cancel', True)

    if name == '':
        return products

    elif not f_b.is_value_in_dict('name', name, products):

        category = f_i.get_input_within_list('\nAvailable categories: Drinks, Snacks, Base, or Toppings.\
                                            \nEnter category for this product ', \
                                            ['Drinks', 'Snacks', 'Base', 'Toppings'])

        price = f_i.get_positive_float_input('\nEnter price for this product')

    else:
        print('item is in list')

    

    # products = f_u.add_thing(products, 'product', ['category', 'price', 'current_inventory', 'active'], connection)

    
    return products




add_product(products, connection)








### save files amd exit
# write_products(products)
# write_couriers(couriers)
close_connection(connection)

print('\nClosing program, goodbye!\n')