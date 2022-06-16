import modules.menu_main as m_m
from unittest.mock import Mock, patch, call


###
### MAIN_MENU_CHOICE
###
@patch('builtins.input', side_effect = ['0'])
@patch('modules.menu_main.print_main_menu')
def test_main_menu_choice_0(mock_print_menu, mock_input):
    expected = False
    td = ['a']
    mock_cxn = Mock()

    actual = m_m.main_menu_choice(td, td, td, mock_cxn)[0]

    assert expected == actual

@patch('modules.menu_main.print_main_menu')
@patch('modules.menu_products.product_menu')
@patch('builtins.input', side_effect = ['1'])
def test_main_menu_choice_1(mock_input, mock_product_menu, mock_print_menu):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_m.main_menu_choice(td, td, td, mock_cxn)[0]

    mock_product_menu.assert_called()
    assert expected == actual

@patch('modules.menu_main.print_main_menu')
@patch('modules.menu_couriers.courier_menu')
@patch('builtins.input', side_effect = ['2'])
def test_main_menu_choice_2(mock_input, mock_courier_menu, mock_print_menu):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_m.main_menu_choice(td, td, td, mock_cxn)[0]

    mock_courier_menu.assert_called()
    assert expected == actual

@patch('modules.menu_main.print_main_menu')
@patch('modules.menu_orders.order_menu')
@patch('builtins.input', side_effect = ['3'])
def test_main_menu_choice_3(mock_input, mock_order_menu, mock_print_menu):
    expected = True
    td = ['a']
    mock_cxn = Mock()
    mock_order_menu.return_value = td, td, td

    actual = m_m.main_menu_choice(td, td, td, mock_cxn)[0]

    mock_order_menu.assert_called()
    assert expected == actual

@patch('builtins.input', side_effect = ['test'])
@patch('builtins.print')
def test_main_menu_choice_invalid(mock_print, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_m.main_menu_choice(td, td, td, mock_cxn)[0]
    mock_print.assert_called_with('Invalid selection. Please select a valid menu option.')
    assert expected == actual

###
### MAIN_MENU
###
@patch('modules.menu_main.main_menu_choice')
def test_main_menu(mock_menu_choice):
    td = ['a']
    test_cxn = Mock()

    mock_menu_choice.return_value = False, ['a'], ['a'], ['a', 'b', 'c']
    expected = ['a'], ['a'], ['a', 'b', 'c']

    actual = m_m.main_menu(td, td, td, test_cxn)

    assert expected == actual
    mock_menu_choice.assert_called_with(td,td, td, test_cxn)
    mock_menu_choice.call_count == 1