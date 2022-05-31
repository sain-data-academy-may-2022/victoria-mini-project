### imports
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


# for index, product in enumerate(products, 1):
#     print(f'{index:>2}] {product["name"]:.<20}: £{product["price"]:.2f}')

# returns a formatted string of list items for a given list
def format_list(a_list: list):
    '''Returns a formatted string for a given list'''

    list_string = '\n'

    for line in a_list:
        for each in line.values():
            list_string += (str(each) + '  ')
        list_string += ('\n')

        # list_string += ('\t' + each + '\n')

    return list_string

print(format_list(products))

# a_string = ''
# for each in orders:
#     print(f'Order Number: {each}')
#     for line in orders[each]:
#         print(f'{line.capitalize():>12}: {orders[each][line]}')
