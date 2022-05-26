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
    
    [0] - Back to Main Menu''')


# product option management function
def product_management(product_list):
    '''Maintains the loop for the product management menu'''

    running = True

    cs.clear_screen()
    print_product_options()

    while running:
        choice = input('\nPlease select an option:\n> ')

        if choice == '0':
            running = False
            return product_list

        elif choice == '1':
            util.print_plain_list('products', product_list)

        elif choice == '2':         # DONE
            add_products(product_list)

        elif choice == '3':
            update_a_product(product_list)
            print('update')

        elif choice == '4':
            util.print_indexed_list('products', product_list)

        elif choice == 'r':
            cs.clear_screen()
            print_product_options()

        else:
            print('Invalid selection.')


def add_products(product_list):
    '''Loop which adds a product to a product list'''

    util.loop_add_items_to_list('product', product_list)


def update_a_product(product_list):
    print('\n' + util.format_list_indexed(product_list))
    index = util.get_int_input('Enter the index of the item to be updated:') - 1

    print(util.is_index_within_range(index, product_list))



def remove_products(product_list):
    util.loop_remove_items_from_list('courier', product_list)


# TESTS
