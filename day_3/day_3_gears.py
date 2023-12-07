import re

SYMBOLS: list[str] = ["*", "$", "/", "+", "-", "=", "&", "#", "@", "%"]
index_map = []
file = open("schematics.txt", "r")
schematic_lines = file.readlines()


def check_schematics():
    tuples_map = []

    for line in schematic_lines:
        index_line = [i for i, item in enumerate(line) if re.search("[0-9]", item)]
        index_map.append(index_line)
    for line in index_map:
        tuples_map.append(convert_to_tuples_list(line))
    line_number = 0
    total = 0
    for line in tuples_map:
        for tuple in line:
            if is_range_adjacent_to_symbol(line_number, tuple[0], tuple[1]):
                total = total + int(
                    schematic_lines[line_number][tuple[0] : tuple[1] + 1]
                )
        line_number = line_number + 1
    print(total)


def is_range_adjacent_to_symbol(line_number: int, first: int, last: int) -> bool:
    first_line = line_number - 1
    if first_line < 0:
        first_line = 0
    final_line = line_number + 1
    if final_line > len(schematic_lines) - 1:
        final_line = len(schematic_lines) - 1
    for line in range(first_line, final_line + 1):
        first_index = first - 1
        if first_index < 0:
            first_index = 0
        last_index = last + 1
        if last_index > len(schematic_lines[line_number]) - 1:
            last_index = len(schematic_lines[line_number]) - 1

        for char_index in range(first_index, last_index + 1):
            if schematic_lines[line][char_index] in SYMBOLS:
                return True
    return False


def convert_to_tuples_list(line: list[int]) -> list[tuple]:
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
