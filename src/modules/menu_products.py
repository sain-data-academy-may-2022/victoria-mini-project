'''Module with functions to manage the products list'''


### imports
import modules.clear_screen as cs
import modules.funcs_print as f_p
import modules.funcs_input as f_i
# import modules.funcs_utilities as f_u
# import modules.utilities as util


### menu functions
# print the product management menu options
def print_product_options():
    '''Prints the product management options'''

    print('''\nProduct Management
    
    [1] - Display Product List
    [2] - Add a New Product
    [3] - Update Existing Product
    [4] - Delete a Product
    
    [0] - Back to Main Menu\n''')


# controls product menu input and selection
def product_menu_choice(products: list, connection):

    choice = input('\nPlease select an option:\n> ')
    running = True

    # exit product menu loop
    if choice == '0':
        running = False
        return running, products

    # print product menu list
    elif choice == '1':
        print_product_list(products)

    # create new product
    elif choice == '2':         ### TEST
        products = add_product(products, connection)

    # update existing product
    elif choice == '3':         #### TEST
        print('3')

    # delete existing product
    elif choice == '4':         #### TEST
        print('4')

    # clear screen and reprint product menu options
    elif choice == '':
        cs.clear_screen()
        print_product_options()

    # handle incorrect input
    else: 
        print('\nInvalid selection. Please select a valid menu option.')

    return running, products


# controls product menu loop
def product_menu(products: list, connection):

    cs.clear_screen()
    print_product_options()

    running = True
    
    while running:
        
        running, products = product_menu_choice(products, connection)

    return products


### program functions

# print the product list (only available products)
def print_product_list(products: list):
    available_drinks = [item for item in products if item['active'] == 1 and item['category'] == 'Drinks']
    f_p.print_plain_list('available drinks', available_drinks)

    available_snacks = [item for item in products if item['active'] == 1 and item['category'] == 'Snacks']
    f_p.print_plain_list('available snacks', available_snacks)

    available_base = [item for item in products if item['active'] == 1 and item['category'] == 'Base']
    f_p.print_plain_list('available bases', available_base)

    available_tops = [item for item in products if item['active'] == 1 and item['category'] == 'Toppings']
    f_p.print_plain_list('available toppings', available_tops)


# print the product list (only available products)
def print_indexed_product_list(products: list):             #### NEEDS TESTING
    available_drinks = [item for item in products if item['active'] == 1 and item['category'] == 'Drinks']
    f_p.print_indexed_list('available drinks', available_drinks)

    available_snacks = [item for item in products if item['active'] == 1 and item['category'] == 'Snacks']
    f_p.print_indexed_list('available snacks', available_snacks)

    available_base = [item for item in products if item['active'] == 1 and item['category'] == 'Base']
    f_p.print_indexed_list('available bases', available_base)

    available_tops = [item for item in products if item['active'] == 1 and item['category'] == 'Toppings']
    f_p.print_indexed_list('available toppings', available_tops)


# add a product to the products list
def add_product(products: list, connection):

    name = f_i.get_string_input('Enter name of new product')

    

    # products = f_u.add_thing(products, 'product', ['category', 'price', 'current_inventory', 'active'], connection)

    
    return products

