"""Advent of code Day 17 part 1"""

from itertools import combinations


def main():
    """Main function"""
    with open('input.txt') as file:
        data = file.readlines()

    comb = 0

    containers = tuple(int(i) for i in data)
    for j in range(1, len(containers)+1):
        for i in combinations(containers, j):
            if sum(i) == 150:
                comb += 1
    print(comb)


if __name__ == "__main__":
    main()
