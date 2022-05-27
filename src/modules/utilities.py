'''utility functions for handling data within the app'''
#
#
#
#
#
### BOOL CHECKS
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
#
#
#
#
#
### ORDERS
#
#
#
#
#
### LISTS
# add an item to a list
def add_item_to_list(item: str, a_list: list):
    '''Adds an item to a list'''

    a_list.append(item)

    return a_list


# loop for repeatedly adding items to a list
def loop_add_items_to_list(type_of_item: str, a_list: list):
    '''Loops through adding items to a list and returns that list'''

    print_plain_list((type_of_item + 's'), a_list)

    while True:

        new_item = format_string(input(f'Enter new {type_of_item} or enter 0 to cancel:\n> '))

        if new_item == '0':
            print('')
            break

        elif len(new_item) > 0:
            a_list = add_item_to_list(new_item, a_list)
            print(f'\n{a_list[-1]} has been added.\n')

        else:
            print(f'Please enter a valid {type_of_item} name.\n')

    return a_list


# update an item within a list
def update_item_in_list(item: str, index: int, a_list: list):
    '''Replaces the list item at a specific index with a new value'''

    a_list[index] = item

    return a_list


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
            print(f'{a_list[index]} has been removed.')
            remove_item_from_list(index, a_list)

    else:
        print(format_list(a_list))

    return a_list
#
#
#
#
#
### FORMATTING AND PRINTING
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
                courier_list: list,
                status: list):
    '''prints a formatted order'''

    print(f'Order Number: {order_id}')
    print(f'\n   Name:  {order["name"]}')
    print(f'Address:  {order["address"]}')
    print(f'  Phone:  {order["phone"]}')
    try:
        print(f'Courier:  {courier_list[order["courier"]]}')
    except IndexError:
        print('Courier:  Unknown')

    print(f'\nOrder Status: {status[order["status"]]}')


# print a formatted order dictionary
def print_order_list(order_list: dict,
                    courier_list: list,
                    status: list):
    '''prints a formatted list of everything in orders'''
    print('------')
    for order in order_list:
        print_an_order(order, order_list[order], courier_list, status)
        print('------')


# prints a list with indexes starting at 0
def print_list_test(a_list):    # <--- TO DO - rename
    for index, name in enumerate(a_list):
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

    for each in a_list:
        list_string += ('\t' + each + '\n')

    return list_string


# returns a formatted string of indexed list items for a given list
def format_list_indexed(a_list: list):
    '''Returns a formatted string for a list with the index and name'''
    list_string = 'ID\tName\n'

    for each in a_list:
        index = str( a_list.index(each) + 1 )
        list_string += (index + '\t' + each + '\n')

    return list_string


# formats a string for proper insertion in a list or dictionary
def format_string(text: str):
    '''Formats a given string for proper insertion'''
    return text.strip().title()
#
#
#
#
#
### INPUTS
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

# takes a question and returns a string if it is a key within a dictionary
def get_dictionary_key(question: str, a_dict: dict):
    '''Gets an input question and dict and returns a string if it is a key within that dictionary'''

    key = get_string_input(question)

    if is_string_a_key(key, a_dict):
        return key
    else:
        get_dictionary_key(question, a_dict)
