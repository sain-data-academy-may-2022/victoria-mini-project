import json

def load_orders():                  # load orders.json and return it as a dict
    with open('data/orders.json', 'r') as file:
        json_order = json.load(file)
        return json_order

def write_orders(dict):             # takes dict and writes out orders.json file
    with open('data/orders.json', 'w') as file:
        json.dump(dict, file, indent=4)