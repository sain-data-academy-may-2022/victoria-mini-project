# def print_num_name_status_changeable(dict, ord_status):  # prints the name, status, and order number of a given dict
#     for index in dict:
#         if dict[index]['status'] < max(ord_status) :
#             print(f'Order: {index}, {dict[index]["customer_name"]}, {ord_status[dict[index]["status"]]}')

# def change_order_status(dict, s_list):                    ###### 
#   ###### GOOD IDEA BUT NEEDS TO HAVE THE INPUT CHECKED AGAINST THE ORDER NUMBERS WHICH CAN BE CHANGED
#     if any([True for val in dict.values() if val['status'] < max(s_list)]):
#         print_num_name_status_changeable(dict, s_list)
#         idx = get_order_num(dict)
#         print(idx)
#     else:
#         print('All orders have been completed.')



orders = {
'347': {
    'customer_name': 'Wallace and Gromit',
    'customer_address': '62 West Wallaby Street',
    'customer_phone': '07700 232 787',
    'status': 1
    }
}

order_count = 1

order_status = {
    1: 'order placed',
    2: 'being prepared',
    3: 'completed, awaiting collection',
    4: 'in-transit',
    5: 'delivered'
}


def get_order_num(dict):
    while True:
        try:
            index = input('\nEnter the order number:\n> ')
            if index in dict:
                return index
            else:
                print('\nOrder number does not exist.')
        except ValueError:
            print('\nNot a valid order number.')

def delete_order(dict):                       # deletes a dict at index from given dict
    print_num_name(dict)
    idx = get_order_num(dict)
    del dict[idx]

def advance_status(idx, dict):
    if dict[idx]['status'] < 5:
        dict[idx]['status'] += 1
        return dict
    else:
        print('This order has already been delivered.')

def change_order_status(dict, s_list):
    print_num_name_status_changeable(dict, s_list)
    idx = get_order_num(dict)
    dict = advance_status(idx, dict)
    return dict

def print_num_name_status_changeable(dict, ord_status):  # prints the name, status, and order number of a given dict
    for index in dict:
        # if dict[index]['status'] < max(ord_status) :
        print(f'Order: {index}, {dict[index]["customer_name"]}, {ord_status[dict[index]["status"]]}')


orders = change_order_status(orders, order_status)

print(orders)