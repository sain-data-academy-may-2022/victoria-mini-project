'''utility functions for handling different lists within the app'''


# checks if a list has items or not
def check_list_has_items(a_list):
    '''If a list has items, returns True. Otherwise returns False.'''
    if a_list:
        return True

    else:
        return False


# get an input and check if it is within the range of a list
def get_index(a_list):
    '''Get user input for an index within a given list'''
    while True:
        try:
            index = int(input('Please enter the ID, or enter 0 to cancel:\n> '))
            if index == 0:
                break
            elif index > 0 and index <= len(a_list):
                return index
            else:
                print('Please enter a valid ID.\n')
        except ValueError:
            print('Please enter a valid ID.\n')


# returns a formatted string of list items for a given list
def format_list(a_list):
    '''Returns a formatted string for a given list'''
    list_string = ''

    for each in a_list:
        list_string += ('\t' + each + '\n')

    return list_string


# returns a formatted string of indexed list items for a given list
def format_list_indexed(a_list):
    '''Returns a formatted string for a list with the index and name'''
    list_string = 'ID\tName\n'

    for each in a_list:
        index = str( a_list.index(each) + 1 )
        list_string += (index + '\t' + each + '\n')

    return list_string


# formats a string for proper insertion in a list or dictionary
def format_string(text):
    '''Formats a given string for proper insertion'''
    return text.strip().capitalize()


# add a product to the products list
def add_item_to_list(item, a_list):
    '''Adds an item to a list'''
    a_list.append(item)
    return a_list


# replaces an item at a specific index
def update_item_in_list(index, item, a_list):
    '''Replaces the item at a specified index in a list'''
    a_list[index - 1] = item
    return a_list


# remove a product from a products list             ### CHANGE???
def remove_item_from_list(index, a_list):
    '''Remove the item at a given index from a product list'''
    return a_list.pop(index - 1)
    # return a_list
