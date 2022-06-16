'''Module with functions to manage the products list'''


### imports
import modules.funcs_utilities as util
from db.db import db_command, db_query

### program functions

# print the product list (only available products)
def print_product_list(products: list):
    available_drinks = [item for item in products if item['active'] == 1 and item['category'] == 'Drinks']
    util.print_plain_list('available drinks', available_drinks)

    available_snacks = [item for item in products if item['active'] == 1 and item['category'] == 'Snacks']
    util.print_plain_list('available snacks', available_snacks)

    available_base = [item for item in products if item['active'] == 1 and item['category'] == 'Base']
    util.print_plain_list('available bases', available_base)

    available_tops = [item for item in products if item['active'] == 1 and item['category'] == 'Toppings']
    util.print_plain_list('available toppings', available_tops)


# print the product list (only available products)
def print_indexed_product_list(products: list):             #### NEEDS TESTING
    index = 1

    available_drinks = [item for item in products if item['active'] == 1 and item['category'] == 'Drinks']
    util.print_indexed_list('available drinks', available_drinks, index)

    index += len(available_drinks)
    available_snacks = [item for item in products if item['active'] == 1 and item['category'] == 'Snacks']
    util.print_indexed_list('available snacks', available_snacks, index)

    index += len(available_snacks)
    available_base = [item for item in products if item['active'] == 1 and item['category'] == 'Base']
    util.print_indexed_list('available bases', available_base, index)

    index += len(available_base)
    available_tops = [item for item in products if item['active'] == 1 and item['category'] == 'Toppings']
    util.print_indexed_list('available toppings', available_tops, index)


# gets name for a new product, either adds new product, updates it, or returns product list
def try_add_product(products: list, connection):
    '''Function which gets a product name. If the name is blank, returns original product list.
    If name already exists, gives option to update list. If name does not exist, adds product'''
    
    name = util.get_string_input('\nEnter name of new product or press ENTER to cancel', True)

    if name == '':
        pass

    elif not util.is_value_in_dict('name', name, products):

        products = add_new_product(name, connection)

    else:
        print(f'\n{name} already exists in the product menu.')
        
        choice = input('Do you want to update this item? Press ENTER to update or any other key to cancel.\n> ')

        if choice == '':
            products = update_product()

    return products


# adds a new product to the product list and db
def add_new_product(name: str, connection):
    '''Gets remaining parameters for new product and inserts them into the database'''

    category = util.get_input_within_list('\nAvailable categories: Drinks, Snacks, Base, or Toppings.\n\
                                        \nEnter category for this product', \
                                        ['Drinks', 'Snacks', 'Base', 'Toppings'])

    price = util.get_positive_float_input('\nEnter price for this product')

    stock = util.get_int_input('\nEnter initial stock amount', allow_zero = True)

    sql_query = f"INSERT INTO `products` (`name`, `category`, `price`, `stock`) VALUES ('{name}', '{category}', {price}, {stock})"

    db_command(sql_query, connection)

    products = db_query('''SELECT * FROM products
                            ORDER BY CASE
                            WHEN category = "Drinks" THEN 1
                            WHEN category = "Snacks" THEN 2
                            WHEN category = "Base" THEN 3
                            ELSE 4 END''', connection)

    return products


# update an existing product
def try_update_product(products: list, connection):
    print_indexed_product_list(products)
    pass



def try_delete_product(products: list, connection):
    pass