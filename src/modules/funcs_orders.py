'''Module with functions to manage the orders list'''


### imports
import modules.funcs_utilities as util
from db.db import db_command, db_query

### data
status_list = ['order placed',
          'being prepared',
          'awaiting collection',
          'in-transit',
          'delivered']


### program functions

def print_order_list():
    pass

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def try_add_order():
    pass


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def try_update_order_status(connection):
    
    order_num = util.get_string_input('\nEnter the order number to be updated, or press ENTER to cancel')

    for index, status in enumerate(status_list):
        print(f'[{index}] - {status}')

    status = util.get_string_input('\nEnter the new status')

    sql_query = f'UPDATE orders SET status_id = {status} WHERE order_id = {order_num};'

    db_command(sql_query, connection)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def try_update_order_details():
    pass

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
def try_delete_order(connection):
    ''''''

    ### print order list

    order_num = util.get_string_input('Enter the order number to be deleted, or press ENTER to cancel')

    sql_query = f'DELETE FROM orders WHERE order_id = {order_num}'

    db_command(sql_query, connection)

    print(f'\nOrder number {order_num} has been deleted.')

