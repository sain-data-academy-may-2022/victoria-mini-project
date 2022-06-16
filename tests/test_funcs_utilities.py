from modules import funcs_utilities as f_u
from unittest.mock import Mock, patch, call

### ADD_ITEM_TO_LIST
def test_add_item_to_list():
    test_list = []
    test_item = 'a'
    expected = ['a']

    actual = f_u.add_item_to_list(test_item, test_list)

    assert expected == actual

def test_add_item_to_list_dict():
    test_list = []
    test_item = {'key': 'a'}
    expected = [{'key': 'a'}]

    actual = f_u.add_item_to_list(test_item, test_list)

    assert expected == actual

def test_add_item_to_list_duplicate():
    test_list = ['a']
    test_item = 'a'
    expected = ['a', 'a']

    actual = f_u.add_item_to_list(test_item, test_list)

    assert expected == actual



### UPDATE_ITEM_IN_LIST
def test_update_item_in_list_end():
    _list = ['a', 'b', 'c']
    _item = 'd'
    _index = 2
    expected = ['a', 'b', 'd']

    actual = f_u.update_item_in_list(_item, _index, _list)

    assert expected == actual

def test_update_item_in_list_start():
    _list = ['a', 'b', 'c']
    _item = 'd'
    _index = 0
    expected = ['d', 'b', 'c']

    actual = f_u.update_item_in_list(_item, _index, _list)

    assert expected == actual

def test_update_item_in_list_out_of_range():
    _list = ['a', 'b', 'c']
    _item = 'd'
    _index = 6
    expected = ['a', 'b', 'c']

    actual = f_u.update_item_in_list(_item, _index, _list)

    assert expected == actual

    