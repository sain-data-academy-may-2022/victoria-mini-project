'''module which handles the loading and saving of csv files related to the app'''

import csv

# load products.csv file and return it as a list
def load_products():
    '''load products.csv file and return it as a list'''
    with open('data/products.csv', 'r', encoding='utf-8') as file:
        csv_file = list(csv.reader(file, delimiter=','))
        return csv_file[0]

# receives a list and writes out products.csv file
def write_products(a_list):
    '''write out a list in a products.csv file'''
    with open('data/products.csv', 'w', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(a_list)
        print('Products list saved...')

# load couriers.csv file and return it as a list
def load_couriers():
    '''load couriers.csv file and return it as a list'''
    with open('data/couriers.csv', 'r', encoding='utf-8') as file:
        csv_file = list(csv.reader(file, delimiter=','))
        return csv_file[0]

# receives a list and writes out products.csv file
def write_couriers(a_list):
    '''write out a list in a couriers.csv file'''
    with open('data/couriers.csv', 'w', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(a_list)
        print('Courier list saved...')
