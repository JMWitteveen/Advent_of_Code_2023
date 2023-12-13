import re
import os
import math

from itertools import cycle

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

with open(full_path, 'r') as file:
    lines = file.readlines()


def clean_up_line(line):
    segments = re.findall(r'[A-Z][A-Z][A-Z]', line)
    return segments[0], (segments[1], segments[2])


instructions = lines[0].replace('\n', '')
instructions = [0 if instruction == 'L' else 1 for instruction in instructions]
direction_dict = {}

for i in range(2, len(lines)):
    key, values = clean_up_line(lines[i])
    direction_dict[key] = values

starting_keys = [key for key in direction_dict if key[2] == 'A']

cycles = []
for key in starting_keys:
    for steps, instruction in enumerate(cycle(instructions), start=1):
        key = direction_dict[key][instruction]
        if key[2] == 'Z':
            cycles.append(steps)
            break

print(math.lcm(*cycles))
