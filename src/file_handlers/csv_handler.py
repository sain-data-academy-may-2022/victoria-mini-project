'''Module which handles the loading and saving of csv files'''

import csv
from decimal import Decimal

# load products.csv file and return it as a list
def load_products(file_path):
    '''load products.csv file and return it as a list'''
    product_list = []
    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            row['product_id'] = int(row['product_id'])
            row['price'] = Decimal(row['price'])
            row['stock'] = int(row['stock'])
            row['active'] = int(row['active'])
            product_list.append(row)

    return product_list

# receives a list and writes out products.csv file
def write_products(product_list):
    '''write out a list in a products.csv file'''
    with open('data/products.csv', 'w') as file:
        fieldnames = ['product_id', 'name', 'category', 'price', 'stock', 'active']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in product_list:
            writer.writerow(product)
        print('Product list saved...')

# load couriers.csv file and return it as a list
def load_couriers(file_path):
    '''load couriers.csv file and return it as a list'''
    courier_list = []
    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            row['courier_id'] = int(row['courier_id'])
            row['active'] = int(row['active'])
            courier_list.append(row)

    return courier_list

# receives a list and writes out products.csv file
def write_couriers(courier_list):
    '''write out a list in a couriers.csv file'''
    with open('data/couriers.csv', 'w') as file:
        fieldnames = ['courier_id', 'name', 'phone', 'active']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for courier in courier_list:
            writer.writerow(courier)
        print('Courier list saved...')

# load orders.csv file and return it as a list
def load_orders():
    '''load orders.csv file and return it as a list'''
    order_list = []
    with open('data/orders.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            row['courier'] = int(row['courier'])
            row['status'] = int(row['status'])
            order_list.append(row)

    return order_list

# receives a list and writes out orders.csv file
def write_orders(order_list):
    '''write out a list in an orders.csv file'''
    with open('data/orders.csv', 'w') as file:
        fieldnames = ['number', 'name', 'address', 'phone', 'courier', 'status', 'items']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in order_list:
            writer.writerow(order)
        print('Order list saved...')
