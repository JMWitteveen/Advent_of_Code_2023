import os

current_dir = os.getcwd()
full_path = os.path.join(current_dir, "input.txt")

UP_LIST = ['|', '7', 'F']
RIGHT_LIST = ['-', 'J', '7']
DOWN_LIST = ['|', 'L', 'J']
LEFT_LIST = ['-', 'L', 'F']

direction_dict = {(-1, 0): UP_LIST,
                  (0, 1): RIGHT_LIST,
                  (1, 0): DOWN_LIST,
                  (0, -1): LEFT_LIST}


def find_s(lines):
    for row, line in enumerate(lines):
        if line.find('S') >= 0:
            return row, line.find('S')


def find_starting_direction(current_point, lines):
    y, x = current_point
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dir in directions:
        y, x = [a + b for a, b in zip(current_point, dir)]
        try:
            if lines[y][x] in direction_dict[dir]:
                return dir
        except IndexError:
            pass


def update_direction_vector(current_character, direction_vector):
    if current_character in ['L', '7']:
        return direction_vector[::-1]
    if current_character in ['F', 'J']:
        x, y = direction_vector[::-1]
        return -x, -y

    return direction_vector


def part_1(current_point, lines):
    direction_vector = find_starting_direction(current_point, lines)
    searching = True
    steps = 0
    while searching:
        current_point = [a + b for a,
                         b in zip(current_point, direction_vector)]

        current_character = lines[current_point[0]][current_point[1]]

        direction_vector = update_direction_vector(
            current_character, direction_vector)
        steps += 1
        if current_character == 'S':
            searching = False
    print(steps/2)


if __name__ == "__main__":
    with open(full_path, 'r') as file:
        lines = file.readlines()

    starting_point = find_s(lines)
    part_1(starting_point, lines)
