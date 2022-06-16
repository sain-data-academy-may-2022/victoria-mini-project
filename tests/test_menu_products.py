import modules.menu_products as m_p
from unittest.mock import Mock, patch, call


### PRODUCT_MENU_CHOICE
@patch('builtins.input', side_effect = ['0'])
def test_product_menu_choice_0(mock_input):
    expected = False
    td = ['a']
    mock_cxn = Mock()

    actual = m_p.product_menu_choice(td, mock_cxn)[0]

    assert expected == actual

@patch('builtins.input', side_effect = ['1'])
@patch('modules.funcs_products.print_product_list')
def test_product_menu_choice_1(mock_print_list, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_p.product_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_print_list.call_count == 1

@patch('builtins.input', side_effect = ['2'])
@patch('modules.funcs_products.try_add_product')
def test_product_menu_choice_2(mock_add_product, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_p.product_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_add_product.call_count == 1

@patch('builtins.input', side_effect = ['3'])
@patch('modules.funcs_products.try_update_product')
def test_product_menu_choice_3(mock_update_product, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_p.product_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_update_product.call_count == 1

@patch('builtins.input', side_effect = ['4'])
@patch('modules.funcs_products.try_delete_product')
def test_product_menu_choice_4(mock_delete_product, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_p.product_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_delete_product.call_count == 1

@patch('builtins.input', side_effect = ['test'])
@patch('builtins.print')
def test_product_menu_choice_invalid(mock_print, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_p.product_menu_choice(td, mock_cxn)[0]
    mock_print.assert_called_with('\nInvalid selection. Please select a valid menu option.')
    assert expected == actual


### PRODUCT_MENU
@patch('modules.clear_screen.clear_screen')
@patch('modules.menu_products.print_product_options')
@patch('modules.menu_products.product_menu_choice')
def test_product_menu(mock_product_choice, mock_product_options, mock_cs):
    test_data = ['a', 'b']
    test_cxn = Mock()
    mock_product_choice.return_value = False, ['a', 'b', 'c']
    expected = ['a', 'b', 'c']

    actual = m_p.product_menu(test_data, test_cxn)

    assert expected == actual
