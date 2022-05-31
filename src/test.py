### imports
from hashlib import new
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products, \
                                            load_orders, write_orders
from file_handlers.json_handler import load_orders, write_orders
# from modules.main_menu import main_menu

# load files
products = load_products()
# couriers = load_couriers()
# orders = load_orders()

# print(products)
# print(couriers)
# print(orders)

# a_string = ''
# for each in orders:
#     print(f'Order Number: {each}')
#     for line in orders[each]:
#         print(f'{line.capitalize():>12}: {orders[each][line]}')


def add_item_to_list(type_of_item: str, keys: list, a_list: list):
    
    running = True

    for key in keys:
        while running:
            value = input(f'Enter new {type_of_item} {key} or enter 0 to cancel:\n> ')

# def loop_add_items_to_list(type_of_item: str, keys: list, a_list: list):
#     '''Loops through adding items to a list and returns that list'''

#     looping = True

#     # print_plain_list((type_of_item + 's'), a_list)

#     while looping:
#         new_item = {}

#         for key in keys:            

#             elif len(value) > 0:

#                 if key == 'price':
#                     new_item[key] = float(value)

#                 else:
#                     new_item[key] = value

#             else:
#                 print(f'Please enter a valid {type_of_item} {key}.\n')

#         print(new_item)
#         get_input = input(f'\nPress ENTER to add item to {type_of_item} list or 0 to cancel:\n> ')
#         if get_input == '':
#             a_list.append(new_item)
#             print(f'{new_item["name"]}')

#     else:
#         return a_list

# print(products)


# takes a question to ask and returns a string response
def get_string_input(question: str):
    '''Gets an input question and returns a non-empty string'''

    while True:
        answer = input(f'{question}\n> ')
        if len(answer) > 0:
            return answer

        else:
            print('Invalid input.\n')

def loop_add_items_to_list(type_of_item: str, item_keys: list, a_list: list):

    ## print plain list

    running = True

    new_item = {}

    while running:
        for key in item_keys:
            value = get_string_input(f'\nEnter new {type_of_item} {key} or enter 0 to cancel:')

            if value == '0':
                running = False
                break

            else:
                if key == 'price':
                    new_item[key] = float(value)

                else:
                    new_item[key] = value
            
        else:
            a_list.append(new_item)
            print(f'{a_list[-1]["name"]} has been added to the {type_of_item} list.')












loop_add_items_to_list('product', ['name', 'price'], products)