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

def calculate_wins(line):
    winning_numbers, numbers_you_have = find_all_numbers(line)
    wins = 0

    for n in numbers_you_have:
            if n in winning_numbers:
                wins += 1
    return wins

with open(full_path, 'r') as file:
    lines = file.readlines()

line_count = len(lines)
n_cards = [1] * line_count
for row, line in enumerate(lines):
    line = clean_up_line(line)
    wins = calculate_wins(line)
    start = row + 1
    end = min(row + 1 + wins, line_count)
    for i in range(start, end):
        n_cards[i] += 1 * n_cards[row]
        pass

print(sum(n_cards))