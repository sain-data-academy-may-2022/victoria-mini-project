'''Module which handles all utility/generic functions'''

### PRINTING
### INPUTS
### BOOLS
### UTILITIES




####################
##### PRINTING #####
####################
# print a non-indexed list for a provided list of dicts
def _print_non_indexed(data_list: list):
    '''
Requires a non-empty list of dicts.
Prints a formatted list with the name, price and phone if those keys exist within the list.
'''

    for row in data_list:
        for key in row:
            if key == 'name':
                print(f'{row[key]:>21}', end = ': ')

            if key == 'price':
                print(f'£{row[key]:.2f}')

            if key == 'phone':
                print(f'{row[key]}')


# print an indexed list for a provided list of dicts
def _print_indexed(data_list: list, start: int = 1):
    '''
Requires a non-empty list of dicts.
Prints a formatted list with an index, name, price and phone if those keys exist within the list.
'''

    for index, row in enumerate(data_list, start):
        print(f'{index:>2}', end = ' ')

        for key in row:
            if key == 'name':
                print(f'{row[key]:.>18}', end = ': ')

            if key == 'price':
                print(f'£{row[key]:>4.2f}', end = ' ')
                
            if key == 'stock':
                print(f'{row[key]:>5}')

            if key == 'phone':
                print(f'{row[key]}')


# print a list without indexes
def print_plain_list(item_type: str, data_list: list):
    '''prints a formatted list if data exists within that list'''

    if data_list:
        print(f'\n{item_type.capitalize()}:')
        _print_non_indexed(data_list)
    
    else:
        print(f'\nThere are no {item_type} listed.')


# print a list with indexes for a given item type
def print_indexed_list(item_type: str, data_list: list, start_index: str = 1):
    '''prints a formatted, indexed list if data exists within that list'''

    if data_list:
        print(f'\n{item_type.capitalize()}:')
        _print_indexed(data_list, start_index)
    
    else:
        print(f'\nThere are no {item_type} listed.')





####################
###### INPUTS ######
####################
# formats a string for proper insertion
def _format_string(text: str):
    '''Formats a given string for proper insertion'''
    return text.lstrip(' £\n\t\'\"\`;').rstrip(' £\n\t\'\"\`;-').title()


# takes a question to ask the user and returns a 1 or 0 
def get_bool_int_input(question: str, allow_blank: bool = False, return_bool: bool = False):
    '''Gets an input question and returns a 1 or a 0 as substitute for a boolean True or False.
    If allow_blank = True, returns an empty string'''

    answer = _format_string(input(f'{question}:\n> '))

    if answer == '' and allow_blank:
        return ''

    elif answer == 'Y' or answer == 'Yes' or answer == '1':
        if return_bool:
            return True
        else:
            return 1

    elif answer == 'N' or answer == 'No' or answer == '0':
        if return_bool:
            return False
        else:
            return 0

    else: 
        print('Please enter a valid answer (yes/no).')
        return get_bool_int_input(question, allow_blank, return_bool)


# takes a question to ask the user and returns an integer response, allows blank responses if set
def get_int_input(question: str, allow_blank: bool = False, allow_zero: bool = False):
    '''Gets an input question and returns the exact integer if the input can be converted, the number is positive, and allow_blank = False.
    Otherwise returns an empty string if allow_blank is True'''

    valid_num = False

    while not valid_num:
        number = _format_string(input(f'{question}:\n> '))
        try:
            number = int(number)

            if (allow_zero and number == 0) or number > 0:
                valid_num = True

            else:
                raise(ValueError)

        except ValueError:
            if allow_blank and number == '':
                return ''
            else:
                print('Please enter a valid number.')
                return get_int_input(question, allow_blank, allow_zero)
            
    return number


# takes a question to ask the user and returns a float response, allows blank responses if set
def get_positive_float_input(question: str, allow_blank: bool = False):
    '''Gets an input question and returns the exact float if the input can be converted, the number is positive, and allow_blank = False.
    Otherwise returns an empty string if allow_blank is True'''

    valid_num = False

    while not valid_num:
        number = _format_string(input(f'{question}:\n> '))
        try:
            number = float(number)

            if number > 0:
                valid_num = True

            else:
                raise(ValueError)

        except ValueError:
            if allow_blank and number == '':
                return ''
            else:
                print('Please enter a valid number.')
                return get_positive_float_input(question, allow_blank)
            
    return round(number, 2)


# takes a question to ask and returns a string response, allows blank responses if set
def get_string_input(question: str, allow_blank: bool = False):
    '''Gets an input question and returns a non-empty string if allow_blank = False
    and allows an empty string if allow_blank = True'''

    answer = _format_string(input(f'{question}:\n> '))
    
    if len(answer) > 0 or (answer == '' and allow_blank):
        return answer
    
    elif answer == '' and not allow_blank:
        print('Empty answers not allowed.')
        return get_string_input(question, allow_blank)


# gets a string input and checks if it is exists within a list, returns the input is it does
def get_input_within_list(question: str, list_of_values: list, allow_blank: bool = False):
    '''Takes an input question and returns a string value only if it exists within a list
    Allows return of an empty string if allow_blank = True'''
    
    answer = get_string_input(question, allow_blank)

    if is_item_in_list(answer, list_of_values) or (answer == '' and allow_blank):
        return answer

    else:
        print('Please enter a valid option.')
        return get_input_within_list(question, list_of_values, allow_blank)


# gets an integer input and checks if it is exists as an index within a list, returns the index is it does
def get_index_within_list(question: str, list_of_values: list, allow_blank: bool = False):
    '''Takes an input question and returns an integer value only if it exists as an index in a list
    Allows return of an empty string if allow_blank = True'''
    
    answer = get_int_input(question, allow_blank)

    if  answer == '' and allow_blank:
        return ''

    elif is_index_within_range(answer - 1, list_of_values):
        return answer - 1

    else:
        print('Please enter a valid option.')
        return get_index_within_list(question, list_of_values, allow_blank)


# takes a value and an input function from input section and will return the result if the input is not blank, otherwise returns old value
def get_updated_value(value, input_function):

    new_value = input_function

    if new_value == '':
        return value
    else:
        return new_value








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





####################
#### UTILITIES #####
####################
### LISTS
# get index for a dict based on the value of a key within that dict
def get_dict_index(key: str, value: str, a_list: list):

    return next(index for (index, d) in enumerate(a_list) if d[key] == value)

# add an item to a list
def add_item_to_list(item: dict, a_list: list):
    '''Adds an item to a list'''

    a_list.append(item)

    return a_list

# update a specific item within a list
def update_item_in_list(item: dict, index: int, a_list: list):
    '''Replaces the list item at a specific index with a new value
    Requires that an index provided is within range'''

    try:
        a_list[index] = item

    except IndexError as e:
        pass
    
    return a_list





