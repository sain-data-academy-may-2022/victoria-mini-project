'''Module while handles all print functions within the app'''

####################
### FORMATTING AND PRINTING
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
                print(f'£{row[key]}')

            if key == 'phone':
                print(f'{row[key]}')


# print an indexed list for a provided list of dicts
def _print_indexed(data_list: list):
    '''
Requires a non-empty list of dicts.
Prints a formatted list with an index, name, price and phone if those keys exist within the list.
'''

    for index, row in enumerate(data_list, 1):
        print(f'{index:>2}', end = ' ')

        for key in row:
            if key == 'name':
                print(f'{row[key]:.>18}', end = ': ')

            if key == 'price':
                print(f'£{row[key]}')
                
            if key == 'phone':
                print(f'{row[key]}')


# print a list without indexes
def print_plain_list(item_type: str, data_list: list):
    '''prints a formatted list if data exists within that list'''

    if data_list:
        print(f'\nCurrent {item_type}:')
        _print_non_indexed(data_list)
    
    else:
        print(f'\nThere are no {item_type} currently listed.\n')


# print a list with indexes for a given item type
def print_indexed_list(item_type: str, data_list: list):
    '''prints a formatted, indexed list if data exists within that list'''

    if data_list:
        print(f'\nCurrent {item_type}:')
        _print_indexed(data_list)
    
    else:
        print(f'\nThere are no {item_type} currently listed.\n')



