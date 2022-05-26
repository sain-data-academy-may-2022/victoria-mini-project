'''Module with functions to manage the courier list'''

import modules.clear_screen as cs
import modules.utilities as util

# print the courier management menu options
def print_courier_options():
    '''Prints the courier management menu options'''

    print('''\nCourier Management
    
    [1] - Display Courier List
    [2] - Add a New Courier
    [3] - Update Existing Courier
    [4] - Delete a Courier
    
    [0] - Back to Main Menu\n''')


# courier option management function
def courier_management(courier_list):
    '''Maintains the loop for the courier management menu'''

    running = True

    cs.clear_screen()
    print_courier_options()

    while running:
        choice = input('Please select an option:\n> ')

        if choice == '0':
            running = False
            return courier_list

        elif choice == '1':
            util.print_plain_list('couriers', courier_list)

        elif choice == '2':         # DONE
            add_couriers(courier_list)

        elif choice == '3':
            update_a_courier(courier_list)

        elif choice == '4':
            remove_couriers(courier_list)

        elif choice == 'r':
            cs.clear_screen()
            print_courier_options()

        else:
            print('Invalid selection.')


def add_couriers(courier_list):
    '''Loop which adds a courier to a courier list'''

    util.loop_add_items_to_list('courier', courier_list)


def update_a_courier(courier_list):
    print('\n' + util.format_list_indexed(courier_list))
    index = util.get_int_input('Enter the ID of the courier to be updated:') - 1

    if util.is_index_within_range(index, courier_list):
        new_courier = util.format_string(util.get_string_input('\nEnter the new name:'))

        print(f'{courier_list[index]} is now {new_courier}.\n')

        util.update_item_in_list(new_courier, index, courier_list)

    else:
        print('Invalid ID\n')



#     print('\n' + util.format_list_indexed(courier_list))
#     index = util.get_int_input('Enter the ID of the courier to be updated:') - 1

#     if util.is_index_within_range(index, courier_list):
#         new_courier = util.get_string_input('Enter the new name:')

#         util.update_item_in_list(new_courier, index, courier_list)
#     else:
#         print('Invalid ID')


def remove_couriers(courier_list):
    util.loop_remove_items_from_list('courier', courier_list)


# TESTS
