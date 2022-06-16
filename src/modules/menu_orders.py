'''Module with functions to manage the orders list'''


### imports
import modules.clear_screen as cs


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

    # 
    elif choice == '1':
        print('1')
        #

    # 
    elif choice == '2':
        print('2')
        #

    # 
    elif choice == '3':
        print('3')
        #

    # clear screen and reprint order menu options
    elif choice == '':
        cs.clear_screen()
        print_order_options()

    # handle incorrect input
    else: 
        print('Invalid selection. Please select a valid menu option.')

    return running, products, couriers, orders


# controls order menu loop
def order_menu(products, couriers, orders, connection):

    cs.clear_screen()
    print_order_options()

    running = True
    
    while running:
        
        running, orders = order_menu_choice(products, couriers, orders, connection)

    return orders
    

