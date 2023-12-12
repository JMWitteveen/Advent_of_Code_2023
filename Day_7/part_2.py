import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

with open(full_path, 'r') as file:
    lines = file.readlines()

def clean_up_line(line):
    return line.replace("\n", "").split(" ")

def determine_poker_hand(line):
    cards = {"x": 0}
    n_jokers = 0
    for card in line:
        if card == "J":
            n_jokers += 1
        elif card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    sorted_keys = sorted(cards, key=lambda x: cards[x], reverse=True)
    
    if cards[sorted_keys[0]] + n_jokers >= 5:      #five of a kind
        return 6
    if cards[sorted_keys[0]] + n_jokers >= 4:      #four of a kind
        return 5
    if cards[sorted_keys[0]] + n_jokers >= 3: 
        if cards[sorted_keys[1]] == 2:  #full house
            return 4
        return 3                        #three of a kind
    if cards[sorted_keys[0]] + n_jokers >= 2:
        if cards[sorted_keys[1]] == 2:  #2 pair
            return 2
        return 1                        #pair
    return 0                            #high card

def sort_hands_by_poker_score():
    poker_hands = [[],[],[],[],[],[],[]]

    for x, line in enumerate(lines):
        lines[x] = clean_up_line(line)
        hand = determine_poker_hand(lines[x][0])
        poker_hands[hand].append(lines[x])
    return poker_hands

def custom_sort_key(card):
    order = "AKQT98765432J"
    return [order.index(c) for c in card[0]]

sorted_poker_hands = sort_hands_by_poker_score()

current_rank = 1

total_value = 0

for x, hands in enumerate(sorted_poker_hands):
    sorted_poker_hands[x] = sorted(sorted_poker_hands[x], key=custom_sort_key, reverse=True)
    for hand in sorted_poker_hands[x]:
        winnings = current_rank * int(hand[1])
        total_value += winnings
        current_rank += 1

print(total_value)