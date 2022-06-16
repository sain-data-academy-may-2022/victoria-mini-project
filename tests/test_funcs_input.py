from modules import funcs_utilities as f_i
from unittest.mock import Mock, patch, call



### _FORMAT_STRING
def test__format_string():
    test_string = 'Test'
    expected = 'Test'

    actual = f_i._format_string(test_string)

    assert expected == actual

def test__format_string_titlecase():
    test_string = 'test'
    expected = 'Test'

    actual = f_i._format_string(test_string)

    assert expected == actual

def test__format_string_strip_empty_space():
    test_string = '     test     '
    expected = 'Test'

    actual = f_i._format_string(test_string)

    assert expected == actual

def test__format_string_strip_trailing_characters():
    test_string = '     test     \n\t'
    expected = 'Test'

    actual = f_i._format_string(test_string)

    assert expected == actual

def test__format_string_strip_pound_signs():
    test_string = '£     test     \n\t'
    expected = 'Test'

    actual = f_i._format_string(test_string)

    assert expected == actual

def test__format_string_strip_only_stripped_chars():
    test_string = '£          \n\t'
    expected = ''

    actual = f_i._format_string(test_string)

    assert expected == actual

def test__format_string_strip_mysql_chars():
    test_string = 'Robert\'); DROP TABLE Students; --'
    expected = 'Robert\'); Drop Table Students'

    actual = f_i._format_string(test_string)

    assert expected == actual



### GET_INT_INPUT
@patch('builtins.input', side_effect = ['3'])
def test_get_int_input(mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q)

    assert expected == actual

@patch('builtins.input', side_effect = ['test', '3'])
@patch('builtins.print')
def test_get_int_input_string(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q)

    mock_print.assert_called_with('Please enter a valid number.')
    assert expected == actual

@patch('builtins.input', side_effect = ['test', '5a', '3'])
@patch('builtins.print')
def test_get_int_input_string_string(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q)

    mock_print.assert_called_with('Please enter a valid number.')
    # mock_print.
    assert expected == actual

@patch('builtins.input', side_effect = ['2.0', '3'])
@patch('builtins.print')
def test_get_int_input_float(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q)

    mock_print.assert_called_with('Please enter a valid number.')
    assert expected == actual

@patch('builtins.input', side_effect = [''])
@patch('builtins.print')
def test_get_int_input_blank(mock_print, mock_input):
    test_q = 'sample input'
    expected = ''
    
    actual = f_i.get_int_input(test_q, True)

    assert expected == actual

@patch('builtins.input', side_effect = ['', '3'])
@patch('builtins.print')
def test_get_int_input_do_not_allow_blank(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q, False)
    assert mock_print.call_count == 1
    assert expected == actual
    mock_print.assert_called_with('Please enter a valid number.')

@patch('builtins.input', side_effect = ['-3', '3'])
@patch('builtins.print')
def test_get_int_input_negative(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q, False)
    assert mock_print.call_count == 1
    assert expected == actual
    mock_print.assert_called_with('Please enter a valid number.')

@patch('builtins.input', side_effect = ['0'])
@patch('builtins.print')
def test_get_int_input_zero_allowed(mock_print, mock_input):
    test_q = 'sample input'
    expected = 0
    
    actual = f_i.get_int_input(test_q, False, True)
    assert expected == actual
    
@patch('builtins.input', side_effect = ['0', '3'])
@patch('builtins.print')
def test_get_int_input_zero_not_allowed(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q, False, False)
    assert mock_print.call_count == 1
    assert expected == actual
    mock_print.assert_called_with('Please enter a valid number.')
    
