
from enum import Enum


class Numbers(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


def get_calibration(input: list[str]) -> list[int]:
    calibration = []
    for line in input:
        digits_in_line = digits(line)
        digits_in_line.update(digits_spelled_out(line))
        number = min(digits_in_line.items(), key=lambda x: x[0])[1]
        number += max(digits_in_line.items(), key=lambda x: x[0])[1]
        calibration.append(int(number))
    return calibration


def digits(line: str) -> dict[int, str]:
    digits = {}
    for i, char in enumerate(line):
        if char.isnumeric():
            digits[i] = char
    return digits

def digits_spelled_out(line: str) -> dict[int, str]:
    digits = {}
    for number in Numbers:
        index = line.find(number.name.lower())
        while index != -1:
            digits[index] = str(number.value)
            index = line.find(number.name.lower(), index+1)
    return digits
   

if __name__ == '__main__':
    with open("day1_trebuchet\input.txt", "r") as input:
        calibration_values = get_calibration(input.readlines())
    print(sum(calibration_values))
