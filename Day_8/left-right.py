import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

with open(full_path, 'r') as file:
    lines = file.readlines()

def clean_up_line(line):
    segments = re.findall(r'[A-Z][A-Z][A-Z]', line)
    return segments[0], (segments[1],segments[2])



instructions = lines[0].replace('\n', '')
direction_dict = {}

for i in range(2,len(lines)):
    key, values = clean_up_line(lines[i])
    direction_dict[key] = values

searching = True
start_key = "AAA"
current_key = start_key
goal_key = "ZZZ"
direction_counter = 0
steps_counter = 0

while searching:
    if instructions[direction_counter] == "L":
        current_key = direction_dict[current_key][0]
    else:
        current_key = direction_dict[current_key][1]
    steps_counter += 1
    direction_counter += 1
    if direction_counter == len(instructions):
        direction_counter = 0
    if current_key == goal_key:
        searching = False

print(steps_counter)