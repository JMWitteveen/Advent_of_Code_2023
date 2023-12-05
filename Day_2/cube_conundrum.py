import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

sum_possible_games = 0

CUBE_PROMPT = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def clean_up_line(line):
    pattern = re.compile(r'^Game \d+: ')
    retval = re.sub(pattern, '', line)
    return retval.replace('\n', '')

def check_cubes(set):
    dict = get_red_green_blue(set)
    
    for key in dict:
        if dict[key] > CUBE_PROMPT[key]:
            return False
    
    return True

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
    for x, line in enumerate(file):
        line = clean_up_line(line)
        possible = True
        for set in line.split('; '):
            if not check_cubes(set):
                possible = False
        if possible:
            sum_possible_games += (x+1)

print(sum_possible_games)