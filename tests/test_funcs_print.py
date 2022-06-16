from modules import funcs_utilities as f_p
from unittest.mock import Mock, patch, call



### _PRINT_NON_INDEXED
@patch('builtins.print')
def test_print_non_indexed_name_phone(mock_print: Mock):
    test_data = [{'name':'value1'},{'phone':'value2'}]

    f_p._print_non_indexed(test_data)

    mock_print.assert_has_calls([
        call('               value1', end=': '),
        call('value2')
    ])
    assert mock_print.call_count == 2

@patch('builtins.print')
def test_print_non_indexed_name_price(mock_print: Mock):
    test_data = [{'name':'value1'},{'price':2}]

    f_p._print_non_indexed(test_data)

    mock_print.assert_has_calls([
        call('               value1', end=': '),
        call('£2.00')
    ])
    assert mock_print.call_count == 2

@patch('builtins.print')
def test_print_non_indexed_name_nokey(mock_print: Mock):
    test_data = [{'name':'value1'},{'key2':'value2'}]

    f_p._print_non_indexed(test_data)

    mock_print.assert_has_calls([
        call('               value1', end=': ')
    ])
    assert mock_print.call_count == 1

@patch('builtins.print')
def test_print_non_indexed_nokeys(mock_print: Mock):
    test_data = [{'key1':'value1'},{'key2':'value2'}]

    f_p._print_non_indexed(test_data)

    assert mock_print.call_count == 0



### _PRINT_INDEXED
@patch('builtins.print')
def test_print_indexed_name_phone(mock_print: Mock):
    test_data = [{'name':'value1'},{'phone':'value2'}]

    f_p._print_indexed(test_data)

    mock_print.assert_has_calls([
        call(' 1', end = ' '),
        call('............value1', end=': '),
        call(' 2', end = ' '),
        call('value2')
    ])
    assert mock_print.call_count == 4

@patch('builtins.print')
def test_print_indexed_name_price(mock_print: Mock):
    test_data = [{'name':'value1'},{'price':2.5}]

    f_p._print_indexed(test_data)

    mock_print.assert_has_calls([
        call(' 1', end = ' '),
        call('............value1', end=': '),
        call(' 2', end = ' '),
        call('£2.50', end = ' ')
    ])
    assert mock_print.call_count == 4

@patch('builtins.print')
def test_print_indexed_name_nokey(mock_print: Mock):
    test_data = [{'name':'value1'},{'key2':'value2'}]

    f_p._print_indexed(test_data)

    mock_print.assert_has_calls([
        call(' 1', end = ' '),
        call('............value1', end=': '),
        call(' 2', end = ' ')
    ])
    assert mock_print.call_count == 3

@patch('builtins.print')
def test_print_indexed_nokeys(mock_print: Mock):
    test_data = [{'key1':'value1'},{'key2':'value2'}]

    f_p._print_indexed(test_data)

    mock_print.assert_has_calls([
        call(' 1', end = ' '),
        call(' 2', end = ' ')
    ])
    assert mock_print.call_count == 2



### PRINT_PLAIN_LIST
@patch('builtins.print')
@patch('modules.funcs_utilities._print_non_indexed')
def test_print_plain_list_products(mock_print_list, mock_print: Mock):
    test_data = [{'key1': 'value1'}]
    test_type = 'products'

    f_p.print_plain_list(test_type, test_data)

    mock_print.assert_called_with('\nProducts:')
    mock_print_list.assert_called_with(test_data)
    assert mock_print.call_count == 1
    assert mock_print_list.call_count == 1

@patch('builtins.print')
@patch('modules.funcs_utilities._print_non_indexed')
def test_print_plain_list_noproducts(mock_print_list, mock_print: Mock):
    test_data = []
    test_type = 'products'

    f_p.print_plain_list(test_type, test_data)

    mock_print.assert_called_with('\nThere are no products listed.')
    assert mock_print.call_count == 1
    assert mock_print_list.call_count == 0



### PRINT_INDEXED_LIST
@patch('builtins.print')
@patch('modules.funcs_utilities._print_indexed')
def test_print_indexed_list_products(mock_print_list, mock_print: Mock):
    test_data = [{'key1': 'value1'}]
    test_type = 'products'

    f_p.print_indexed_list(test_type, test_data)

    mock_print.assert_any_call('\nProducts:')
    mock_print_list.assert_called_with(test_data, 1)
    assert mock_print.call_count == 1
    assert mock_print_list.call_count == 1

@patch('builtins.print')
@patch('modules.funcs_utilities._print_non_indexed')
def test_print_indexed_list_noproducts(mock_print_list, mock_print: Mock):
    test_data = []
    test_type = 'products'

    f_p.print_indexed_list(test_type, test_data)

    mock_print.assert_called_with('\nThere are no products listed.')
    assert mock_print.call_count == 1
    assert mock_print_list.call_count == 0
