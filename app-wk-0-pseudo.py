# main program
# maintain main program loop
while True:
    ### print main menu here
    print('main menu:')

    # ask for user input first, then check against menu options
    user_input = input('> ')

    if user_input == '0':
        # if option 0, exit program
        print('\nClosing program, goodbye!')
        break

    elif user_input == '1':
        # if option 1, enter product management menu
        print('product management')

        # maintain product management menu
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
        # if option 2, enter courier management menu
        print('courier management')

        # maintain courier management menu
        while True:
            ### print courier management menu
            print('courier management menu')

            # ask for user input first, then check against menu options
            user_input = input('> ')

            if user_input == '0':
                # RETURN to main menu
                break

            elif user_input == '1':
                # PRINT couriers list

            elif user_input == '2':
                # CREATE new courier
                # GET user input for courier name
                # APPEND courier name to couriers list

            elif user_input == '3':
                # UPDATE existing courier

                # PRINT courier names with its index value
                # GET user input for courier index value
                # GET user input for new courier name
                # UPDATE courier name at index in couriers list

            elif user_input == '4':
                # DELETE courier

                # PRINT courier list
                # GET user input for courier index value
                # DELETE courier at index in courier list

    elif user_input == '3':
        # if option 3, enter order management menu
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

                # PRINT couriers list with index value for each courier
                # GET user input for courier index to select courier
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
                print('Please select a valid option.')

    else:
        print('Please select a valid option.')