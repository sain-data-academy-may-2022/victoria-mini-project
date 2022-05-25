'''Module with functions to manage the products list'''


import utilities as utilities
from clear_screen import clear_screen


# print the product management menu options
def print_product_options():
    '''Prints the product management menu options'''

    clear_screen()
    print('''Product Management
    
    [1] - Display Product List
    [2] - Add a New Product
    [3] - Update Existing Product
    [4] - Delete a Product
    
    [0] - Back to Main Menu''')


# product option management function
def product_management(product_list):
    '''Maintains the loop for the product management menu'''

    running = True
    print_product_options()
    print('\n\n')

    while running:

        running = product_menu_input_check(product_list)

    return product_list


# product option selection
def product_menu_input_check(product_list):
    '''Manages the input of menu options'''

    option = input('Please select an option:\n> ')

    # leave product management
    if option == '0':
        return False

    # display product list
    elif option == '1':
        print_product_options()
        print('\n[1] - Display Product List\n')

        print_product_list(product_list)

    # add a new product
    elif option == '2':
        print_product_options()
        print('\n[2] - Add a New Product\n')

        add_product_loop(product_list)

    # update existing product
    elif option == '3':
        print_product_options()
        print('\n[3] - Update Existing Product\n')
        print_product_indexed(product_list)

        update_product(product_list)

    # delete a product
    elif option == '4':
        print_product_options()
        print('\n[4] - Delete a Product\n')
        print_product_indexed(product_list)

        remove_product_loop(product_list)

    # handles invalid input
    else:
        print_product_options()
        print('\nInvalid input.\n')

    return True


# loop for adding a new product
def add_product_loop(product_list):
    '''Loop which adds a product to a product list'''

    while True:
        new_product = utilities.format_string(input('Enter new product or enter 0 to cancel:\n> '))
        if new_product == '0':
            break

        elif len(new_product) > 0:
            product_list = utilities.add_item_to_list(new_product, product_list)
            print(f'\n{product_list[-1]} has been added to the menu.\n')

        else:
            print('Please enter a valid product name.\n')

    return product_list


# update a product
def update_product(product_list):
    '''Gets input to update an item in a list'''
    index = utilities.get_index(product_list)

    new_product = utilities.format_string(input('Enter new product or enter 0 to cancel:\n> '))

    if new_product == '0':
        pass

    elif len(new_product) > 0:
        utilities.update_item_in_list(index, new_product, product_list)
        print(f'{index} is now {new_product}')

    else:
        print('Please enter a valid product name.\n')



#loop for removing products from a list
def remove_product_loop(product_list):
    '''Loop to control removing products from a list'''

    print_product_options()
    print('\n[4] - Delete a Product\n')

    while utilities.check_list_has_items(product_list):
        print_product_indexed(product_list)

        index = utilities.get_index(product_list)

        if index is None:
            print_product_options()
            print('')
            break

        else:
            confirm = input(f'\nPress Enter to confirm removal of {product_list[index-1]}.\n> ')

            if confirm == '':
                print(f'\n{product_list[index - 1]} has been removed.\n')
                utilities.remove_item_from_list(index, product_list)


# # remove a product from a list
# def remove_product(product_list):
#     '''Removes a product from a product list'''

#     if index is None:
#         return product_list

#     else:


#     return product_list


# print a product list
def print_product_list(product_list):
    '''Prints the product list'''

    if utilities.check_list_has_items(product_list):
        print('The current menu is:')
        print(utilities.format_list(product_list))

    else:
        print('There are no products currently listed.\n')


# print a product list with indexes
def print_product_indexed(product_list):
    '''Prints the product list with indexes'''

    if utilities.check_list_has_items(product_list):
        print(utilities.format_list_indexed(product_list))

    else:
        print('There are no products currently listed.\n')


# TESTS

product_list2 = ['tea','coffee','grape juice']


# utilities.get_index(product_list2)
product_management(product_list2)

# add_product(product_list2)
