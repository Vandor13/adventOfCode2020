directions = {
    "north": [0, -1],
    "east": [1, 0],
    "south": [0, 1],
    "west": [-1, 0]
}

direction_sequence = ["east", "south", "west", "north"]

direction_parse_dict = {
    "N": "north",
    "S": "south",
    "E": "east",
    "W": "west",
    "L": "left",
    "R": "right",
    "F": "forward"
}


def parse_file(file_name: str) -> list:
    commands = []
    with open(file_name, "r") as file:
        for command in file.readlines():
            direction = direction_parse_dict[command[0]]
            value = int(command[1:])
            commands.append([direction, value])
    return commands


def execute_command(heading: str, position: list, command: list) -> [str, list]:
    if command[0] in ["left", "right"]:
        heading = execute_turn(heading, command)
        print("Changed direction to", heading, "due to command", command)
    else:
        position = execute_move(heading, position, command)
        print("Moved to", position, "due to command", command)
    return [heading, position]


def execute_turn(heading: str, command: list) -> str:
    current_heading_index = direction_sequence.index(heading)
    heading_change_value = command[1] // 90
    # print("Heading change value:", heading_change_value, "due to command:", command)
    sign = -1 if command[0] == "left" else 1
    new_heading_index = (current_heading_index + (sign * heading_change_value)) % 4
    return direction_sequence[new_heading_index]


def execute_move(heading: str, position: list, command: list) -> list:
    if command[0] == "forward":
        move_vector = directions[heading]
    else:
        move_vector = directions[command[0]]
    pos_x = position[0] + move_vector[0] * command[1]
    pos_y = position[1] + move_vector[1] * command[1]
    return [pos_x, pos_y]


current_heading = "east"
current_position = [0, 0]
command_list = parse_file("input12.txt")
for command_tuple in command_list:
    current_heading, current_position = execute_command(current_heading, current_position, command_tuple)
print("Endposition:", current_position)
print("Manhattan Distance:", abs(current_position[0]) + abs(current_position[1]))
