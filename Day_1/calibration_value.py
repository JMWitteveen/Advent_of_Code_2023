import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")
total_value = 0

digit_strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
reversed_strings = [s[::-1] for s in digit_strings]

pattern_from_left = re.compile("|".join(map(re.escape, digit_strings)))
pattern_from_right = re.compile("|".join(map(re.escape, reversed_strings)))

def word_to_digit(word, reversed=False):
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    if reversed:
        word = word[::-1]

    return word_to_digit[word]


def get_first_digit(line):
    match = pattern_from_left.search(line)

    if match.group().isdigit():
       return str(match.group())
    
    return word_to_digit(match.group())

def get_last_digit(line):
    match = pattern_from_right.search(line[::-1])

    if match.group().isdigit():
       return str(match.group())
    
    return word_to_digit(match.group(), True)

with open(full_path, 'r') as file:
    for line in file:
        calibration_value = ""
        calibration_value += get_first_digit(line)
        calibration_value += get_last_digit(line)
        total_value += int(calibration_value)

print(total_value)