# import
from modules.clear import clear

# product list
products = []

# function to print product management menu
def print_product_options():
    print('''Product Management
    
    [1] - Display Product List
    [2] - Add a New Product
    [3] - Update Existing Product
    [4] - Delete Product
    
    [0] - Back to Main Menu''')

def check_list_size(a):
    if len(a) != 0:
        return True
    else:
        return False

def print_product_list():
    # print product list without index
    if check_list_size(products) == False:
        print('There are no products currently listed.')
    else:
        for each in products:
            print(each)

# function to control the product management menu
def product_menu():
    ### print product management menu
    print_product_options()
    print('\nSelect an option:')

    # maintain product management menu
    while True:

        # ask for user input first, then check against menu options
        user_input = input('> ')

        if user_input == '0':   ### done
            # RETURN to main menu
            clear()
            break

        elif user_input == '1': ### done
            # PRINT products list
            clear()
            print_product_options()
            print('\n[1] - Display Product List\n')
            print_product_list()
            print('\nSelect another option.')

        elif user_input == '2':
            # CREATE new product
            # GET user input for product name
            # APPEND product name to products list
            clear()
            print_product_options()
            print('\n[2] - Add a New Product\n')

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
            clear()
            print_product_options()
            print('\nPlease enter a valid option.\n')
