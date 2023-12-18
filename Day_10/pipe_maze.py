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


def part_2(current_point, lines):
    direction_vector = find_starting_direction(current_point, lines)
    loop_segments = [current_point]
    n_inside_loop = 0
    searching = True
    steps = 0
    while searching:
        current_point = [a + b for a,
                         b in zip(current_point, direction_vector)]

        current_character = lines[current_point[0]][current_point[1]]
        loop_segments.append(current_point)

        direction_vector = update_direction_vector(
            current_character, direction_vector)
        steps += 1
        if current_character == 'S':
            searching = False

    s_character = determine_pipe_value_of_S(loop_segments)
    s_row = loop_segments[0][0]
    lines[s_row] = lines[s_row][:loop_segments[0][1]] + \
        s_character + lines[s_row][loop_segments[0][1]+1:]
    for row, line in enumerate(lines):
        in_loop = False
        count = 0
        for i in range(len(line)):
            index = [row, i]
            if index in loop_segments:
                next_char = line[i]
                if next_char == "|":
                    in_loop = not in_loop
                elif next_char == "F" or next_char == "J":
                    count += 1
                elif next_char == "7" or next_char == "L":
                    count -= 1
                if count == 2 or count == -2:
                    in_loop = not in_loop
                    count = 0
            else:
                if in_loop:
                    n_inside_loop += 1
    print(n_inside_loop)


def determine_pipe_value_of_S(loop_segments):
    start_location = loop_segments[-2]
    middle_location = loop_segments[0]
    end_location = loop_segments[1]

    if start_location[0] == middle_location[0] == end_location[0]:
        return "-"  # horizontal line
    if start_location[1] == middle_location[1] == end_location[1]:
        return "|"  # vertical line

    if start_location[0] > middle_location[0]:
        # start is below middle so: 7 or F
        if middle_location[1] > end_location[1]:
            # middle is to the right of end
            return "7"  # up and to the left
        else:
            return "F"  # up and to the right
    else:
        # start is above middle so: J or L
        if middle_location[1] > end_location[1]:
            # middle is to the right of end
            return "L"  # down and to the left
        else:
            return "J"


if __name__ == "__main__":
    with open(full_path, 'r') as file:
        lines = file.readlines()

    lines = [f"0{line}0".replace("\n", "") for line in lines]

    starting_point = find_s(lines)
    part_2(starting_point, lines)
