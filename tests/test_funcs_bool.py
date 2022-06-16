import modules.funcs_utilities as f_b
from unittest.mock import Mock, patch, call

### IS_VALUE_IN_DICT
def test_is_value_in_dict_true():
    td = [
        {'name': 'Test1', 'category': 'Drinks', 'active': 1},
        {'name': 'Test2', 'category': 'Drinks', 'active': 0},
    ]
    expected = True

    actual = f_b.is_value_in_dict('name', 'Test1', td)

    assert expected == actual

def test_is_value_in_dict_false():
    td = [
        {'name': 'Test1', 'category': 'Drinks', 'active': 1},
        {'name': 'Test2', 'category': 'Drinks', 'active': 0},
    ]
    expected = False

    actual = f_b.is_value_in_dict('name', 'Test4', td)

    assert expected == actual

def test_is_value_in_dict_empty_list():
    td = []
    expected = False

    actual = f_b.is_value_in_dict('name', 'Test4', td)

    assert expected == actual



### IS_ITEM_IN_LIST
def test_is_item_in_list():
    test_list = ['a1', 'b2', 'c3']
    test_item = 'a1'
    expected = True

    actual = f_b.is_item_in_list(test_item, test_list)

    assert expected == actual

def test_is_item_in_list_not():
    test_list = ['a1', 'b2', 'c3']
    test_item = 'd4'
    expected = False

    actual = f_b.is_item_in_list(test_item, test_list)

    assert expected == actual

def test_is_item_in_list_empty():
    test_list = []
    test_item = 'a1'
    expected = False

    actual = f_b.is_item_in_list(test_item, test_list)

    assert expected == actual



### IS_INDEX_WITHIN_RANGE
def test_is_index_within_range_start_range():
    test_idx = 0
    test_list = ['a', 'b', 'c', 'd', 'e']
    expected = True

    actual = f_b.is_index_within_range(test_idx, test_list)

    assert expected == actual

def test_is_index_within_range_end_of_range():
    test_idx = 4
    test_list = ['a', 'b', 'c', 'd', 'e']
    expected = True

    actual = f_b.is_index_within_range(test_idx, test_list)

    assert expected == actual

def test_is_index_within_range_below_range():
    test_idx = -1
    test_list = ['a', 'b', 'c', 'd', 'e']
    expected = False

    actual = f_b.is_index_within_range(test_idx, test_list)

    assert expected == actual

def test_is_index_within_range_beyond_range():
    test_idx = 5
    test_list = ['a', 'b', 'c', 'd', 'e']
    expected = False

    actual = f_b.is_index_within_range(test_idx, test_list)

    assert expected == actual

def test_is_index_within_range_empty_list():
    test_idx = 1
    test_list = []
    expected = False

    actual = f_b.is_index_within_range(test_idx, test_list)

    assert expected == actual
