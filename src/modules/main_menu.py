'''Module with functions to manage the main menu'''

import products_functions as pf
import couriers_functions as cf
import orders_functions as of

# print the main menu options
def print_main_menu():
    '''Prints the main menu options'''
    print('''\nWelcome to Bready or Not Breakfast Bar

    [1] - Product Management
    [2] - Courier Management
    [3] - Order Management
    More options coming soon...

    [0] - Exit Application''')

# product option management function
def main_menu(product_list, courier_list, order_list):
    '''Maintains the loop for the product management menu'''

    running = True
    print_main_menu()
    print('\n\n')

    while running:

        running = main_menu_input_check(product_list, courier_list, order_list)

    return product_list, courier_list, order_list

# main menu option selection
def main_menu_input_check(product_list, courier_list, order_list):
    '''Manages the input of menu options'''

    option = input('Please select an option:\n> ')

    # close program
    if option == '0':
        return False

    # enter product management menu
    elif option == '1':
        pf.product_management(product_list)

    # enter courier management menu
    elif option == '2':
        cf.courier_management(courier_list)

    # enter order management menu
    elif option == '3':
        pass

    # handles invalid input
    else:
        print_main_menu()
        print('\nInvalid input.\n')
