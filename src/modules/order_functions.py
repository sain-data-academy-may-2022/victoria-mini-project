'''Module with functions to manage the orders list'''


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
def order_management(order_list):
    '''Maintains the loop for the order management menu'''

    running = True
    print_order_options()

    while running:
        choice = input('\nPlease select an option:\n> ')

        if choice == '0':
            running = False
            return order_list

        elif choice == '1':
            print('order list')

        elif choice == '2':
            print('new')

        elif choice == '3':
            print('advance status')

        elif choice == '4':
            print('update')

        elif choice == '5':
            print('delete')

        else:
            print('Invalid selection.')
