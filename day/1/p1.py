# Code for part 1

from pathlib import Path

DIGITS = "0123456789"
DIGIT_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


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
    return int(
        find_first_digit_in_line(line, DIGIT_WORDS)
        + find_first_digit_in_line(line[::-1], reverse_dictionary_keys(DIGIT_WORDS))
    )


def find_first_digit_in_line(line, digit_words):
    for index, character in enumerate(line):
        if character in DIGITS:
            return character
        for key in digit_words.keys():
            if character == key[0]:
                if key == line[index : index + len(key)]:
                    return digit_words[key]


def reverse_dictionary_keys(dictionary):
    reversed_dictionary = {}
    for key in dictionary.keys():
        reversed_dictionary[key[::-1]] = dictionary[key]
    return reversed_dictionary


if __name__ == "__main__":
    main()
