### imports
import os
import csv
import json

### data            # split out to seperate files
# product list
products = [
    'Waffles',
    'Pancakes',
    'Coffee',
    'Tea',
    'Toast'
]

# order list
order_count = 1

orders = {
123: {
    'customer_name': 'Sherlock Holmes',
    'customer_address': '221b Baker Street',
    'customer_phone': '07700 123 456',
    'status': 5
    },
258: {
    'customer_name': 'Phileas Fogg',
    'customer_address': '7 Savile Row',
    'customer_phone': '07700 987 321',
    'status': 2
    },
347: {
    'customer_name': 'Wallace and Gromit',
    'customer_address': '62 West Wallaby Street',
    'customer_phone': '07700 232 787',
    'status': 1
    }
}

order_status = {
    1: 'order placed',
    2: 'being prepared',
    3: 'completed, awaiting collection',
    4: 'in-transit',
    5: 'delivered'
}

### functions
# menu management
def main_menu():                    # print main menu options
    print('''\nWelcome to 

    [1] - Product Management
    [2] - Order Management

    [0] - Exit Application''')

    choice = input('\nPlease select an option:\n> ')
    return choice

def product_menu():                 # print product management menu options
    print('''\nProduct Management
    
    [1] - Display Product List
    [2] - Add a New Product
    [3] - Update Existing Product
    [4] - Delete a Product
    
    [0] - Back to Main Menu''')

    choice = input('\nPlease select an option:\n> ')
    return choice

def order_menu():                   # print order management menu options
    print('''\nOrder Management
    
    [1] - Display Order List
    [2] - Add a New Order
    [3] - Update Existing Order Status
    [4] - Update Existing Order Details
    [5] - Delete an Order
    
    [0] - Back to Main Menu''')

    choice = input('\nPlease select an option:\n> ')
    return choice

# product management
def print_list(list):               # print a given list without indexes
    for item in list:
        print(f'\t{item}')

def print_indexed_list(list):       # print a given list with indexes
    print('ID\tName')
    for each in list:
        print(f'{list.index(each)+1}\t{each}')

def add_item(item, list):           # takes item and appends to a list
    list.append(item.strip())
    return item

def get_index_input(list):          # takes list and gets input for an index within that list
    print_indexed_list(list)
    while True:
        try:
            index = int(input('\nPlease enter the ID:\n> '))
            if index > 0 and index <= len(list):
                return index
            else:
                print('\nID does not exist in product list.')
        except ValueError:
            print('\nNot a valid ID.')

def update_item(list):              #
    id = get_index_input(list)
    list[id - 1] = input('\nPlease enter the updated product name:\n> ').strip()

def delete_item(list):              #
    id = get_index_input(list)
    list.pop(id - 1)

# order management
def print_order_list(orders, s_list):      # print a given dict of dictionaries
    print('------')
    for index in orders:
        print_order(index, orders[index], s_list)
        print('------')

def print_order(idx, ord, ord_status):     # prints a given dictionary in a specified format
    print(f'''Order Number: {idx}

   Name:  {ord['customer_name']}
Address:  {ord['customer_address']}
  Phone:  {ord['customer_phone']}

Order Status: {ord_status[ord['status']]}''')

def print_order_and_name(dict):            # prints just the name and order number of a given dict
    for index in dict:
        print(f'Order: {index}, Name: {dict[index]["customer_name"]}')

def add_order(count, dict):                # takes a list of dicts and an order count, returns new order count
    new_order = {}
    new_order['customer_name'] = input('\nPlease enter the customer\'s name:\n> ').strip()
    new_order['customer_address'] = input('\nPlease enter the customer\'s address:\n> ').strip()
    new_order['customer_phone'] = input('\nPlease enter the customer\'s phone number:\n> ').strip()
    new_order['status'] = 1

    dict[count] = new_order
    count += 1

    return count

def get_order_num(dict):
    print_order_and_name(dict)
    while True:
        try:
            index = int(input('\nEnter the order number:\n> '))
            if index in dict:
                return index
            else:
                print('\nOrder number does not exist.')
        except ValueError:
            print('\nNot a valid order number.')

def delete_order(dict):               # deletes a dict at index from given dict
    idx = get_order_num(dict)
    del dict[idx]



# utilities
def clear():                        # clear terminal screen
    os.system('clear')

def check_if_empty(list):           # check if a given list is empty
    # returns True if list has elements
    if list:
        return True
    else:
        return False

def load_products():                # load products.csv file and return it as a list
    with open("data/products.csv", 'r') as file:
        csv_file = list(csv.reader(file, delimiter=','))
        return csv_file[0]

def write_products(list):           # takes list and writes out products.csv file
    with open('data/products.csv', 'w') as file:
        print(list)
        write = csv.writer(file)
        write.writerow(list)
    

### program
products = load_products()

while True:             # main program loop

    user_input = main_menu()

    if user_input == '0':   # exit program
        write_products(products)
        print('\nClosing program, goodbye!\n')
        break

    elif user_input == '1': # enter product menu
        
        while True:
            user_input = product_menu()

            if user_input == '0':   # return to main menu       ### DONE
                break

            elif user_input == '1': # print product list        ### DONE
                if check_if_empty(products):
                    print('\nThe current menu is:')
                    print_list(products)
                else:
                    print('\nThere are no products currently listed.')

            elif user_input == '2': # create new product        ### DONE
                while True:
                    new_prod = input('\nEnter new product or enter 0 to cancel:\n> ').strip()

                    if new_prod == '0':
                        break
                    else:
                        print(f'\n{add_item(new_prod, products)} was added to the product list.')

            elif user_input == '3': # update existing product   ### DONE ???
                update_item(products)

            elif user_input == '4': # delete existing product   ### DONE ???
                delete_item(products)

            else:                   # handle invaid input       ### DONE
                print('invalid input')

    elif user_input == '2': # enter order menu
        
        while True:
            user_input = order_menu()

            if user_input == '0':   # return to main menu       ### DONE
                break

            elif user_input == '1': # print order list          ### DONE
                print_order_list(orders, order_status)

            elif user_input == '2': # create new order          ### DONE
                order_count = add_order(order_count, orders)

            elif user_input == '3': # update order status       ### CURRENT
                continue

            elif user_input == '4': # update order details      ### TO DO
                continue

            elif user_input == '5': # delete existing order     ### DONE
                delete_order(orders)

            else:                   # handle invaid input       ### DONE
                print('\nPlease enter a valid option.')

    else:                   # handle invalid input
        print('\nPlease enter a valid option.')