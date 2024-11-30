# Code for part 1

from pathlib import Path


def main():
    input_file_path = Path(__file__).parent / "input.txt"
    print(sum_all_lines_in_file(input_file_path))


def sum_all_lines_in_string(input_string):
    input_lines = input_string.splitlines()
    return sum_all_lines(input_lines)


def sum_all_lines_in_file(input_file_name):
    input_file = open(input_file_name)
    input_lines = input_file.readlines()
    return sum_all_lines(input_lines)


def sum_all_lines(input_lines):
    return sum(combine_first_and_last_digits_from(line) for line in input_lines)


def combine_first_and_last_digits_from(line):
    digits = "0123456789"
    find_first_digit_in_line(line, digits)

    return int(
        find_first_digit_in_line(line, digits)
        + find_first_digit_in_line(line[::-1], digits)
    )


def find_first_digit_in_line(line, digits):
    for x in line:
        if x in digits:
            return x


if __name__ == "__main__":
    main()
