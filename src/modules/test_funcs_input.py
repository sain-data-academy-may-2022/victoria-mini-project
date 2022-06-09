import funcs_input as f_i
from unittest.mock import Mock, patch, call



### FORMAT_STRING
def test_format_string():
    test_string = 'Test'
    expected = 'Test'

    actual = f_i.format_string(test_string)

    assert expected == actual

def test_format_string_titlecase():
    test_string = 'test'
    expected = 'Test'

    actual = f_i.format_string(test_string)

    assert expected == actual

def test_format_string_strip_empty_space():
    test_string = '     test     '
    expected = 'Test'

    actual = f_i.format_string(test_string)

    assert expected == actual

def test_format_string_strip_trailing_characters():
    test_string = '     test     \n\t'
    expected = 'Test'

    actual = f_i.format_string(test_string)

    assert expected == actual

def test_format_string_strip_pound_signs():
    test_string = '£     test     \n\t'
    expected = 'Test'

    actual = f_i.format_string(test_string)

    assert expected == actual



###
