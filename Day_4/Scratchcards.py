import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")
total_value = 0

def clean_up_line(line):
    pattern = re.compile(r'^Card *\d+: ')
    retval = re.sub(pattern, '', line)
    return retval.replace('\n', '')

def find_all_numbers(line):
        line = line.split("|")
        winning_numbers = re.findall(r'\d+', line[0])
        numbers_you_have = re.findall(r'\d+', line[1])
        return winning_numbers, numbers_you_have

with open(full_path, 'r') as file:

    for line in file:
        wins = 0
        line = clean_up_line(line)
        winning_numbers, numbers_you_have = find_all_numbers(line)

        for n in numbers_you_have:
            if n in winning_numbers:
                wins += 1

        total_value += 0 if wins == 0 else 2**(wins-1)
        
print(total_value)