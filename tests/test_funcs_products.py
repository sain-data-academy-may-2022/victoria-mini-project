import modules.funcs_products as prod
from unittest.mock import Mock, patch, call

### PRINT_PRODUCT_LIST
@patch('modules.funcs_utilities.print_plain_list')
def test_print_product_list(mock_print_list):
    td = []

    prod.print_product_list(td)

    assert mock_print_list.call_count == 5

@patch('modules.funcs_utilities.print_plain_list')
def test_print_product_list_filtered(mock_print_list):
    td = [
        {'name': 'Test', 'category': 'Drinks', 'active': 1, 'stock': 1},
        {'name': 'Test2', 'category': 'Drinks', 'active': 0, 'stock': 0},
    ]

    prod.print_product_list(td)

    mock_print_list.assert_has_calls([
        call('currently available drinks', [{'name': 'Test', 'category': 'Drinks', 'active': 1, 'stock': 1}]),
        call('currently available snacks', []),
        call('currently available bases', []),
        call('currently available toppings', []),
        call('items currently out of stock', [])
        ])
    assert mock_print_list.call_count == 5

@patch('modules.funcs_utilities.print_plain_list')
def test_print_product_list_filtered_all(mock_print_list):
    td = [
        {'name': 'Test1', 'category': 'Drinks', 'active': 1, 'stock': 1},
        {'name': 'Test2', 'category': 'Drinks', 'active': 0, 'stock': 1},
        {'name': 'Test3', 'category': 'Snacks', 'active': 1, 'stock': 1},
        {'name': 'Test4', 'category': 'Snacks', 'active': 0, 'stock': 1},
        {'name': 'Test5', 'category': 'Base', 'active': 1, 'stock': 1},
        {'name': 'Test6', 'category': 'Base', 'active': 0, 'stock': 1},
        {'name': 'Test7', 'category': 'Toppings', 'active': 1, 'stock': 1},
        {'name': 'Test8', 'category': 'Toppings', 'active': 0, 'stock': 1},
    ]

    prod.print_product_list(td)

    mock_print_list.assert_has_calls([
        call('currently available drinks', [{'name': 'Test1', 'category': 'Drinks', 'active': 1, 'stock': 1}]),
        call('currently available snacks', [{'name': 'Test3', 'category': 'Snacks', 'active': 1, 'stock': 1}]),
        call('currently available bases', [{'name': 'Test5', 'category': 'Base', 'active': 1, 'stock': 1}]),
        call('currently available toppings', [{'name': 'Test7', 'category': 'Toppings', 'active': 1, 'stock': 1}]),
        call('items currently out of stock', [])
        ])
    assert mock_print_list.call_count == 5

@patch('modules.funcs_utilities.print_plain_list')
def test_print_product_list_filtered_oos(mock_print_list):
    td = [
        {'name': 'Test1', 'category': 'Drinks', 'active': 1, 'stock': 1},
        {'name': 'Test2', 'category': 'Drinks', 'active': 0, 'stock': 1},
        {'name': 'Test3', 'category': 'Snacks', 'active': 1, 'stock': 1},
        {'name': 'Test4', 'category': 'Snacks', 'active': 0, 'stock': 1},
        {'name': 'Test5', 'category': 'Base', 'active': 1, 'stock': 0},
        {'name': 'Test6', 'category': 'Base', 'active': 0, 'stock': 1},
        {'name': 'Test7', 'category': 'Toppings', 'active': 1, 'stock': 1},
        {'name': 'Test8', 'category': 'Toppings', 'active': 0, 'stock': 1},
    ]

    prod.print_product_list(td)

    mock_print_list.assert_has_calls([
        call('currently available drinks', [{'name': 'Test1', 'category': 'Drinks', 'active': 1, 'stock': 1}]),
        call('currently available snacks', [{'name': 'Test3', 'category': 'Snacks', 'active': 1, 'stock': 1}]),
        call('currently available bases', []),
        call('currently available toppings', [{'name': 'Test7', 'category': 'Toppings', 'active': 1, 'stock': 1}]),
        call('items currently out of stock', [{'name': 'Test5', 'category': 'Base', 'active': 1, 'stock': 0}])
        ])
    assert mock_print_list.call_count == 5

@patch('modules.funcs_utilities.print_plain_list')
def test_print_product_list_filtered_oos_unavailable(mock_print_list):
    td = [
        {'name': 'Test1', 'category': 'Drinks', 'active': 1, 'stock': 1},
        {'name': 'Test2', 'category': 'Drinks', 'active': 0, 'stock': 1},
        {'name': 'Test3', 'category': 'Snacks', 'active': 1, 'stock': 1},
        {'name': 'Test5', 'category': 'Base', 'active': 1, 'stock': 0},
        {'name': 'Test7', 'category': 'Toppings', 'active': 1, 'stock': 1},
    ]

    prod.print_product_list(td, allow_inactive = True)

    mock_print_list.assert_has_calls([
        call('currently available drinks', [{'name': 'Test1', 'category': 'Drinks', 'active': 1, 'stock': 1}]),
        call('currently available snacks', [{'name': 'Test3', 'category': 'Snacks', 'active': 1, 'stock': 1}]),
        call('currently available bases', []),
        call('currently available toppings', [{'name': 'Test7', 'category': 'Toppings', 'active': 1, 'stock': 1}]),
        call('items currently out of stock', [{'name': 'Test5', 'category': 'Base', 'active': 1, 'stock': 0}]),
        call('inactive menu items', [{'name': 'Test2', 'category': 'Drinks', 'active': 0, 'stock': 1}, ])
        ])
    assert mock_print_list.call_count == 6



