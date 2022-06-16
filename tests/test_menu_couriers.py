import modules.menu_couriers as m_c
from unittest.mock import Mock, patch, call


### COURIER_MENU_CHOICE
@patch('builtins.input', side_effect = ['0'])
def test_courier_menu_choice_0(mock_input):
    expected = False
    td = ['a']
    mock_cxn = Mock()

    actual = m_c.courier_menu_choice(td, mock_cxn)[0]

    assert expected == actual

@patch('builtins.input', side_effect = ['1'])
@patch('modules.funcs_couriers.print_courier_list')
def test_courier_menu_choice_1(mock_print_list, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_c.courier_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_print_list.call_count == 1

@patch('builtins.input', side_effect = ['2'])
@patch('modules.funcs_couriers.try_add_courier')
def test_courier_menu_choice_2(mock_add, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_c.courier_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_add.call_count == 1

@patch('builtins.input', side_effect = ['3'])
@patch('modules.funcs_couriers.try_update_courier')
def test_courier_menu_choice_3(mock_update, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_c.courier_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_update.call_count == 1

@patch('builtins.input', side_effect = ['4'])
@patch('modules.funcs_couriers.try_delete_courier')
def test_courier_menu_choice_4(mock_delete, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_c.courier_menu_choice(td, mock_cxn)[0]

    assert expected == actual
    assert mock_delete.call_count == 1

@patch('builtins.input', side_effect = ['test'])
@patch('builtins.print')
def test_courier_menu_choice_invalid(mock_print, mock_input):
    expected = True
    td = ['a']
    mock_cxn = Mock()

    actual = m_c.courier_menu_choice(td, mock_cxn)[0]
    
    mock_print.assert_called_with('\nInvalid selection. Please select a valid menu option.')
    assert expected == actual


