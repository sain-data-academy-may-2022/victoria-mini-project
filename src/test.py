order_count = 1

orders = {
123: {
    'customer_name': 'Sherlock Holmes',
    'customer_address': '221b Baker Street',
    'customer_phone': '07700 123 456',
    'status': 5
    },
258: {
    'customer_name': 'Phileas Fogg',
    'customer_address': '7 Savile Row',
    'customer_phone': '07700 987 321',
    'status': 2
    },
347: {
    'customer_name': 'Wallace and Gromit',
    'customer_address': '62 West Wallaby Street',
    'customer_phone': '07700 232 787',
    'status': 1
    }
}

order_status = {
    1: 'order placed',
    2: 'being prepared',
    3: 'order completed, awaiting collection',
    4: 'order in-transit',
    5: 'order delivered'
}

products = []

def print_order_list(orders, s_list):      # print a given dict of dictionaries
    print('------')
    for index in orders:
        print_order(index, orders[index], s_list)
        print('------')

def print_order(idx, ord, ord_status):     # prints a given dictionary in a specified format
    print(f'''Order Number: {idx}

   Name:  {ord['customer_name']}
Address:  {ord['customer_address']}
  Phone:  {ord['customer_phone']}

Order Status: {ord_status[ord['status']]}''')

def add_order(count, dict):                # takes a list of dicts and an order count, returns new order count
    new_order = {}
    new_order['customer_name'] = input('\nPlease enter the customer\'s name:\n> ').strip()
    new_order['customer_address'] = input('\nPlease enter the customer\'s address:\n> ').strip()
    new_order['customer_phone'] = input('\nPlease enter the customer\'s phone number:\n> ').strip()
    new_order['status'] = 1

    dict[count] = new_order
    count += 1

    return count

def delete_order(idx, dict):
    del dict[idx]

def print_order_and_name(dict):
    for index in dict:
        print(f'Order: {index}, Name: {dict[index]["customer_name"]}')

def get_order_num(dict):
    print_order_and_name(dict)
    while True:
        try:
            index = int(input('\nEnter the order number:\n> '))
            if index in dict:
                return index
            else:
                print('\nOrder number does not exist.')
        except ValueError:
            print('\nNot a valid order number.')

def delete_order(dict):                    # deletes a dict at index from given dict
    idx = get_order_num(dict)
    del dict[idx]


import csv

def load_products():
    with open("data/products.csv", 'r') as file:
        csv_file = list(csv.reader(file, delimiter=','))
        return csv_file[0]
            

products = load_products()
print(products)