import re

SYMBOLS: list[str] = ["*", "$", "/", "+", "-", "=", "&", "#", "@", "%"]
numbersmap = []
file = open("schematics.txt", "r")
lines = file.readlines()


def check_schematics():
    tuplemap = []

    for line in lines:
        index_line = [i for i, item in enumerate(line) if re.search("[0-9]", item)]
        numbersmap.append(index_line)
    for line in numbersmap:
        tuplemap.append(turn_into_tuples(line))
    line_number = 0
    total = 0
    for line in tuplemap:
        for tuple in line:
            if adjacent_to_symbol(line_number, tuple[0], tuple[1]):
                total = total + int(lines[line_number][tuple[0] : tuple[1] + 1])
        line_number = line_number + 1
    print(total)


def adjacent_to_symbol(line_number: int, first: int, last: int) -> bool:
    first_line = line_number - 1
    if first_line < 0:
        first_line = 0
    final_line = line_number + 1
    if final_line > len(lines) - 1:
        final_line = len(lines) - 1
    for line in range(first_line, final_line + 1):
        first_index = first - 1
        if first_index < 0:
            first_index = 0
        last_index = last + 1
        if last_index > len(lines[line_number]) - 1:
            last_index = len(lines[line_number]) - 1

        for char_index in range(first_index, last_index + 1):
            if lines[line][char_index] in SYMBOLS:
                return True
    return False


def turn_into_tuples(line: list[int]) -> tuple:
    first = line[0]
    last = line[0]
    tuples: list[tuple] = []
    for number in line[1:]:
        if number == last + 1:
            last = number
        else:
            tuples.append((first, last))
            first = number
            last = number

        if number == line[-1]:
            tuples.append((first, last))

    return tuples


check_schematics()
