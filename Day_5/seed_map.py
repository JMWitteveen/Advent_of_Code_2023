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

final_locations = []

for seed in maps[0][0]:
    current_value = int(seed)
    for conversion_map in range(1,len(maps)):
        for conversion_range in maps[conversion_map]:
            if int(conversion_range[1]) <= current_value < (int(conversion_range[1]) + int(conversion_range[2])):
                current_value = int(conversion_range[0]) + (current_value - int(conversion_range[1]))
                break
    final_locations.append(current_value)

print(min(final_locations))
