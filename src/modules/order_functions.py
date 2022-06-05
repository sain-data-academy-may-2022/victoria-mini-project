'''Module with functions to manage the orders list'''

import modules.clear_screen as cs
import modules.utilities as util

### data
status = ['order placed       ',
          'being prepared     ',
          'awaiting collection',
          'in-transit         ',
          'delivered          ']


### main functions
# print the order management menu options
def print_order_options():
    '''Prints the order management menu options'''

    print('''\nOrder Management
    
    [1] - Display Order List
    [2] - Add a New Order
    [3] - Advance Order Status
    [4] - Update Existing Order Details
    [5] - Delete an Order
    
    [0] - Back to Main Menu''')


# order option management function
def order_management(product_list, courier_list, order_list):
    '''Maintains the loop for the order management menu'''

    running = True

    cs.clear_screen()
    print_order_options()

    while running:

        choice = input('\nPlease select an option:\n> ')

        if choice == '0':
            running = False
            return order_list

        elif choice == '1':
            util.print_order_list(order_list, product_list, courier_list, status)

        elif choice == '2':
            add_order(order_list, product_list, courier_list)

        elif choice == '3':
            update_order_status(order_list, status)

        elif choice == '4':
            update_order_details(order_list, product_list, courier_list, status)
            # print('Hi, this currently does nothing :)') AND NEEDS REFACTORING

        elif choice == '5':
            delete_an_order(order_list, status)
            # print('Hi, this currently does nothing :)') AND NEEDS REFACTORING

        elif choice == '':
            cs.clear_screen()
            print_order_options()


        else:
            print('Invalid selection.')


def add_order(order_list: dict, product_list: list, courier_list: list):
    '''generic docstring'''
    order_count = 0
    order_count = int(max(order_list.keys())) + 1
    new_order = {}

    new_order['name'] = \
        util.format_string(input('\nPlease enter the customer\'s name:\n> '))

    new_order['address'] = \
        util.format_string(input('\nPlease enter the customer\'s address:\n> '))

    new_order['phone'] = \
        util.format_string(input('\nPlease enter the customer\'s phone number:\n> '))

    util.print_indexed_list('courier', courier_list)

    new_order['courier'] = \
        util.get_int_within_list('Please enter the courier\'s ID:', courier_list)

    new_order['status'] = 0

    new_order['items'] = \
        util.get_products_for_order(product_list)

    util.print_an_order(str(order_count),new_order,product_list,courier_list,status)

    confirm = input('\nPress ENTER to confirm adding this order, or 0 to cancel:\n> ')
    
    if confirm == '':
        order_list[str(order_count)] = new_order

    return order_list


def update_order_status(order_list, status_list):
    util.print_short_order_list(order_list, status_list)
    updated_order = \
        util.get_dictionary_key('\nEnter the order number to be updated:', order_list)

    util.print_list_test(status, 1)

    updated_status = \
        util.get_int_within_list('\nEnter the status code for this order:', status)

    order_list[updated_order]['status'] = updated_status


def update_order_details(order_list, product_list, courier_list, status_list):     # <--- TO DO ::: FIGURE OUT HOW TO ADD UPDATES FOR STATUS AND COURIER WITH LOGIC CHECKS
    util.print_order_list(order_list, product_list, courier_list, status_list)
    updated_order = \
        util.get_dictionary_key('\nEnter the order number to be updated:', order_list)

    for key in order_list[updated_order].keys():

        if key == 'courier' or key == 'status':
            if key == 'courier':
                print('\n', util.format_list_indexed(courier_list))

            elif key == 'status':
                util.print_list_test(status, 1)

            new_value = util.format_string(input(f'\nEnter a new {key} or ENTER to skip:\n> '))
            if new_value != '':
                new_value = int(new_value) - 1

        elif key == 'items':
            new_value = util.get_products_for_order(product_list)
            if new_value == []:
                new_value = ''

        else:
            new_value = util.format_string(input(f'\nEnter a new {key} or ENTER to skip:\n> '))

        if new_value != '':
            order_list[updated_order][key] = new_value


def delete_an_order(order_list, status_list):
    util.print_short_order_list(order_list, status_list)
    deleted_order = \
            util.get_dictionary_key('\nEnter the order number to be deleted:', order_list)
    
    confirm = input('Press ENTER to confirm, or 0 to cancel.\n> ')

    if confirm == '':
        del order_list[deleted_order]
        print('This order has been deleted.')

