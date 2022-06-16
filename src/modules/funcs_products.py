'''Module with functions to manage the products list'''


### imports
import modules.funcs_utilities as util
from db.db import db_command, db_query

### program functions

# print the product list (only available products)
def print_product_list(products: list, 
                        allow_oos: bool = True,
                        allow_inactive: bool = False):
                        
    available_drinks = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Drinks']
    util.print_plain_list('currently available drinks', available_drinks)

    available_snacks = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Snacks']
    util.print_plain_list('currently available snacks', available_snacks)

    available_base = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Base']
    util.print_plain_list('currently available bases', available_base)

    available_tops = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Toppings']
    util.print_plain_list('currently available toppings', available_tops)

    if allow_oos:
        out_of_stock = [item for item in products if item['active'] == 1 and item['stock'] == 0]
        util.print_plain_list('items currently out of stock', out_of_stock)

    if allow_inactive:
        inactive = [item for item in products if item['active'] == 0]
        util.print_plain_list('inactive menu items', inactive)


# print the product list (only available products)
def print_indexed_product_list(products: list, 
                                allow_oos: bool = True, 
                                allow_inactive: bool = False,
                                return_sorted_list: bool = False):             #### NEEDS TESTING
    index = 1

    available_drinks = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Drinks']
    util.print_indexed_list('currently available drinks', available_drinks, index)

    index += len(available_drinks)
    available_snacks = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Snacks']
    util.print_indexed_list('currently available snacks', available_snacks, index)

    index += len(available_snacks)
    available_base = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Base']
    util.print_indexed_list('currently available bases', available_base, index)

    index += len(available_base)
    available_tops = [item for item in products if item['active'] == 1 and item['stock'] > 0 and item['category'] == 'Toppings']
    util.print_indexed_list('currently available toppings', available_tops, index)

    if allow_oos:
        index += len(available_tops)
        out_of_stock = [item for item in products if item['active'] == 1 and item['stock'] == 0]
        util.print_indexed_list('items currently out of stock', out_of_stock, index)

    if allow_inactive:
        if allow_oos:
            index += len(out_of_stock)
        else:
            index += len(available_tops)
        inactive = [item for item in products if item['active'] == 0]
        util.print_indexed_list('inactive menu items', inactive, index)

    if return_sorted_list:
        return available_drinks + available_snacks + available_base + available_tops + out_of_stock + inactive


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# sends query to and retrieves updated product list from product database
def update_products_db(sql_query: str, connection):

    db_command(sql_query, connection)

    products = db_query('''SELECT * FROM products
                            ORDER BY CASE
                            WHEN category = "Drinks" THEN 1
                            WHEN category = "Snacks" THEN 2
                            WHEN category = "Base" THEN 3
                            ELSE 4 END''', connection)
    return products


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# gets an index within a sorted product list and returns the dict at that index
def get_index_within_product_list(products: list, interaction_string: str):

    sorted_list = print_indexed_product_list(products, allow_oos = True, allow_inactive = True, return_sorted_list = True)
    
    _index = util.get_index_within_list(f'\nEnter the ID of the product to be {interaction_string}d or press ENTER to cancel', sorted_list, True)

    if _index == '':
        return ''

    else:
        return sorted_list[_index]


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
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

            _index = util.get_dict_index('name', name, products)

            products = update_product(products[_index], products, connection)

    return products


# adds a new product to the product list and db
def add_new_product(name: str, connection):
    '''Gets remaining parameters for new product and inserts them into the database'''

    sql_query = get_new_product_data(name)

    return update_products_db(sql_query, connection)


# gets remainder of product data, returns a formatted sql query
def get_new_product_data(name: str):

    category = util.get_input_within_list('\nAvailable categories: Drinks, Snacks, Base, or Toppings.\n\
                                        \nEnter category for this product', \
                                        ['Drinks', 'Snacks', 'Base', 'Toppings'])

    price = util.get_positive_float_input('\nEnter price for this product')

    stock = util.get_int_input('\nEnter initial stock amount', allow_zero = True)

    return f"INSERT INTO `products`(`name`, `category`, `price`, `stock`) VALUES ('{name}', '{category}', {price}, {stock}); "


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# update an existing product
def try_update_product(products: list, connection):

    prod_dict = get_index_within_product_list(products, "update")

    if prod_dict == '':
        pass

    else:
        products = update_product(prod_dict, products, connection)

    return products


# gets updated values for a product within the 
def update_product(prod: dict, products: list, connection):

    prod = get_updated_product_values(prod)

    sql_query = f'''UPDATE `products` SET 
                `name` = "{prod["name"]}",
                `category` = "{prod["category"]}",
                `price` = {prod["price"]},
                `stock` = {prod["stock"]},
                `active` = {prod["active"]}

                WHERE
                `product_id` = {prod["product_id"]};'''

    products = update_products_db(sql_query, connection)

    print('\nProduct updated successfully.')
    
    return products


#
def get_updated_product_values(prod):

    for key, value in prod.items():
        question = f'\nThe current {key} is {value}. Enter new {key} or press ENTER to skip'

        if key == 'product_id':
            pass

        elif key == 'name' or key == 'phone':
            prod[key] = util.get_updated_value(value, util.get_string_input(question, allow_blank = True))

        elif key == 'category': 
            prod[key] = util.get_updated_value(value, util.get_input_within_list(question, ['Drinks', 'Snacks', 'Base', 'Toppings'], allow_blank = True))

        elif key == 'price':
            prod[key] = util.get_updated_value(value, util.get_positive_float_input(question, True))

        elif key == 'stock':
            prod[key] = util.get_updated_value(value, util.get_int_input(question, allow_blank = True, allow_zero = True))

        elif key == 'active':        
            question = f'\n{"Currently listed in active menu." if value == 1 else "Not listed in active menu."} Enter (yes/no) to list this item in menu or press ENTER to skip.'

            prod[key] = util.get_updated_value(value, util.get_bool_int_input(question, allow_blank = True))

            if prod[key] == 0 and prod['stock'] > 0:
                print(f'\n{prod["name"]} has been set as inactive, however still has {prod["stock"]} in stock.')

                question = f'\nSet {prod["name"]} stock to 0? (yes/no)'

                if util.get_bool_int_input(question, return_bool = True):
                    prod['stock'] = 0

    return prod


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
def try_delete_product(products: list, connection):

    prod_dict = get_index_within_product_list(products, "delete")

    if prod_dict == '':
        pass

    else:
        products = delete_product(prod_dict, products, connection)

    return products

#
def delete_product(prod: dict, products: list, connection):

    sql_query = f'''DELETE FROM products WHERE `product_id` = {prod["product_id"]}'''

    confirm = util.get_bool_int_input(f'\nYou are about to delete {prod["name"]}. Enter (yes/no) to confirm', return_bool = True)

    if confirm:

        products = update_products_db(sql_query, connection)
        print(f'\n{prod["name"]} has been deleted.')

    return products

