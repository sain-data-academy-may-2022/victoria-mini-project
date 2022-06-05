'''utility functions for handling data within the app'''





####################
### BOOL CHECKS
####################
# checks if a list has items or not
def check_list_has_items(a_list: list):
    '''If a list has items, returns True. Otherwise returns False.'''

    if a_list:
        return True

    else:
        return False


# checks if an index exists within a list
def is_index_within_range(index: int, a_list: list):
    '''Returns True if a given integer exists as an index within a list'''

    return index >= 0 and index < len(a_list)


# checks if a str is a key within a dictionary
def is_string_a_key(text: str, a_dict: dict):
    '''returns True is a string exists as a key in a dictionary'''

    return text in a_dict





####################
### ORDERS
####################
#
def get_products_for_order(product_list):
    ''''''
    print('\n', format_list_indexed(product_list))

    running = True

    items = []
    
    while running:
        new_item = get_int_input('\nEnter the ID of the product, or 0 to cancel:')

        if new_item == 0:
            print('\nCurrent items:')

            for each in items:
                print(f'\t{product_list[each]["name"]}')

            loop = input('\nPress ENTER to confirm these items, or 0 to add more:\n> ')
            
            if loop == '':
                running = False

        elif is_index_within_range(new_item - 1, product_list):
            items.append(new_item - 1)
            print(f'{product_list[new_item - 1]["name"]} has been added.')

    return items








####################
### LISTS
####################
# add an item to a list
def add_item_to_list(item: dict, a_list: list):
    '''Adds an item to a list'''

    a_list.append(item)

    return a_list


# loop for repeatedly adding items to a list
def loop_add_items_to_list(type_of_item: str, item_keys: list, a_list: list):
    '''Loops through adding items to a list and returns that list'''

    running = True

    new_item = {}

    while running:
        for key in item_keys:
            value = format_string(get_string_input(f'\nEnter new {type_of_item} {key} or enter 0 to cancel:'))

            if value == '0':
                running = False
                break

            else:
                if key == 'price':
                    new_item[key] = float(value)

                else:
                    new_item[key] = value
            
        else:
            add_item_to_list(new_item, a_list)
            print(f'{a_list[-1]["name"]} has been added to the {type_of_item} list.')

    return a_list


# update a specific item within a list
def update_item_in_list(item: str, index: int, a_list: list):
    '''Replaces the list item at a specific index with a new value'''

    a_list[index] = item

    return a_list


# get updated values for iten within a list
def get_updated_item_values(item: dict):
    '''receives a dict and returns an updated dict'''
    new_item = {}

    for key, value in item.items():
        new_value = get_an_updated_value(value, key)

        if key == 'price':
            new_value = float(new_value)

        new_item[key] = new_value

    return new_item


# remove an item from a list
def remove_item_from_list(index: int, a_list: list):
    '''Remove the item at a given index from a list'''

    removed_item = a_list.pop(index)
    return removed_item, a_list


# loop for repeatedly removing items from a list <--- TO DO
def loop_remove_items_from_list(type_of_item: str, a_list: list):
    '''Loops through removing items from a list and returns that list'''

    while a_list:
        print_indexed_list(type_of_item, a_list)

        index = \
            get_int_input(f'Enter the ID of the {type_of_item} to be removed, or 0 to cancel:') - 1

        if index == -1:
            break

        elif is_index_within_range(index, a_list):
            print(f'{a_list[index]["name"]} has been removed.')
            remove_item_from_list(index, a_list)

    else:
        print(format_list(a_list))

    return a_list





####################
### FORMATTING AND PRINTING
####################
# prints a shortened form of an order dictionary
def print_short_order_list(order_list: dict,
                            status: list):
    '''prints a formatted list of orders in a shortened form'''

    print('')
    for order in order_list:
        print(f'Order {order}: {status[order_list[order]["status"]]} {order_list[order]["name"]}')


# prints a given order in a specified format
def print_an_order(order_id: str,
                order: dict,
                product_list: list,
                courier_list: list,
                status: list):
    '''prints a formatted order'''

    print(f'Order Number: {order_id}')
    print(f'\n   Name:  {order["name"]}')
    print(f'Address:  {order["address"]}')
    print(f'  Phone:  {order["phone"]}')
    if len(order["items"]) > 0:
        print(f'Ordered:  {product_list[order["items"][0]]["name"]}') 
        for each in range(1,len(order["items"])):
            print(f'          ' + f'{product_list[order["items"][each]]["name"]}')
    try:
        print(f'Courier:  {courier_list[order["courier"]]["name"]}')
    except IndexError:
        print('Courier:  Unknown')

    print(f'\nOrder Status: {status[order["status"]]}')


