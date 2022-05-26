'''utility functions for handling different lists within the app'''









# 1
# 2
# 3
# 4
# 5
### BOOL CHECKS
# checks if a list has items or not
def check_list_has_items(a_list):
    '''If a list has items, returns True. Otherwise returns False.'''

    if a_list:
        return True

    else:
        return False


# checks if an index exists within a list
def is_index_within_range(index: int, a_list: list):
    '''Returns True if a given integer exists as an index within a list'''

    return index >= 0 and index < len(a_list)
# 1
# 2
# 3
# 4
# 5
### LISTS
# add an item to a list
def add_item_to_list(item: str, a_list: list):
    '''Adds an item to a list'''

    a_list.append(item)

    return a_list


# loop for repeatedly adding items to a list
def loop_add_items_to_list(type_of_item: str, a_list: list):
    '''Loops through adding items to a list and returns that list'''

    while True:
        print(format_list(a_list))

        new_item = format_string(input(f'Enter new {type_of_item} or enter 0 to cancel:\n> '))

        if new_item == '0':
            break

        elif len(new_item) > 0:
            a_list = add_item_to_list(new_item, a_list)
            print(f'\n{a_list[-1]} has been added.')

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


# loop for repeatedly removing items from a list
def loop_remove_items_from_list(type_of_item: str, a_list: list):
    '''Loops through removing items from a list and returns that list'''

    while a_list:
        print(a_list)
        a_list.pop(0)

    else:
        print(format_list(a_list))
    
    return a_list

# 1
# 2
# 3
# 4
# 5
### FORMATTING AND PRINTING
# print a list without indexes
def print_plain_list(item_type: str, a_list: list):
    '''prints a plain list'''
    if a_list:
        print(f'\nCurrent {item_type}:', end='')
        print(format_list(a_list)[:-1])
    else:
        print(f'\nThere are no {item_type} currently listed.')


# print a list with indexes
def print_indexed_list(item_type: str, a_list: list):
    '''prints a plain list'''
    if a_list:
        print('\n' + format_list_indexed(a_list))
    else:
        print(f'\nThere are no {item_type} currently listed.')


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
# 1
# 2
# 3
# 4
# 5
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





## TESTS
