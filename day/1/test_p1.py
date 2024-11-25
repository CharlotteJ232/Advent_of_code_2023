from p1 import combine_first_and_last_digits_from, sum_all_lines, sum_all_lines_in_file
from pathlib import Path


EXAMPLE_INPUT = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


# Tests need to start with test_ or end with _test, as well as the file they are in, for pytest to automatically recognize them (by default)
# Test name: Given, When, Then
def test_given_a_string_when_the_only_digits_are_in_the_first_and_last_place_combine_them():
    # Structure: Arrange, Act, Assert
    # Arrange
    line = "1abc2"

    # Act
    res = combine_first_and_last_digits_from(line)

    # Assert
    assert res == 12


def test_given_a_string_when_the_only_digits_are_in_the_first_and_last_place_combine_them_2():
    # Structure: Arrange, Act, Assert
    # Arrange
    line = "3def4"

    # Act
    res = combine_first_and_last_digits_from(line)

    # Assert
    assert res == 34


def test_two_digits():
    line = "pqr3stu8vwx"

    res = combine_first_and_last_digits_from(line)

    assert res == 38


def test_more_than_two_digits():
    line = "a1b2c3d4e5f"

    res = combine_first_and_last_digits_from(line)

    assert res == 15


def test_one_digit():
    assert combine_first_and_last_digits_from("treb7uchet") == 77


def test_multiple_lines_in_string():
    assert sum_all_lines(EXAMPLE_INPUT) == 142


def test_file_input():
    thisfile = Path(__file__)
    thisdirectory = thisfile.parent
    input_file_path = thisdirectory / "test_input.txt"
    assert sum_all_lines_in_file(input_file_path) == 142