### TRY_ADD_NEW_PRODUCT
@patch('builtins.input', side_effect = ['example'])
@patch('modules.funcs_products.add_new_product')
@patch('modules.funcs_products.update_product')
def test_try_add_new_product___path_1___add_unknown_item(mock_update, mock_add, mock_input):
    test_prod = [{'name': 'test'}, {'name': 'sample'}]
    mock_cxn = Mock()
    mock_update.return_value = [{'name': 'test'}, {'name': 'example'}]
    mock_add.return_value = [{'name': 'test'}, {'name': 'sample'}, {'name': 'example'}]
    expected = [{'name': 'test'}, {'name': 'sample'}, {'name': 'example'}]

    actual = prod.try_add_product(test_prod, mock_cxn)

    assert expected == actual
    assert mock_update.call_count == 0
    assert mock_add.call_count == 1

@patch('builtins.input', side_effect = [''])
@patch('modules.funcs_products.add_new_product')
@patch('modules.funcs_products.update_product')
def test_try_add_new_product___path_2___blank_input(mock_update, mock_add, mock_input):
    test_prod = [{'name': 'test'}, {'name': 'sample'}]
    mock_cxn = Mock()
    mock_update.return_value = [{'name': 'test'}, {'name': 'example'}]
    mock_add.return_value = [{'name': 'test'}, {'name': 'sample'}, {'name': 'example'}]
    expected = [{'name': 'test'}, {'name': 'sample'}]

    actual = prod.try_add_product(test_prod, mock_cxn)

    assert expected == actual
    assert mock_update.call_count == 0
    assert mock_add.call_count == 0

@patch('builtins.input', side_effect = ['a2','n'])
@patch('builtins.print')
@patch('modules.funcs_products.add_new_product')
@patch('modules.funcs_products.update_product')
@patch('modules.funcs_utilities.is_value_in_dict')
def test_try_add_new_product___path_3___product_exists__do_not_update(mock_dict_check, 
                                                                mock_update_func, 
                                                                mock_add_func, 
                                                                mock_print, 
                                                                mock_input):
    test_products = [{'name': 'a1'}, {'name': 'a2'}]
    mock_cxn = Mock()
    mock_dict_check.return_value = True
    mock_update_func.return_value = [{'name': 'a1'}, {'name': 'a3'}]
    mock_add_func.return_value = [{'name': 'a1'}, {'name': 'a2'}, {'name': 'a3'}]
    expected = [{'name': 'a1'}, {'name': 'a2'}]

    actual = prod.try_add_product(test_products, mock_cxn)

    assert expected == actual
    assert mock_update_func.call_count == 0
    assert mock_add_func.call_count == 0
    mock_print.assert_called_with('\nA2 already exists in the product menu.')

@patch('builtins.input', side_effect = ['a2',''])
@patch('builtins.print')
@patch('modules.funcs_products.add_new_product')
@patch('modules.funcs_products.update_product')
@patch('modules.funcs_utilities.is_value_in_dict')
@patch('modules.funcs_utilities.get_dict_index')
def test_try_add_new_product___path_4___product_exists__update(mock_get_index,
                                                                mock_dict_check,
                                                                mock_update_func, 
                                                                mock_add_func, 
                                                                mock_print, 
                                                                mock_input):
    test_products = [{'name': 'a1'}, {'name': 'a2'}]
    mock_cxn = Mock()
    mock_get_index.return_value = 1
    mock_dict_check.return_value = True
    mock_update_func.return_value = [{'name': 'a1'}, {'name': 'a3'}]
    mock_add_func.return_value = [{'name': 'a1'}, {'name': 'a2'}, {'name': 'a3'}]
    expected = [{'name': 'a1'}, {'name': 'a3'}]

    actual = prod.try_add_product(test_products, mock_cxn)

    assert expected == actual
    assert mock_add_func.call_count == 0
    assert mock_update_func.call_count == 1
    # mock_update_func.assert_called_with({'name': 'a2'}, [{'name': 'a1'}, {'name': 'a2'}])
    mock_print.assert_called_with('\nA2 already exists in the product menu.')



# @patch('builtins.input', side_effect = ['Drinks', '4.45', '17'])
# @patch('db.db.db_command')
# @patch('db.db.db_query')
# def test_add_new_product(mock_query, mock_db, mock_input):
#     mock_cxn = Mock()
#     sql = "INSERT INTO `products` (`name`, `category`, `price`, `stock`) VALUES ('Test', 'Drinks', 4.45, 17)"

#     prod.add_new_product('Test', mock_cxn)

#     mock_db.assert_called_with('sql', mock_cxn)

