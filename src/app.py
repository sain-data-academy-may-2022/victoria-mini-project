# imports

import os


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


# functions



# main program
while True:
    ### print main menu here
    print('main menu here:')

    # ask for user input first, then check against menu options
    user_input = input('> ')

    if user_input == '0':
        # if option 0, exit program
        break

    elif user_input == '1':
        # if option 1, enter product management menu
        print('product management')

        while True:
            ### print product management menu
            print('product management menu')

            # ask for user input first, then check against menu options
            user_input = input('> ')

            if user_input == '0':
                # RETURN to main menu
                break

            elif user_input == '1':
                # PRINT products list
                print('print products list')

            elif user_input == '2':
                # CREATE new product
                # GET user input for product name
                # APPEND product name to products list
                print('create new product')

            elif user_input == '3':
                # UPDATE existing product
                # PRINT products name with its index value
                # GET user input for product index value
                # GET user input for new product name
                # UPDATE product name at index in products list
                print('update existing product')

            elif user_input == '4':
                # DELETE product
                # PRINT products list
                # GET user input for product index value
                # DELETE product at index in products list
                print('delete product')

            else:
                # handle invalid input
                print('Please select a valid option.')


    elif user_input == '2':
        # if option 2, enter order management menu
        print('order management')

    else:
        print('Please select a valid option.')