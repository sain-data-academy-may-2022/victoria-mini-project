'''Module with functions to manage the courier list'''


### imports
import modules.clear_screen as cs
import modules.funcs_couriers as cour


### menu functions
# print the courier management menu options
def print_courier_options():
    '''Prints the courier management menu options'''

    cs.clear_screen()

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
        cour.print_courier_list(couriers)

    # create new courier
    elif choice == '2':
        couriers = cour.try_add_courier(couriers, connection)

    # update existing courier
    elif choice == '3':
        couriers = cour.try_update_courier(couriers, connection)

    # delete existing courier
    elif choice == '4':
        couriers = cour.try_delete_courier(couriers, connection)

    # clear screen and reprint courier menu options
    elif choice == '':
        print_courier_options()

    # handle incorrect input
    else: 
        print('\nInvalid selection. Please select a valid menu option.')

    return running, couriers


# controls courier menu loop
def courier_menu(couriers: list, connection):

    print_courier_options()

    running = True
    
    while running:
        
        running, couriers = courier_menu_choice(couriers, connection)

    return couriers
