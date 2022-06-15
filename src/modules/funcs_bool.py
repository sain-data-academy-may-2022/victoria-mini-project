'''Module which handles all boolean check functions within the app'''

####################
###### BOOLS #######
####################
# check if a key-value exists in a list of dictionaries
def is_value_in_dict(key: str, value: str, list_of_dicts: list):
    '''Checks if a key-value pair exists within a list of dictionaries, returns True if found.
    Returns False if not found or if list is empty'''

    if not any(item[key] == value for item in list_of_dicts) or not list_of_dicts:
        return False

    else:
        return True


# check if a value exists in a list
def is_item_in_list(item: str, list: list):
    '''Checks if a value exists within a list, returns True if found.
    Returns False if not found or if list is empty'''

    if not (item in list) or not list:
        return False
    
    else:
        return True


# check if an index exists within a list
def is_index_within_range(index: int, a_list: list):
    '''Returns True if a given integer exists as an index within a list'''
    
    return index >= 0 and index < len(a_list)


# next function here
def func():
    pass


# next function here
def func():
    pass
