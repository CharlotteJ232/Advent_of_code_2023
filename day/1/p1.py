# Code for part 1


def main():
    return NotImplementedError()


def sum_all_lines(input_string):
    return sum(
        combine_first_and_last_digits_from(line) for line in input_string.splitlines()
    )


def sum_all_lines_in_file(input_file_name):
    input_file = open(input_file_name)
    return sum(
        combine_first_and_last_digits_from(line) for line in input_file.readlines()
    )


def combine_first_and_last_digits_from(line):
    digits = "0123456789"
    line_filtered = ""
    for x in line:
        if x in digits:
            line_filtered += x
    return int(line_filtered[0] + line_filtered[-1])


if __name__ == "__main__":
    main()
