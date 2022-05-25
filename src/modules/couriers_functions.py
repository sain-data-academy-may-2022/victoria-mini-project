'''Module with functions to manage the courier list'''


import utilities as utilities
from clear_screen import clear_screen


# print the courier management menu options
def print_courier_options():
    '''Prints the courier management menu options'''

    clear_screen()
    print('''Courier Management
    
    [1] - Display Courier List
    [2] - Add a New Courier
    [3] - Update Existing Courier
    [4] - Delete a Courier
    
    [0] - Back to Main Menu''')


# courier option management function
def courier_management(courier_list):
    '''Maintains the loop for the courier management menu'''

    running = True
    print_courier_options()
    print('\n\n')

    while running:

        running = courier_menu_input_check(courier_list)

    return courier_list


# courier option selection
def courier_menu_input_check(courier_list):
    '''Manages the input of menu options'''

    option = input('Please select an option:\n> ')

    # leave courier management
    if option == '0':
        return False

    # display courier list
    elif option == '1':
        print_courier_options()
        print('\n[1] - Display Courier List\n')

        # print_courier_list(courier_list)

    # add a new courier
    elif option == '2':
        print_courier_options()
        print('\n[2] - Add a New courier\n')

        # add_courier_loop(courier_list)

    # update existing courier
    elif option == '3':
        print_courier_options()
        print('\n[3] - Update Existing courier\n')
        print_courier_indexed(courier_list)

        # update_courier(courier_list)

    # delete a courier
    elif option == '4':
        print_courier_options()
        print('\n[4] - Delete a courier\n')
        print_courier_indexed(courier_list)

        # remove_courier_loop(courier_list)

    # handles invalid input
    else:
        print_courier_options()
        print('\nInvalid input.\n')

    return True

# add a courier to a list
def add_courier(courier_list):
    '''adds a courier to a courier list'''
    return courier_list


# remove a courier from a list
def remove_courier(courier_list):
    '''removes a courier to a courier list'''
    return courier_list


# print a courier list
def print_courier_list(courier_list):
    '''Prints the courier list'''
    if utilities.check_list_has_items(courier_list):
        print('\nCurrent couriers:')
        print(utilities.format_list(courier_list))
    else:
        print('There are no couriers currently listed.')


# print a courier list with indexes
def print_courier_indexed(courier_list):
    '''Prints the courier list with indexes'''
    if utilities.check_list_has_items(courier_list):
        print(utilities.format_list_indexed(courier_list))
    else:
        print('There are no couriers currently listed.')



# TESTS
couriers = ['Bob', 'Janice', 'Amir']

print_courier_list(couriers)

print_courier_indexed(couriers)
