import re
import os
import string

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

total_value = 0

def find_numbers(line):
    indices = [(match.start(), match.end()) for match in re.finditer(r'\d+', line)]
    matches = re.findall(r'\d+', line)
    return indices, matches

def look_for_symbol(row, number_indices, text):
    symbol_found = False
    #check before and after the number
    if number_indices[0] > 0:
        symbol_found = True if is_valid_symbol(text[row][number_indices[0]-1]) else symbol_found
    if number_indices[1] < len(text[row]):
        symbol_found = True if is_valid_symbol(text[row][number_indices[1]]) else symbol_found
    #check above the number
    if row > 0:
        start = max(number_indices[0]-1, 0)
        end = min(number_indices[1], len(text[row])-1)
        for i in range(start,end+1):
            symbol_found = True if is_valid_symbol(text[row-1][i]) else symbol_found

    #check below
    if row < len(text)-1:
        start = max(number_indices[0]-1, 0)
        end = min(number_indices[1], len(text[row])-1)
        for i in range(start,end+1):
            symbol_found = True if is_valid_symbol(text[row+1][i]) else symbol_found

    return symbol_found

def is_valid_symbol(char):
    return char in string.punctuation and char != '.'

with open(full_path, 'r') as file:
    text = []

    for line in file:
        text.append(line.replace('\n', ''))

    for x, line in enumerate(text):
        indices, numbers  = find_numbers(line)
        for y, index in enumerate(indices):
            if look_for_symbol(x, index, text):
                print(numbers[y])
                total_value += int(numbers[y])


print(total_value)