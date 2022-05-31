import csv

orders = [{
    'number': '1',
    'name': 'Sherlock Holmes',
    'address': '221b Baker Street',
    'phone': '07700 123 456',
    'courier': 1,
    'status': 4,
    'items': [1, 2, 5]
    },
    {
    'number': '2',
    'name': 'Phileas Fogg',
    'address': '7 Savile Row',
    'phone': '07700 987 321',
    'courier': 1,
    'status': 3,
    'items': [2, 2, 3]
    },
    {
    'number': '3',
    'name': 'Wallace and Gromit',
    'address': '62 West Wallaby Street',
    'phone': '07700 444 456',
    'courier': 8,
    'status': 2,
    'items': [1, 1]
    },
    {
    'number': '4',
    'name': 'Keith and Jim',
    'address': 'The Moon',
    'phone': '0800 00 1066',
    'courier': 1,
    'status': 0,
    'items': [5, 5, 5, 5, 5, 5]
    }
    ]

def load_orders():
    order_list = []
    with open('data/orders.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            # print(int(row['status']))
            row['courier'] = int(row['courier'])
            row['status'] = int(row['status'])
            order_list.append(row)

    return order_list

def write_orders(order_list):
    with open('data/orders.csv', 'w') as file:
        fieldnames = ['number', 'name', 'address', 'phone', 'courier', 'status', 'items']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in order_list:
            writer.writerow(order)
        print('Order list saved...')

# orders = load_orders()
write_orders(orders)
print(orders)

orders = load_orders()