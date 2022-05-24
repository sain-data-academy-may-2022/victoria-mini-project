import csv

def load_products():                # load products.csv file and return it as a list
    with open('data/products.csv', 'r') as file:
        csv_file = list(csv.reader(file, delimiter=','))
        return csv_file[0]

def write_products(list):           # takes list and writes out products.csv file
    with open('data/products.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(list)