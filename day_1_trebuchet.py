NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def replace_numbers_in_str(input: str) -> str:
    for i in range(0, len(NUMBERS)):
        input = input.replace(NUMBERS[i], str(f"{NUMBERS[i]}{i}{NUMBERS[i]}"))

    return input


def get_first_int(input: str) -> int:
    for letter in input:
        if letter.isdigit():
            return int(letter)
    print("This string does not contain any numbers!")


def get_last_int(input: str) -> int:
    for letter in reversed(input):
        if letter.isdigit():
            return int(letter)
    print("This string does not contain any numbers!")


def concat_numbers(first: str, last: str) -> int:
    return int(str(first) + str(last))


def calculate_calibration_data(filename: str) -> int:
    file = open(filename, "r")
    lines = file.readlines()
    total: int = 0
    for word in lines:
        word = replace_numbers_in_str(word)
        total = total + (concat_numbers(get_first_int(word), get_last_int(word)))

    return total


print(calculate_calibration_data("calibration_data.txt"))