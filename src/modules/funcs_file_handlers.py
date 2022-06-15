from file_handlers.csv_handler import load_products, load_couriers
from db.db import get_connection, close_connection, db_query


### PRODUCTS
# attempts to load products from database first, then tries local storage, otherwise throws error and returns empty list
def get_products():

    products = []

    # try to load from database
    try:
        connection = get_connection()
        products = db_query('''SELECT * FROM products
                            ORDER BY CASE
                            WHEN category = "Drinks" THEN 1
                            WHEN category = "Snacks" THEN 2
                            WHEN category = "Base" THEN 3
                            ELSE 4 END''', connection)
        close_connection(connection)
    
    # if exception, then try to load from csv file
    except:
        try:
            csv_file = load_products('data/products.csv')

            drinks = [item for item in csv_file if item['category'] == 'Drinks']
            snacks = [item for item in csv_file if item['category'] == 'Snacks']
            base = [item for item in csv_file if item['category'] == 'Base']
            tops = [item for item in csv_file if item['category'] == 'Toppings']

            products = drinks + snacks + base + tops

    # if cannot load from either, inform user
        except Exception as e:
            print(f'Unable to load products data from database or local storage.\nError: {e}')

    return products


### COURIERS
# attempts to load couriers from database first, then tries local storage, otherwise throws error and returns empty list
def get_couriers():

    couriers = []

    # try to load from database
    try:
        connection = get_connection()
        couriers = db_query('''SELECT * FROM couriers''', connection)
        close_connection(connection)
    
    # if exception, then try to load from csv file
    except:
        try:
            couriers = load_couriers('data/couriers.csv')

    # if cannot load from either, inform user
        except Exception as e:
            print(f'Unable to load couriers data from database or local storage.\nError: {e}')

    return couriers

