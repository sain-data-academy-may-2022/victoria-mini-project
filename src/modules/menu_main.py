'''Module with functions to manage the main menu'''


### imports 
import modules.clear_screen as cs
import modules.menu_products as m_p
import modules.menu_couriers as m_c
import modules.menu_orders as m_o


### menu functions
# print the main menu options
def print_main_menu():
    '''Prints the main menu options'''
    
    cs.clear_screen()
    print('''\nWelcome to the 
 ___                                  ___                                              ___      
(   )                                (   )                                            (   )     
 | |.-. ___ .-.    .--.    .---.   .-.| |___  ___    .--.  ___ .-.     ___ .-.   .--.  | |_     
 | /   (   )   \  /    \  / .-, \ /   \ (   )(   )  /    \(   )   \   (   )   \ /    \(   __)   
 |  .-. | ' .-. ;|  .-. ;(__) ; ||  .-. || |  | |  |  .-. ;| ' .-. ;   |  .-. .|  .-. ;| |      
 | |  | |  / (___)  | | |  .'`  || |  | || |  | |  | |  | ||  / (___)  | |  | || |  | || | ___  
 | |  | | |      |  |/  | / .'| || |  | || '  | |  | |  | || |         | |  | || |  | || |(   ) 
 | |  | | |      |  ' _.'| /  | || |  | |'  `-' |  | |  | || |         | |  | || |  | || | | |  
 | '  | | |      |  .'.-.; |  ; || '  | | `.__. |  | '  | || |         | |  | || '  | || ' | |  
 ' `-' ;| |      '  `-' /' `-'  |' `-'  / ___ | |  '  `-' /| |         | |  | |'  `-' /' `-' ;  
  `.__.(___)      `.__.' `.__.'_. `.__,' (   )' |   `.__.'(___)       (___)(___)`.__.'  `.__.   
                                          ; `-' '                                               
                                           .__.'                                                
                                                    Breakfast Bar!



    [1] - Product Management
    [2] - Courier Management
    [3] - Order Management
    More options coming soon...

    [0] - Exit Application''')


# controls main menu input and selection
def main_menu_choice(products: list, couriers: list, orders: list, connection):

    print_main_menu()


    choice = input('\nPlease select an option:\n> ')
    running = True

    if choice == '0':
        running = False
        return running, products, couriers, orders

    # enter product management menu
    elif choice == '1':
        products = m_p.product_menu(products, connection)

    # enter courier management menu
    elif choice == '2':
        couriers = m_c.courier_menu(couriers, connection)

    # enter order management menu
    elif choice == '3':
        orders = m_o.order_menu(products, couriers, orders, connection)

    # clear screen and reprint main menu options
    elif choice == '':
        print_main_menu()

    # handle incorrect input
    else: 
        print_main_menu()
        print('Invalid selection. Please select a valid menu option.')

    return running, products, couriers, orders


# controls main menu loop
def main_menu(products: list, couriers: list, orders: list, connection):

    running = True
    
    while running:
        
        running, products, couriers, orders = main_menu_choice(products, couriers, orders, connection)

    cs.clear_screen()
    return orders

