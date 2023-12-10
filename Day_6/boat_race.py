import re
import os
from math import prod

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")
total_value = 0

with open(full_path, 'r') as file:
    lines = file.readlines()

def handle_input_txt(lines):
    output = []
    for line in lines:
        output.append([int(num) for num in re.findall(r'\d+', line)])

    return tuple(output)

races, records = handle_input_txt(lines)

total_value = []

for x, race in enumerate(races):
    n_wins = 0
    for second in range(race):
        distance = (race-second) * second
        if distance > records[x]:
            n_wins += 1
    total_value.append(n_wins)

print(prod(total_value))
