'''Module which handles all boolean check functions within the app'''

####################
###### BOOLS #######
####################
# check if a key-value exists in a list of dictionaries
def is_value_in_list(key, value, list_of_dicts):
    '''Checks if a key-value pair exists within a list of dictionaries, returns True if found.
    Returns False if not found or if list is empty'''

    if not any(item[key] == value for item in list_of_dicts) or not list_of_dicts:
        return False

    else:
        return True


# next function here
def func():
    pass


# next function here
def func():
    pass


# next function here
def func():
    pass
