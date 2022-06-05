### imports
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products, \
                                            load_orders, write_orders
from file_handlers.json_handler import load_orders, write_orders
# # from modules.main_menu import main_menu
import modules.utilities as util


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

def get_products_for_order(product_list):
    ''''''
    print('\n', util.format_list_indexed(product_list))

    running = True

    items = []
    
    while running:
        new_item = util.get_int_input('\nEnter the ID of the product, or 0 to cancel:')

        if new_item == 0:
            print('\nCurrent items:')

            for each in items:
                print(f'\t{product_list[each]["name"]}')

            loop = input('\nPress ENTER to confirm these items, or 0 to add more:\n> ')
            
            if loop == '':
                running = False

        elif util.is_index_within_range(new_item - 1, product_list):
            items.append(new_item - 1)
            print(f'{product_list[new_item - 1]["name"]} has been added.')

    return items

        

order_items = get_products_for_order(products)

print(order_items)