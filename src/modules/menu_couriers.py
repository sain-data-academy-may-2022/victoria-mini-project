'''Module with functions to manage the courier list'''


### imports
import modules.clear_screen as cs
import modules.funcs_print as f_p
import db.db as db
# import modules.utilities as util


### menu functions
# print the courier management menu options
def print_courier_options():
    '''Prints the courier management menu options'''

    print('''\nCourier Management
    
    [1] - Display Courier List
    [2] - Add a New Courier
    [3] - Update Existing Courier
    [4] - Delete a Courier
    
    [0] - Back to Main Menu\n''')


# controls courier menu input and selection
def courier_menu_choice(couriers: list, connection):

    choice = input('\nPlease select an option:\n> ')
    running = True

    # exit courier menu loop
    if choice == '0':
        running = False
        return running, couriers

    # print courier menu list
    elif choice == '1':
        print_courier_list(couriers)

    # 
    elif choice == '2':
        print('2')
        #

    # 
    elif choice == '3':
        print('3')
        #

    # clear screen and reprint courier menu options
    elif choice == '':
        cs.clear_screen()
        print_courier_options()

    # handle incorrect input
    else: 
        print('Invalid selection. Please select a valid menu option.')

    return running, couriers


# controls courier menu loop
def courier_menu(couriers: list, connection):

    cs.clear_screen()
    print_courier_options()

    running = True
    
    while running:
        
        running, couriers = courier_menu_choice(couriers, connection)

    return couriers


### functional functions (wut)
# print non-indexed courier list
def print_courier_list(couriers: list):
    f_p.print_plain_list('couriers', couriers)


# 