@patch('builtins.input', side_effect = ['£3'])
def test_get_int_input_pounds(mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = f_i.get_int_input(test_q, False, False)
    assert expected == actual



### GET_FLOAT_NUMBER
@patch('builtins.input', side_effect = ['3'])
def test_get_float_input_int(mock_input):
    test_q = 'sample input'
    expected = 3.0

    actual = f_i.get_positive_float_input(test_q)

    assert expected == actual

@patch('builtins.input', side_effect = ['3.7'])
def test_get_float_input_float(mock_input):
    test_q = 'sample input'
    expected = 3.7

    actual = f_i.get_positive_float_input(test_q)

    assert expected == actual

@patch('builtins.input', side_effect = ['test', '3.7'])
@patch('builtins.print')
def test_get_float_input_string(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3.7

    actual = f_i.get_positive_float_input(test_q)

    assert expected == actual
    mock_print.assert_called_with('Please enter a valid number.')
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect = ['', '3.7'])
@patch('builtins.print')
def test_get_float_input_not_allow_blank(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3.7

    actual = f_i.get_positive_float_input(test_q)

    assert expected == actual
    mock_print.assert_called_with('Please enter a valid number.')
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect = ['test', ''])
@patch('builtins.print')
def test_get_float_input_allow_blank(mock_print, mock_input):
    test_q = 'sample input'
    expected = ''

    actual = f_i.get_positive_float_input(test_q, True)

    assert expected == actual
    mock_print.assert_called_with('Please enter a valid number.')
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect = ['-3', '3'])
@patch('builtins.print')
def test_get_float_input_negative(mock_print, mock_input):
    test_q = 'sample input'
    expected = 3.0

    actual = f_i.get_positive_float_input(test_q, False)

    assert expected == actual
    mock_print.assert_called_with('Please enter a valid number.')
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect = ['£3.40'])
def test_get_float_input_pounds(mock_input):
    test_q = 'sample input'
    expected = 3.40

    actual = f_i.get_positive_float_input(test_q, False)

    assert expected == actual

@patch('builtins.input', side_effect = ['3.48888'])
def test_get_float_input_rounded(mock_input):
    test_q = 'sample input'
    expected = 3.49

    actual = f_i.get_positive_float_input(test_q, False)

    assert expected == actual



### GET_STRING_INPUT
@patch('builtins.input', side_effect = ['test'])
def test_get_string_input(mock_input):
    test_q = 'sample input'
    expected = 'Test'
    
    actual = f_i.get_string_input(test_q, True)

    assert expected == actual

@patch('builtins.input', side_effect = [''])
def test_get_string_input_allow_blank(mock_input):
    test_q = 'sample input'
    expected = ''
    
    actual = f_i.get_string_input(test_q, True)

    assert expected == actual

@patch('builtins.input', side_effect = ['', 'test'])
@patch('builtins.print')
def test_get_string_input_blank_not_allowed(mock_print, mock_input):
    test_q = 'sample input'
    expected = 'Test'
    
    actual = f_i.get_string_input(test_q, False)

    mock_print.assert_called_once_with('Empty answers not allowed.')
    assert expected == actual

@patch('builtins.input', side_effect = ['', '', 'test'])
@patch('builtins.print')
def test_get_string_input_blank_x2_not_allowed(mock_print, mock_input):
    test_q = 'sample input'
    expected = 'Test'
    
    actual = f_i.get_string_input(test_q, False)

    mock_print.assert_has_calls([
        call('Empty answers not allowed.'),
        call('Empty answers not allowed.')])
    assert expected == actual



### GET_INPUT_WITHIN_LIST
@patch('builtins.input', side_effect = ['test'])
def test_get_string_input_within_list(mock_input):
    test_q = 'sample input'
    test_list = ['Test', 'Input', 'A1']
    expected = 'Test'
    
    actual = f_i.get_input_within_list(test_q, test_list)

    assert expected == actual

@patch('builtins.input', side_effect = ['', 'a1'])
@patch('builtins.print')
def test_get_string_input_within_list_blank_not_allowed(mock_print, mock_input):
    test_q = 'sample input'
    test_list = ['Test', 'Input', 'A1']
    expected = 'A1'
    
    actual = f_i.get_input_within_list(test_q, test_list)

    assert expected == actual
    assert mock_print.call_count == 1
    mock_print.assert_called_with('Empty answers not allowed.')

@patch('builtins.input', side_effect = [''])
def test_get_string_input_within_list_empty_allowed(mock_input):
    test_q = 'sample input'
    test_list = ['Test', 'Input', 'A1']
    expected = ''
    
    actual = f_i.get_input_within_list(test_q, test_list, True)

    assert expected == actual

@patch('builtins.print')
@patch('builtins.input', side_effect = ['sample', ''])
def test_get_string_input_within_list_empty_allowed_nested(mock_input, mock_print):
    test_q = 'sample input'
    test_list = ['Test', 'Input', 'A1']
    expected = ''
    
    actual = f_i.get_input_within_list(test_q, test_list, True)

    assert expected == actual
    assert mock_print.call_count == 1
    mock_print.assert_called_with('Please enter a valid option.')

@patch('builtins.input', side_effect = ['sample', 'test'])
@patch('builtins.print')
def test_get_string_input_within_list_not_(mock_print, mock_input):
    test_q = 'sample input'
    test_list = ['Test', 'Input', 'A1']
    expected = 'Test'
    
    actual = f_i.get_input_within_list(test_q, test_list, True)

    assert expected == actual
    assert mock_print.call_count == 1
    mock_print.assert_called_with('Please enter a valid option.')