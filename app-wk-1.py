# imports

import os

# create products list

products = [
    'Salad',
    'Coffee',
    'Sandwich'
]

# functions

def clear():
    # clears terminal screen
    os.system('clear')

def check_menu_size():
    # check if product list is 0 length
    if len(products) != 0:
        return True
    else:
        return False

def print_menu():
    # print product list
    if check_menu_size() == True:
        print('''
The current menu is:''')
        for item in products:
            print(item)
        print('')
    else: 
        print('There is nothing in the products menu currently.')

def print_menu_with_index():
    # print products list with index
    # index starts from 1
    if check_menu_size() == True:
        print('ID    Name')
        for each in products:
            print(f'{products.index(each)+1}     {each}')
        print('')
    else:
        print('There is nothing in the products menu currently.')

def print_product_management():
    clear()
    print('''Product Management

    [1] - Display Product List
    [2] - Add a New Product
    [3] - Update Existing Product
    [4] - Delete Product

    [0] - Back to Main Menu
        ''')


# main program

# main menu
# maintain program loop
while True:
    clear()
    print('''Welcome!

    [1] - Product Management
    Exciting new features coming soon...
    
    [0] - Exit Application
    ''')

    # ask for user input
    user_input = input('> ')

    # if 0, exit program
    if user_input == '0':
        print('''
Closing program, goodbye!
''')
        break

    # print product management menu
    elif user_input == '1':
        print_product_management()

        # keeps submenu running
        while True:
            user_input = input('> ')

            # go back to main menu
            if user_input == '0':
                clear()
                break
            
            # print product list
            elif user_input == '1':
                print_product_management()
                print('''[1] - Display Product List''')
                print_menu()
                print('''Select another option.''')
            
            # create new product
            elif user_input == '2':
                print_product_management()
                print('''[2] - Add a New Product
                ''')
                while True:
                    new_product = input('Enter new product or enter 0 to cancel: ')
                    if new_product == '0':
                        print_product_management()
                        break
                    else:
                        products.append(new_product)
                        print(f'''
{new_product} was added to the product list.
                        ''')

            # update existing product
            elif user_input == '3':
                print_product_management()
                print('''[3] - Update Existing Product
                ''')
                print_menu_with_index()

                # get user input
                # to do: add input checking
                prod_index = int(input('''
Enter the ID of the product you wish to update or enter 0 to cancel.
> '''))-1
                if prod_index == -1:
                    print_product_management()

                elif prod_index in range(0,len(products)):
                    products[prod_index] = input('''
Please enter the updated product name.
> ''')
                    print_product_management()
                    print(f'''ID {prod_index + 1} is now {products[prod_index]}
''')
                    print('''Select another option.''')
                else:
                    print('The index you have chosen does not exist.')

            # delete product
            elif user_input == '4':
                
                # check products list has things in it
                while check_menu_size() == True:

                    print_product_management()
                    print('''[4] - Delete Product
                    ''')
                    print_menu_with_index()

                    user_input = int(input('''Enter the ID of the item you wish to remove or enter 0 to cancel.
> '''))-1
                    if user_input == -1:
                        print_product_management()
                        break
                    elif user_input in range(0,len(products)):
                        print(f'''
{products.pop(user_input)} has been removed from the product list.
''')
                    else:
                        print('ID not recognised, please try again.')

                print_product_management()
                print_menu()

            else:
                print('Please enter a valid option.')

    elif user_input == '2':
        print('this is not added yet, please come back soon')

    else:
        print('Please select a valid option.')