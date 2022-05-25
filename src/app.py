### imports
from modules.clear_screen import clear_screen
from file_handlers.csv_handler import load_products, write_products, \
                                    load_couriers, write_couriers
from file_handlers.json_handler import load_orders, write_orders
import modules.product_management as pm

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
    clear_screen()
    print('''\nWelcome to Bready or Not Breakfast Bar

    [1] - Product Management
    [2] - Order Management
    [3] - Courier Management

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
    [3] - Advance Order Status
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
def print_order_list(orders, s_list):         # print a given dict of dictionaries
    print('------')
    for index in orders:
        print_order(index, orders[index], s_list)
        print('------')

def print_order(idx, ord, ord_status):        # prints a given dictionary in a specified format
    print(f'''Order Number: {idx}

   Name:  {ord['customer_name']}
Address:  {ord['customer_address']}
  Phone:  {ord['customer_phone']}

Order Status: {ord_status[ord['status']]}''')

def print_num_name(dict):                     # prints just the name and order number of a given dict
    for index in dict:
        print(f'Order: {index}, Name: {dict[index]["customer_name"]}')

def print_num_name_status_changeable(dict, ord_status):  # prints the name, status, and order number of a given dict
    for index in dict:
        # if dict[index]['status'] < max(ord_status) :
        print(f'Order: {index}, {dict[index]["customer_name"]}, {ord_status[dict[index]["status"]]}')

def add_order(count, dict):                   # takes a list of dicts and an order count, returns new order count
    new_order = {}
    new_order['customer_name'] = input('\nPlease enter the customer\'s name:\n> ').strip()
    new_order['customer_address'] = input('\nPlease enter the customer\'s address:\n> ').strip()
    new_order['customer_phone'] = input('\nPlease enter the customer\'s phone number:\n> ').strip()
    new_order['status'] = 1

    dict[str(count)] = new_order
    count += 1

    return count

def get_order_num(dict):
    while True:
        print(dict)
        try:
            index = input('\nEnter the order number:\n> ')
            if index in dict:
                return index
            else:
                print('\nOrder number does not exist.')
        except ValueError:
            print('\nNot a valid order number.')

def delete_order(dict):                       # deletes a dict at index from given dict
    print_num_name(dict)
    idx = get_order_num(dict)
    del dict[idx]

def advance_status(idx, dict, s_list):        # 
    if dict[idx]['status'] < max(s_list):
        dict[idx]['status'] += 1
        return dict
    else:
        print('This order has already been delivered.')

def change_order_status(dict, s_list):        # 
    print_num_name_status_changeable(dict, s_list)
    idx = get_order_num(dict)
    dict = advance_status(idx, dict, s_list)
    return dict

def change_order_details(dict, s_list):
    print_order_list(dict, s_list)
    idx = get_order_num(dict)
    print('\nYou are changing:\n')
    print_order(idx, dict[idx], s_list)
    
    text = input('\nEnter the updated customer name or enter 0 to skip:\n> ').strip()
    if text != '0':
        dict[idx]['customer_name'] = text
    text = input('\nEnter the updated customer address or enter 0 to skip:\n> ').strip()
    if text != '0':
        dict[idx]['customer_address'] = text
    text = input('\nEnter the updated customer phone number or enter 0 to skip:\n> ').strip()
    if text != '0':
        dict[idx]['customer_phone'] = text
    text = int(input('\nEnter the updated order status or enter 0 to skip:\n> ').strip())
    if text != 0:
        dict[idx]['status'] = text
    print_order(idx, dict[idx], s_list)
    

# utilities
def check_if_empty(list):           # check if a given list is empty
    # returns True if list has elements
    if list:
        return True
    else:
        return False

### program

# loads product, orders 
products = load_products()
orders = load_orders()
couriers = load_couriers()
order_count = int(max(orders.keys())) + 1

while True:             # main program loop
    user_input = main_menu()

    if user_input == '0':           ### ADD EXPORT FOR COURIER LIST
        # export products and orders, exit program
        write_products(products)
        write_orders(orders)
        write_couriers(couriers)
        print('\nClosing program, goodbye!\n')
        break

    elif user_input == '1': # enter product menu
        
        while True:
            user_input = product_menu()

            if user_input == '0':   # return to main menu       ### DONE
                break

            elif user_input == '1': # print product list        ### DONE - refactored
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

            elif user_input == '3': # advance order status      ### DONE
                change_order_status(orders, order_status)

            elif user_input == '4': # update order details      ### DONE
                change_order_details(orders, order_status)

            elif user_input == '5': # delete existing order     ### DONE
                delete_order(orders)

            else:                   # handle invaid input       ### DONE
                print('\nPlease enter a valid option.')

    elif user_input == '3': # enter courier menu
        
        while True:

            user_input = input("> ")

            if user_input == '0':   # return to main menu       ### 
                break

            elif user_input == '1': # print courier list        ### 
                pass 

            elif user_input == '2': # create new courier        ###
                pass
            
            elif user_input == '3': # update existing courier   ###
                pass

            elif user_input == '4': # delete courier            ###
                pass



    else:                   # handle invalid input
        print('\nPlease enter a valid option.')

# end of program debug area

