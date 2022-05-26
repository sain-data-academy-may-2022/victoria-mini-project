'''Module with functions to manage the orders list'''

import modules.clear_screen as cs
import modules.utilities as util

### data
status = ['order placed',
        'being prepared',
        'completed, awaiting collection',
        'in-transit',
        'delivered']

order_count = 0

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
            util.print_order_list(order_list, courier_list, status)

        elif choice == '2':
            print('new')

        elif choice == '3':
            print('advance status')

        elif choice == '4':
            print('update')

        elif choice == '5':
            print('delete')

        elif choice == 'r':
            cs.clear_screen()
            print_order_options()


        else:
            print('Invalid selection.')

