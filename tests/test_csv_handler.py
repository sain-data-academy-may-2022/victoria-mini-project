from file_handlers import csv_handler as handler
from decimal import Decimal

def test_load_products():
    test_file = 'tests/test_data/test_csv.csv'
    expected = [{'product_id': 1, 'courier_id': '1', 'name': 'Tea', 'phone': '07700123456', 'category': 'Drinks', 'price': Decimal('1.80'), 'stock': 200, 'active': 1}]

    actual = handler.load_products(test_file)

    assert expected == actual

def test_load_products_empty():
    test_file = 'tests/test_data/test_csv_empty.csv'
    expected = []

    actual = handler.load_products(test_file)

    assert expected == actual

def test_load_couriers():
    test_file = 'tests/test_data/test_csv.csv'
    expected = [{'product_id': '1', 'courier_id': 1, 'name': 'Tea', 'phone': '07700123456', 'category': 'Drinks', 'price': '1.80', 'stock': '200', 'active': 1}]

    actual = handler.load_couriers(test_file)

    assert expected == actual

def test_load_couriers_empty():
    test_file = 'tests/test_data/test_csv_empty.csv'
    expected = []

    actual = handler.load_couriers(test_file)

    assert expected == actual