'''Module with functions to manage the courier list'''


# print the courier management menu options
def print_courier_options():
    '''Prints the courier management menu options'''

    print('''\nCourier Management
    
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

    while running:
        choice = input('\nPlease select an option:\n> ')

        if choice == '0':
            running = False
            return courier_list

        elif choice == '1':
            print('courier list')

        elif choice == '2':
            print('new')

        elif choice == '3':
            print('update')

        elif choice == '4':
            print('delete')

        else:
            print('Invalid selection.')
