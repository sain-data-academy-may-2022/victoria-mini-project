### imports
from modules.clear_screen import clear_screen
from file_handlers.csv_handler import load_couriers, write_couriers, \
                                        load_products, write_products
from file_handlers.json_handler import load_orders, write_orders
import modules.main_menu as mm
import modules.product_management as pm
import modules.courier_management as cm
import modules.order_management as om

### program
# load files and set order counter
products = load_products()
couriers = load_couriers()
orders = load_orders()
order_count = int(max(orders.keys())) + 1

# main program loop
while True:
    clear_screen()
    mm.print_main_menu()
    print('\nPlease select an option:')

    user_input = input('> ')

    # close program and write out files
    if user_input == '0':
        # write_products()
        # write_couriers()
        # write_orders()
        break

    # product management menu
    elif user_input == '1':
        clear_screen()
        pm.print_product_options()
        print('Please select an option:')

        while True:
            user_input = input('> ')

            if user_input == '0':
                break

            # print product list
            elif user_input == '1':
                clear_screen()
                pm.print_product_options()
                print('\n[1] - Display Product List\n')

                print(pm.format_products_list(products))

                print('Please select another option:')

            # create new product
            elif user_input == '2':
                clear_screen()
                pm.print_product_options()
                print('\n[2] - Add a New Product\n')

                while True:
                    new_prod = input('Enter new product or enter 0 to cancel:\n> ')
                    if new_prod == '0':
                        break

                    else:
                        print('Please enter a valid product name.')
                    print(id(products))

                    # if new_prod == '0':
                    #     pass
                    # else:
                    #     pm.add_product(new_prod, products)

                print('Please select another option:')

            # update existing product
            elif user_input == '3':
                clear_screen()
                pm.print_product_options()
                print('\n[3] - Update Existing Product\n')

                print(pm.format_products_indexed(products))

                print('Please select another option:')

            # delete existing product
            elif user_input == '4':
                clear_screen()
                pm.print_product_options()
                print('\n[4] - Delete a Product\n')



                products = pm.remove_product(1, products)
                print(pm.format_products_indexed(products))

                print('Please select another option:')

            # handle invalid input
            else:
                clear_screen()
                pm.print_product_options()

                print('\nInvalid input. Please select an option:')

    # courier management menu
    elif user_input == '2':
        clear_screen()
        cm.print_courier_options()
        print('\nPlease select an option:')

        while True:
            user_input = input('> ')

            if user_input == '0':
                break

            # print courier list
            elif user_input == '1':
                pass

            # create new courier
            elif user_input == '2':
                pass

            # update existing courier
            elif user_input == '3':
                pass

            # delete existing courier
            elif user_input == '4':
                pass

            # handle invalid input
            else:
                clear_screen()
                cm.print_courier_options()

                print('\nInvalid input. Please select an option:')


    # order management menu
    elif user_input == '3':
        clear_screen()
        # om.print_order_options()
        print('\nPlease select an option:')

        while True:
            user_input = input('> ')

            if user_input == '0':
                break

            # print order list
            elif user_input == '1':
                pass

            #
            elif user_input == '2':
                pass

            #
            elif user_input == '3':
                pass

            #
            elif user_input == '4':
                pass

            #
            elif user_input == '5':
                pass

            # handle invalid input
            else:
                clear_screen()
                # om.print_product_options()

                print('\nInvalid input. Please select an option:')

    # handle invalid input
    else:
        clear_screen()
        mm.print_main_menu()

        print('\nInvalid input. Please select an option:')
