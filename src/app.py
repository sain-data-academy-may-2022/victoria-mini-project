# imports

from modules.prod_mgmt import product_menu
from modules.ord_mgmt import order_menu
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
    clear()
    print('main menu:')

    # ask for user input first, then check against menu options
    user_input = input('> ')

    if user_input == '0':
        # if option 0, exit program
        clear()
        print('Closing program, goodbye!\n\n\n')
        break

    elif user_input == '1':
        # call product management function
        product_menu()

    elif user_input == '2':
        # call order management function
        order_menu()

    else:
        print('Please enter a valid option.')