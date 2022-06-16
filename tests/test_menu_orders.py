import modules.menu_orders as m_o
from unittest.mock import Mock, patch, call


### ORDER_MENU_CHOICE
@patch('builtins.input', side_effect = ['0'])
def test_order_menu_choice_0(mock_input):
    expected = False
    td = ['a']
    mock_cxn = Mock()

    actual = m_o.order_menu_choice(td, td, td, mock_cxn)[0]

    assert expected == actual

@patch('builtins.input', side_effect = ['1'])
@patch('modules.funcs_orders.print_order_list')
def test_order_menu_choice_1(mock_print_list, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_o.order_menu_choice(td, td, td, mock_cxn)[0]

    assert expected == actual
    assert mock_print_list.call_count == 1

@patch('builtins.input', side_effect = ['2'])
@patch('modules.funcs_orders.try_add_order')
def test_order_menu_choice_2(mock_add_order, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_o.order_menu_choice(td, td, td, mock_cxn)[0]

    assert expected == actual
    assert mock_add_order.call_count == 1

@patch('builtins.input', side_effect = ['3'])
@patch('modules.funcs_orders.try_update_order_status')
def test_order_menu_choice_3(mock_update_order, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_o.order_menu_choice(td, td, td, mock_cxn)[0]

    assert expected == actual
    assert mock_update_order.call_count == 1

@patch('builtins.input', side_effect = ['4'])
@patch('modules.funcs_orders.try_update_order_details')
def test_order_menu_choice_4(mock_update_order, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_o.order_menu_choice(td, td, td, mock_cxn)[0]

    assert expected == actual
    assert mock_update_order.call_count == 1

@patch('builtins.input', side_effect = ['5'])
@patch('modules.funcs_orders.try_delete_order')
def test_order_menu_choice_4(mock_delete_order, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_o.order_menu_choice(td, td, td, mock_cxn)[0]

    assert expected == actual
    assert mock_delete_order.call_count == 1

@patch('builtins.input', side_effect = ['test'])
@patch('builtins.print')
def test_order_menu_choice_invalid(mock_print, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_o.order_menu_choice(td, td, td, mock_cxn)[0]

    mock_print.assert_called_with('\nInvalid selection. Please select a valid menu option.')
    assert expected == actual


### ORDER_MENU
@patch('modules.clear_screen.clear_screen')
@patch('modules.menu_orders.print_order_options')
@patch('modules.menu_orders.order_menu_choice')
def test_order_menu(mock_order_choice, mock_order_options, mock_cs):
    test_data = ['a', 'b']
    test_cxn = Mock()
    mock_order_choice.return_value = False, ['a', 'b'], ['a', 'b'], ['a', 'b', 'c']
    expected = ['a', 'b'], ['a', 'b'], ['a', 'b', 'c']

    actual = m_o.order_menu(test_data, test_data, test_data, test_cxn)

    assert expected == actual