# print a formatted order dictionary
def print_order_list(order_list: dict,
                    product_list: list,
                    courier_list: list,
                    status: list):
    '''prints a formatted list of everything in orders'''
    print('----------------')
    for order in order_list:
        print_an_order(order, order_list[order], product_list, courier_list, status)
        print('----------------')


# prints a list with indexes starting at 0
def print_list_test(a_list, start):    # <--- TO DO - rename
    for index, name in enumerate(a_list, start):
        print(f'{index} - {name}')


# print a list without indexes
def print_plain_list(item_type: str, a_list: list):
    '''prints a plain list'''
    if a_list:
        print(f'\nCurrent {item_type}:', end='')
        print(format_list(a_list))
    else:
        print(f'\nThere are no {item_type} currently listed.\n')


# print a list with indexes
def print_indexed_list(item_type: str, a_list: list):
    '''prints a plain list'''
    if a_list:
        print('\n' + format_list_indexed(a_list))
    else:
        print(f'\nThere are no {item_type} currently listed.\n')


# returns a formatted string of list items for a given list
def format_list(a_list: list):
    '''Returns a formatted string for a given list'''

    list_string = '\n'

    for line in a_list:
        for key in line.keys():
            if key == 'name':
                list_string += f'{line[key]:>21}'
            elif key == 'price':
                list_string += f': £{line[key]:.2f}' + '\n'
            else:
                list_string += f': {line[key]}' + '\n'

    return list_string


# returns a formatted string of indexed list items for a given list
def format_list_indexed(a_list: list):
    '''Returns a formatted string for a list with the index and name'''
    list_string = f'ID Name\n'

    for line in a_list:
        list_string += f'{a_list.index(line) + 1:>2}'
        for key in line.keys():
            if key == 'name':
                list_string += f' {line[key]:.<18}'
            elif key == 'price':
                list_string += f': £{line[key]:.2f}' + '\n'
            else:
                list_string += f': {line[key]}' + '\n'

    return list_string


# formats a string for proper insertion in a list or dictionary
def format_string(text: str):
    '''Formats a given string for proper insertion'''
    return text.strip(' £\n\t').title()





####################
### INPUTS
####################
# takes a question to ask and returns an integer response
def get_int_input(question: str):
    '''Gets an input question and returns an integer is the input can be converted'''

    while True:
        number = input(f'{question}\n> ')
        if number.isdigit():
            return int(number)

        else:
            print('Please enter a valid number.')


# takes a question and gets an integer but only returns it
# if the integer exists within a list
def get_int_within_list(question: str, a_list:list):
    '''Gets an input question and returns an integer if it is an index within a list'''

    index = get_int_input(question) - 1

    if is_index_within_range(index, a_list):
        return 0 if (index == 0) else index

    else:
        get_int_within_list(question, a_list)


# takes a question to ask and returns a string response
def get_string_input(question: str):
    '''Gets an input question and returns a non-empty string'''

    while True:
        answer = input(f'{question}\n> ')
        if len(answer) > 0:
            return answer

        else:
            print('Invalid input.\n')


# takes a value and string and gets a user input, if the input is blank returns original value, otherwise new value
def get_an_updated_value(orig_value, type_of_item: str):
    '''Takes a string for a user input question and a value of any type. Returns the new value if the user input is not blank'''

    new_value = format_string(input(f'\nEnter new {type_of_item} or press ENTER to skip:\n> '))

    if new_value == '':
        return orig_value
    else:
        return new_value


# takes a question and returns a string if it is a key within a dictionary
def get_dictionary_key(question: str, a_dict: dict):
    '''Gets an input question and dict and returns a string if it is a key within that dictionary'''

    key = get_string_input(question)

    if is_string_a_key(key, a_dict):
        return key
    else:
        get_dictionary_key(question, a_dict)


# gets input for every item in a list and returns it as a key-value dictionary
def get_dict_of_inputs(adjective: str, type_of_item: str, key_list: list):          # UNUSED
    '''takes a list of keys and returns a dictionary of keys and values'''

    values_list = []

    for key in key_list:
        new_value = format_string(get_string_input(f'Enter {adjective} {type_of_item} {key}:'))

        if key == 'price':
            new_value = float(new_value)

        values_list.append(new_value)

    new_dict = dict(zip(key_list, values_list))

    return new_dict