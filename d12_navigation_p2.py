# import numpy

directions = {
    "north": [0, 1],
    "east": [1, 0],
    "south": [0, -1],
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


def execute_command(waypoint: list,  position: list, command: list) -> [list, list]:
    if command[0] in ["left", "right"]:
        waypoint = rotate_waypoint(waypoint,  command)
        print("Rotated waypoint to", waypoint, "due to command", command)
    elif command[0] == "forward":
        position = execute_move(waypoint, position, command)
        print("Moved to", position, "due to command", command)
    else:
        waypoint = move_waypoint(waypoint, command)
        print("Moved waypoint to", waypoint, "due to command", command)
    return [waypoint, position]


def rotate_waypoint(waypoint: list, command: list) -> list:
    rotation_value = command[1] // 90
    sign = -1 if command[0] == "left" else 1
    d90_rotation_number = (sign * rotation_value) % 4
    for _ in range(d90_rotation_number):
        new_x = waypoint[1]
        new_y = - waypoint[0]
        waypoint = [new_x, new_y]
    return waypoint


def move_waypoint(waypoint: list, command: list) -> list:
    move_vector = directions[command[0]]
    pos_x = waypoint[0] + move_vector[0] * command[1]
    pos_y = waypoint[1] + move_vector[1] * command[1]
    return [pos_x, pos_y]


def execute_move(waypoint: list, position: list, command: list) -> list:
    pos_x = position[0] + waypoint[0] * command[1]
    pos_y = position[1] + waypoint[1] * command[1]
    return [pos_x, pos_y]


current_position = [0, 0]
current_waypoint = [10, 1]
command_list = parse_file("input12.txt")
for command_tuple in command_list:
    current_waypoint, current_position = execute_command(current_waypoint, current_position, command_tuple)
print("Endposition:", current_position)
print("Manhattan Distance:", abs(current_position[0]) + abs(current_position[1]))
