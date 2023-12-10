import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "test.txt")

with open(full_path, 'r') as file:
    lines = file.readlines()

def clean_up_line(line):
    return line.replace("\n", "").split(" ")

def determine_poker_hand(line):
    cards = {}

    for card in line:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    sorted_keys = sorted(cards, key=lambda x: cards[x], reverse=True)
        
    if cards[sorted_keys[0]] == 5:
        return 6
    if cards[sorted_keys[0]] == 4:
        return 5
    if cards[sorted_keys[0]] == 3:
        if cards[sorted_keys[1]] == 2:
            return 4
        return 3
    if cards[sorted_keys[0]] == 2:
        if cards[sorted_keys[1]] == 2:
            return 2
        return 1
    return 0
    

for x, line in enumerate(lines):
    lines[x] = clean_up_line(line)
    lines[x].append(determine_poker_hand(lines[x][0]))
    print(lines[x])
    