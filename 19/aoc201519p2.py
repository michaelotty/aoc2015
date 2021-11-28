"""Advent of code Day 19 part 2"""

import re
from multiprocessing import Process

def processing(replacements: list[tuple[str, str]], formula: str, list_of_formula: list):
    for replace_from, replace_to in replacements:
        for i in range(len(formula)):
            left_formula, right_formula = formula[:i], formula[i:]
            molecule = left_formula + \
                right_formula.replace(replace_to, replace_from, 1)
            list_of_formula.append(molecule)


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        file_contents = file.read()

    replacements, original_formula = file_contents.split('\n\n')
    replacements = replacements.split('\n')
    replacements = [tuple(re.split(r' => ', line)) for line in replacements]

    distinct_molecules = []
    distinct_molecules.append(original_formula)
    level = 0

    while 'e' not in distinct_molecules:
        processes = [Process(target=processing, args=(replacements, formula, distinct_molecules)) for formula in tuple(distinct_molecules)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()
            
        level += 1

    print(distinct_molecules)
    print(level)


if __name__ == "__main__":
    main()