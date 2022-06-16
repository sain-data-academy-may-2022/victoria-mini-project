'''Module with functions to manage the orders list'''


### imports
import modules.clear_screen as cs
import modules.funcs_orders as ord


### data
status = ['order placed       ',
          'being prepared     ',
          'awaiting collection',
          'in-transit         ',
          'delivered          ']


### menu functions
# print the order management menu options
def print_order_options():
    '''Prints the order management menu options'''

    cs.clear_screen()

    print('''\nOrder Management
    
    [1] - Display Order List
    [2] - Add a New Order
    [3] - Advance Order Status
    [4] - Update Existing Order Details
    [5] - Delete an Order
    
    [0] - Back to Main Menu''')


# controls order menu input and selection
def order_menu_choice(products, couriers, orders, connection):

    choice = input('\nPlease select an option:\n> ')
    running = True

    # exit order menu loop
    if choice == '0':
        running = False
        return running, products, couriers, orders

    # print order list
    elif choice == '1':
        ord.print_order_list()

    # create new order
    elif choice == '2':
        ord.try_add_order()

    # update existing order status
    elif choice == '3':
        ord.try_update_order_status()

    # update existing order details
    elif choice == '4':
        ord.try_update_order_details()

    # delete order
    elif choice == '5':
        ord.try_delete_order()

    # clear screen and reprint order menu options
    elif choice == '':
        print_order_options()

    # handle incorrect input
    else: 
        print('\nInvalid selection. Please select a valid menu option.')

    return running, products, couriers, orders


# controls order menu loop
def order_menu(products, couriers, orders, connection):

    print_order_options()

    running = True
    
    while running:
        
        running, products, couriers, orders = order_menu_choice(products, couriers, orders, connection)

    return products, couriers, orders
    

