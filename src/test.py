import csv

test = []

items = [{  'name': 'Tea',
            'price': 1.80},
        {   'name': 'Coffee',
            'price': 2.20},
        {   'name': 'Waffles',
            'price': 4.50}
        ]

with open('data/products-2.csv', 'w') as items_file:
    for item in items:
      items_file.write(item + '\n')


print(items)