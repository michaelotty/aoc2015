"""Advent of code Day 4 part 1"""

import hashlib


def main():
    """Main function"""
    with open('input.txt') as f:
        file_contents = f.read()

    found = False
    i = 0

    while not found:
        i += 1
        hash_val = hashlib.md5(
            ''.join((file_contents, str(i))).encode('utf-8')).hexdigest()
        found = hash_val[0:5] == '00000'

    print(i)


if __name__ == "__main__":
    main()