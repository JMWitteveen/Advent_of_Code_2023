import re
import os
from functools import reduce
from operator import mul

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

total_value = 0

def clean_up_line(line):
    pattern = re.compile(r'^Game \d+: ')
    retval = re.sub(pattern, '', line)
    return retval.replace('\n', '')

def check_cubes(set, max_dict):
    dict = get_red_green_blue(set)
    
    for key in dict:
        max_dict[key] = max(dict[key], max_dict[key])
    
    return max_dict

def get_red_green_blue(set):
    color_dict = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    set = set.split(', ')
    for s in set:
        foo = s.split(' ')
        color_dict[foo[1]] += int(foo[0])

    return color_dict
        
with open(full_path, 'r') as file:
    for line in file:
        max_dict = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        line = clean_up_line(line)
        for set in line.split('; '):
            max_dict = check_cubes(set, max_dict)
        
        power = reduce(mul, max_dict.values())
        total_value += power

print(total_value)
