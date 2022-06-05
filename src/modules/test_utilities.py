import utilities as util
from unittest.mock import Mock, patch, call


####################
### BOOL CHECKS
####################
### CHECK_LIST_HAS_ITEMS
def test_list_has_items():
    test_list = ['a', 'b', 'c']
    expected = True

    actual = util.check_list_has_items(test_list)

    assert expected == actual

def test_list_has_no_items():
    test_list = []
    expected = False

    actual = util.check_list_has_items(test_list)

    assert expected == actual


### IS_INDEX_WITHIN_RANGE
def test_index_is_within_range():
    test_list = ['a', 'b', 'c']
    test_index = 1
    expected = True

    actual = util.is_index_within_range(test_index, test_list)

    assert expected == actual

def test_index_not_in_range():
    test_list = ['a', 'b', 'c']
    test_index = 5
    expected = False

    actual = util.is_index_within_range(test_index, test_list)

    assert expected == actual

def test_index_in_empty_list():
    test_list = []
    test_index = 0
    expected = False

    actual = util.is_index_within_range(test_index, test_list)

    assert expected == actual


### IS_STRING_A_KEY
def test_string_is_a_key():
    test_dict = {'key1': 'example', 'key2': 'example'}
    test_string = 'key1'
    expected = True

    actual = util.is_string_a_key(test_string, test_dict)

    assert expected == actual

def test_string_not_a_key():
    test_dict = {'key1': 'example', 'key2': 'example'}
    test_string = 'key4'
    expected = False

    actual = util.is_string_a_key(test_string, test_dict)

    assert expected == actual

def test_string_in_empty_dict():
    test_dict = {}
    test_string = 'key4'
    expected = False

    actual = util.is_string_a_key(test_string, test_dict)

    assert expected == actual


####################
### LISTS
####################
### ADD_ITEM_TO_LIST
def test_add_item_to_list():
    test_list = ['banana', 'apple']
    test_add = 'orange'
    expected = ['banana', 'apple', 'orange']

    actual = util.add_item_to_list(test_add, test_list)

    assert expected == actual


####################
### INPUTS
####################
### GET_INT_INPUT
@patch('builtins.input', side_effect = ['3'])
def test_get_int_input(mock_input):
    test_q = 'sample input'
    expected = 3
    
    actual = util.get_int_input(test_q)

    assert expected == actual
    
# @patch('builtins.input', side_effect = ['test'])
# @patch('builtins.print')
# def test_get_int_input(mock_print, mock_input):
#     test_q = 'sample input'
    
#     util.get_int_input(test_q)

#     mock_print.assert_called_with('Please enter a valid number.')