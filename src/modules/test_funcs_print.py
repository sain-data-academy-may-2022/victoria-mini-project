import funcs_print as f_p
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
    test_data = [{'name':'value1'},{'price':'value2'}]

    f_p._print_non_indexed(test_data)

    mock_print.assert_has_calls([
        call('               value1', end=': '),
        call('£value2')
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
    test_data = [{'name':'value1'},{'price':'value2'}]

    f_p._print_indexed(test_data)

    mock_print.assert_has_calls([
        call(' 1', end = ' '),
        call('............value1', end=': '),
        call(' 2', end = ' '),
        call('£value2')
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
def test_print_plain_list_products(mock_print: Mock):
    test_data = [{'key1': 'value1'}]
    test_type = 'products'

    mock_func = Mock(side_effect = f_p._print_non_indexed(test_data))

    f_p.print_plain_list(test_type, test_data)

    mock_print.assert_called_with('\nCurrent products: ')
    assert mock_print.call_count == 1
    assert mock_func.call_count == 1

@patch('builtins.print')
def test_print_plain_list_products(mock_print: Mock):
    test_data = [{}]
    test_type = 'products'

    mock_func = Mock(side_effect = f_p._print_non_indexed(test_data))

    f_p.print_plain_list(test_type, test_data)

    mock_print.assert_called_with('\nCurrent products:')
    assert mock_print.call_count == 1
    assert mock_func.call_count == 0

