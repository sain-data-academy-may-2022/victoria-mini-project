'''Module with functions to manage the couriers list'''


### imports
import modules.funcs_utilities as util
from db.db import db_command, db_query

### program functions

# print the courier list (only available couriers)
def print_courier_list(couriers: list, 
                        allow_inactive: bool = False):

    available_couriers = [person for person in couriers if person['active'] == 1]
    util.print_plain_list('currently available couriers', available_couriers)

    if allow_inactive:
        inactive = [person for person in couriers if person['active'] == 0]
        util.print_plain_list('inactive couriers', inactive)


# print the courier list (only available couriers)
def print_indexed_courier_list(couriers: list, 
                                allow_inactive: bool = False,
                                return_sorted_list: bool = False):             #### NEEDS TESTING
    index = 1

    available_couriers = [person for person in couriers if person['active'] == 1]
    util.print_indexed_list('currently available couriers', available_couriers, index)

    if allow_inactive:
        index += len(available_couriers)
        inactive = [person for person in couriers if person['active'] == 0]
        util.print_indexed_list('inactive couriers', inactive, index)

    if return_sorted_list:
        return available_couriers + inactive


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# sends query to and retrieves updated courier list from courier database
def update_couriers_db(sql_query: str, connection):

    db_command(sql_query, connection)

    couriers = db_query('''SELECT * FROM couriers
                            ORDER BY active DESC''', connection)

    return couriers


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# gets an index within a sorted courier list and returns the dict at that index
def get_index_within_courier_list(couriers: list, interaction_string: str):

    sorted_list = print_indexed_courier_list(couriers, allow_inactive = True, return_sorted_list = True)
    
    _index = util.get_index_within_list(f'\nEnter the ID of the courier to be {interaction_string}d or press ENTER to cancel', sorted_list, True)

    if _index == '':
        return ''

    else:
        return sorted_list[_index]


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# gets name for a new courier, either adds new courier, updates it, or returns courier list
def try_add_courier(couriers: list, connection):
    '''Function which gets a courier name. If the name is blank, returns original courier list.
    If name already exists, gives option to update list. If name does not exist, adds courier'''
    
    name = util.get_string_input('\nEnter name of new courier or press ENTER to cancel', True)

    if name == '':
        pass

    elif not util.is_value_in_dict('name', name, couriers):

        couriers = add_new_courier(name, connection)

    else:
        print(f'\n{name} already exists in the courier menu.')
        
        choice = input('Do you want to update this person? Press ENTER to update or any other key to cancel.\n> ')

        if choice == '':

            _index = util.get_dict_index('name', name, couriers)

            couriers = update_courier(couriers[_index], couriers, connection)

    return couriers


# adds a new courier to the courier list and db
def add_new_courier(name: str, connection):
    '''Gets remaining parameters for new courier and inserts them into the database'''

    sql_query = get_new_courier_data(name)

    return update_couriers_db(sql_query, connection)


# gets remainder of courier data, returns a formatted sql query
def get_new_courier_data(name: str):

    phone = util.get_string_input('\nEnter phone number for this courier')

    return f"INSERT INTO `couriers`(`name`, `phone`) VALUES ('{name}', '{phone}'); "


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# update an existing courier
def try_update_courier(couriers: list, connection):

    cour_dict = get_index_within_courier_list(couriers, "update")

    if cour_dict == '':
        pass

    else:
        couriers = update_courier(cour_dict, couriers, connection)

    return couriers


# gets updated values for a courier within the 
def update_courier(cour: dict, couriers: list, connection):

    cour = get_updated_courier_values(cour)

    sql_query = f'''UPDATE `couriers` SET 
                `name` = "{cour["name"]}",
                `phone` = "{cour["phone"]}",
                `active` = {cour["active"]}

                WHERE
                `courier_id` = {cour["courier_id"]};'''

    couriers = update_couriers_db(sql_query, connection)

    print('\nCourier updated successfully.')
    
    return couriers


#
def get_updated_courier_values(cour):

    for key, value in cour.items():
        question = f'\nThe current {key} is {value}. Enter new {key} or press ENTER to skip'

        if key == 'courier_id':
            pass

        elif key == 'name' or key == 'phone':
            cour[key] = util.get_updated_value(value, util.get_string_input(question, allow_blank = True))

        elif key == 'active':        
            question = f'\n{"Currently listed in active menu." if value == 1 else "Not listed in active menu."} Enter (yes/no) to list this item in menu or press ENTER to skip.'

            cour[key] = util.get_updated_value(value, util.get_bool_int_input(question, allow_blank = True))

    return cour


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
def try_delete_courier(couriers: list, connection):

    prod_dict = get_index_within_courier_list(couriers, "delete")

    if prod_dict == '':
        pass

    else:
        couriers = delete_courier(prod_dict, couriers, connection)

    return couriers

#
def delete_courier(cour: dict, couriers: list, connection):

    sql_query = f'''DELETE FROM couriers WHERE `courier_id` = {cour["courier_id"]}'''

    confirm = util.get_bool_int_input(f'\nYou are about to delete {cour["name"]}. Enter (yes/no) to confirm', return_bool = True)

    if confirm:

        couriers = update_couriers_db(sql_query, connection)
        print(f'\n{cour["name"]} has been deleted.')

    return couriers

