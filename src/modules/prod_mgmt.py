# import
from modules.clear import clear

# product list
products = [
    'Waffles',
    'Pancakes',
    'Coffee',
    'Tea',
    'Toast'
]

def print_product_options():
    # function to print product management menu
    print('''Product Management
    
    [1] - Display Product List
    [2] - Add a New Product
    [3] - Update Existing Product
    [4] - Delete a Product
    
    [0] - Back to Main Menu''')

def check_list_size(list):
    if len(list) != 0:
        return True
    else:
        return False

def print_product_list(list):
    # print product list without index
    if check_list_size(list) == False:
        print('There are no products currently listed.')
    else:
        print('The current menu is:')
        for item in list:
            print(f'\t{item}')

def print_product_list_with_index(list):
    # print product list with index
    if check_list_size(list) == False:
        print('There are no products currently listed.')
    else:
        print('ID\tName')
        for each in list:
            print(f'{products.index(each)+1}\t{each}')     # index starts with 1

def remove_item(index):
    index = index-1
    print(index)

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
            print_product_list(products)
            print('\nSelect another option:')

        elif user_input == '2': ### done
            # CREATE new product
            # GET user input for product name
            # APPEND product name to products list
            clear()
            print_product_options()
            print('\n[2] - Add a New Product\n')

            while True:
                new_product = input('Enter new product or enter 0 to cancel: ').strip()

                if new_product == '0':
                    clear()
                    print_product_options()
                    print('\nSelect another option:')
                    break

                else:
                    products.append(new_product)
                    print(f'\n{new_product} was added to the product list.\n')

        elif user_input == '3': ### TO DO
            # UPDATE existing product
            # PRINT products name with its index value
            # GET user input for product index value
            # GET user input for new product name
            # UPDATE product name at index in products list
            print('update existing product')

        elif user_input == '4': ### DONE - refactor
            # DELETE product
            # PRINT products list
            # GET user input for product index value
            # DELETE product at index in products list
            clear()
            print_product_options()
            print('\n[4] - Delete a Product\n')

            while check_list_size(products) == True:

                print_product_list_with_index(products)
                print('\nEnter the ID of the item to be removed, or enter 0 to cancel:')

                user_input = input('> ')

                if user_input == '0':
                    break
                else:
                    try:
                        user_input = int(user_input)
                    except:
                        print('\nPlease enter the ID of the item to be removed.\n')

                    if type(user_input) is int:
                        if user_input > 0 and user_input <= len(products):
                            products.pop(user_input-1)
                        else:
                            print('\nID does not exist in product list.\n')
                    else:
                        continue

            clear()
            print_product_options()
            print('\n[4] - Delete a Product\n')
            print_product_list(products)
            print('\nSelect another option:')
            
        else: ### done
            # handle invalid input
            clear()
            print_product_options()
            print('\nPlease enter a valid option.')
