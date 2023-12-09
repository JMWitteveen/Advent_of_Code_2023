import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

def convert_txt_to_lists():
    with open(full_path, 'r') as file:
        lines = file.read()

    lines = lines.replace('\n', '@').split('@@')

    for line in lines:
        line = clean_up_line(line)
        maps.append(line.split('@'))

    for x in maps:
        for index, values in enumerate(x):
            x[index] = values.split(' ')

def clean_up_line(line):
    pattern = re.compile(r'[a-zA-Z- ]+:@* *')
    return re.sub(pattern, '', line)

maps = []
convert_txt_to_lists()
checkpoint = 50000
increment = checkpoint
goal = 100000000

for i in range(goal):
    if i > checkpoint:
        print(f'progress: {checkpoint} / {goal}')
        checkpoint += increment
    current_value = i
    for conversion_map in range(len(maps)-1, 0, -1):
        for conversion_range in maps[conversion_map]:
            if int(conversion_range[0]) <= current_value < int(conversion_range[0]) + int(conversion_range[2]):
                current_value = int(conversion_range[1]) + (current_value - int(conversion_range[0]))
                break
    for seed_range in maps[0]:
        if int(seed_range[0]) <= current_value < int(seed_range[0]) + int(seed_range[1]):
            print(f'location: {i}, current: {current_value}')
            break
    else:
        continue
    break
