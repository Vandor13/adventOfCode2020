with open("input", "r") as input_file:
    input_lines = [int(line) for line in input_file.readlines()]
for line in input_lines:
    first_rest_to_2020 = 2020 - line
    # print(line, rest_to_2020)
    for line2 in input_lines:
        second_rest_to_2020 = first_rest_to_2020 - line2
        if second_rest_to_2020 in input_lines:
            print(line, line2, second_rest_to_2020)
            print(line * line2 * second_rest_to_2020)
            exit()
    # else:
    #     input_lines.remove(line)
