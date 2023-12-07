import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

total_value = 0

def find_numbers(line):
    indices = [(match.start(), match.end()) for match in re.finditer(r'\d+', line)]
    matches = re.findall(r'\d+', line)
    return indices, matches

def find_asterisks(line):
    asterisks = [match.start() for match in re.finditer(r'\*', line)]
    return asterisks

def calculate_gear_ratio(row, asterisk, text):
    found_numbers = []
    search_range = range(max(0, asterisk-1), min(asterisk+2, len(text[row])))
    
    # check above
    if row > 0:
        found_numbers += check_row(text, row-1, search_range)
    
    #check sides
    found_numbers += check_row(text, row, search_range)
    
    #check below
    if row < len(text)-1:
        found_numbers += check_row(text, row+1, search_range)

    filtered_list = [value for value in found_numbers if value]
    if len(filtered_list) == 2:
        print(f'row: {row}, first number: {filtered_list[0]}, second number: {filtered_list[1]}')
        return filtered_list[0] * filtered_list[1]
    else:
        return 0

def check_row(text, row, search_range):
    n_found_numbers = 0
    found_number_indices = []
    for index in search_range:
            if text[row][index].isdigit():
                temp = find_corresponding_number_indices(text, row, index)
                if temp not in found_number_indices:
                    found_number_indices.append(temp)
                    n_found_numbers += 1

    found_numbers = []
    for x in found_number_indices:
        found_numbers.append(int(text[row][x[0]:x[1]]))
    return(found_numbers)

def find_corresponding_number_indices(text, row, index):
    indices, numbers  = find_numbers(text[row])
    for start, end in indices:
        if start <= index < end: #test if this should be <= end instead
            return start, end

with open(full_path, 'r') as file:
    text = []

    #converts all text into a 2d array and removes the endline notation
    for line in file:
        text.append(line.replace('\n', ''))

    for row, line in enumerate(text):
        asterisks = find_asterisks(line)
        for asterisk in asterisks:
            total_value += calculate_gear_ratio(row, asterisk, text)

print(total_value)
            



