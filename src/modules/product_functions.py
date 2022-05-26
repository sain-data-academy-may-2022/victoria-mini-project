'''Module with functions to manage the products list'''


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
    print_product_options()

    while running:
        choice = input('\nPlease select an option:\n> ')

        if choice == '0':
            running = False
            return product_list

        elif choice == '1':
            print('product list')

        elif choice == '2':
            print('new')

        elif choice == '3':
            print('update')

        elif choice == '4':
            print('delete')

        else:
            print('Invalid selection.')
