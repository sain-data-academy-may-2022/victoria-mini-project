'''Module with functions to manage the main menu'''


import modules.product_functions as pf
import modules.courier_functions as cf
import modules.order_functions as of


# print the main menu options
def print_main_menu():
    '''Prints the main menu options'''

    print('''\nWelcome to "Bready or Not" Breakfast Bar

    [1] - Product Management
    [2] - Courier Management
    [3] - Order Management
    More options coming soon...

    [0] - Exit Application''')


# main menu function
def main_menu(product_list, courier_list, order_list):
    '''Maintains the loop for the main menu'''

    running = True

    while running:

        print_main_menu()

        choice = input('\nPlease select an option:\n> ')

        if choice == '0':
            print('\nClosing program, goodbye!\n')
            running = False
            return product_list, courier_list, order_list

        elif choice == '1':
            pf.product_management(product_list)

        elif choice == '2':
            cf.courier_management(courier_list)

        elif choice == '3':
            of.order_management(order_list)

        else:
            print('Invalid selection.')
