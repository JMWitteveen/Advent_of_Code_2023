import re
import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")
total_value = 0

with open(full_path, 'r') as file:
    lines = file.readlines()


def clean_up_line(line):
    result = re.findall(r'-*\d+', line)
    return [int(entry) for entry in result]


def predict_next_value(values):
    print(values)
    if all(value == 0 for value in values):
        return 0

    difference_values = [values[i+1] - values[i] for i in range(len(values)-1)]

    result = predict_next_value(difference_values)
    return values[0] - result


for line in lines:
    values = clean_up_line(line)
    result = predict_next_value(values)
    print(f'PREVIOUS VALUE: {result}')
    total_value += result

print(total_value)
