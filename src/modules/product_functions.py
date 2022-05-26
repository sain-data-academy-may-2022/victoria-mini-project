'''Module with functions to manage the products list'''

import modules.clear_screen as cs
import modules.utilities as util

# print the product management menu options
def print_product_options():
    '''Prints the product management options'''

    print('''\nProduct Management
    
    [1] - Display Product List
    [2] - Add a New Product
    [3] - Update Existing Product
    [4] - Delete a Product
    
    [0] - Back to Main Menu\n''')


# product option management function
def product_management(product_list):
    '''Maintains the loop for the product management menu'''

    running = True

    cs.clear_screen()
    print_product_options()

    while running:
        choice = input('Please select an option:\n> ')

        if choice == '0':
            running = False
            return product_list

        elif choice == '1':
            util.print_plain_list('products', product_list)

        elif choice == '2':
            add_products(product_list)

        elif choice == '3':
            update_a_product(product_list)

        elif choice == '4':
            remove_products(product_list)

        elif choice == 'r':
            cs.clear_screen()
            print_product_options()

        else:
            print('Invalid selection.\n')


def add_products(product_list):
    '''Loop which adds a product to a product list'''

    util.loop_add_items_to_list('product', product_list)


def update_a_product(product_list):         # <---- REFACTOR
    '''generic docstring'''
    print('\n' + util.format_list_indexed(product_list))
    index = util.get_int_input('Enter the ID of the product to be updated:') - 1

    if util.is_index_within_range(index, product_list):
        new_product = util.format_string(util.get_string_input('\nEnter the new name:'))

        print(f'{product_list[index]} is now {new_product}.\n')

        util.update_item_in_list(new_product, index, product_list)

    else:
        print('Invalid ID\n')


def remove_products(product_list):
    '''generic docstring'''
    util.loop_remove_items_from_list('product', product_list)


# TESTS
