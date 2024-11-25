# Code for part 1

def main():
    return NotImplementedError()

def combine_first_and_last_digits_from(line):
    digits = '0123456789'
    line_filtered = ''
    for x in line:
        if x in digits:
            line_filtered += x
    return int(line_filtered[0]+line_filtered[-1])

if __name__ == '__main__':
    main()