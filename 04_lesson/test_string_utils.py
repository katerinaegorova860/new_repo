import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Capitalize()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("    ", "    "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_with_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# trim()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   python  ", "python  "),
    ("no_spaces", "no_spaces"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("\tskypro", "\tskypro"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_with_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# contains()


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPpro", "S", True),
    ("SkyPro", "y", True),
    ("hello word", " ", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("SkyPro", "", False),  # проверка на пустой символ
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
def test_contains_with_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")


#  delete_symbol()


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", " ", "helloworld"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_with_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
