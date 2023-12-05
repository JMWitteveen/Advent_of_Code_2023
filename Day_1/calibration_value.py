import os
import re

file_name = 'C:/Users/jmwit/Desktop/Advent_of_Code_2023/Day_1/input.txt'
total_value = 0

digit_strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

pattern = re.compile("|".join(map(re.escape, digit_strings)))

def get_first_digit(line):
    match = pattern.search(line)

    return match.group()

def get_last_digit(line):
    matches = list(pattern.finditer(line))

    return matches[-1].group()

print(get_first_digit("eight2three"))
print(get_last_digit("eight2three"))


# with open(file_name, 'r') as file:
#     for line in file:
#         calibration_value = ""
#         calibration_value += get_first_digit(line)
#         calibration_value += get_last_digit(line)
#         total_value += int(calibration_value)

# print(total_value)