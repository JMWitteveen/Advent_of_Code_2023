import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

def strip_start(line):
    pattern = re.compile(r'^game \d+: ')
    return re.sub(pattern, '', line)


with open(full_path, 'r') as file:
    for line in file:
        line = strip_start(line)
        print(line)