'''Module with functions to manage the products list menu'''


### imports
import modules.clear_screen as cs
import modules.funcs_products as prod


### menu functions
# print the product management menu options
def print_product_options():
    '''Prints the product management options'''

    cs.clear_screen()

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
        prod.print_product_list(products)

    # create new product
    elif choice == '2':         ### TEST
        products = prod.try_add_product(products, connection)

    # update existing product
    elif choice == '3':         #### TEST
        products = prod.try_update_product(products, connection)

    # delete existing product
    elif choice == '4':         #### TEST
        products = prod.try_delete_product(products, connection)

    # clear screen and reprint product menu options
    elif choice == '':
        print_product_options()

    # handle incorrect input
    else: 
        print('\nInvalid selection. Please select a valid menu option.')

    return running, products


# controls product menu loop
def product_menu(products: list, connection):

    print_product_options()

    running = True
    
    while running:
        
        running, products = product_menu_choice(products, connection)

    return products
