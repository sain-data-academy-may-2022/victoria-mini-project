# imports

from modules.prod_mgmt import product_menu
from modules.clear import clear


# products
### create an initial products list, replace later

products = [
    'salad',
    'coffee',
    'sandwich'
]

# orders
### create an initial orders list (list of dicts), replace later

orders = []


# main program
# maintain main program loop
while True:
    ### print main menu here
    print('main menu:')

    # ask for user input first, then check against menu options
    user_input = input('> ')

    if user_input == '0':
        # if option 0, exit program
        clear()
        print('\nClosing program, goodbye!')
        break

    elif user_input == '1':
        # call product management function
        product_menu()

    elif user_input == '2':
        # if option 2, enter order management menu
        print('order management')

        # maintain order management menu
        while True:
            ### print order management menu
            print('order management menu')

            # ask for user input first, then check against menu options
            user_input = input('> ')

            if user_input == '0':
                # RETURN to main menu
                break

            elif user_input == '1':
                # PRINT orders dictionary
                print('print orders dictionary')

            elif user_input == '2':
                # GET user input for customer name
                # GET user input for customer address
                # GET user input for customer phone number

                # SET order status to be 'preparing'
                # APPEND order to orders list
                print('create order and get input')

            elif user_input == '3':
                # UPDATE existing order status
                
                # PRINT orders list with its index values
                # GET user input for order index value
                # PRINT order status list with index values
                # GET user input for order status index value
                # UPDATE status for order
                print('update existing order status')

            elif user_input == '4':
                # UPDATE existing order
                # PRINT orders list with its index values
                # GET user input for order index value

                # FOR EACH key-value pair in selected order:
                #   GET user input for updated property
                #   IF user input is blank:
                #       do not update this property
                #   ELSE:
                #       update the property value with user input
                print('update existing order')

            elif user_input == '5':
                # DELETE order

                # PRINT orders list
                # GET user input for order index value
                # DELETE order at index in order list
                print('delete order')

            else:
                print('Please enter a valid option.')

    else:
        print('Please enter a valid option.')