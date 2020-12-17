with open("input", "r") as input_file:
    input_lines = [int(line) for line in input_file.readlines()]
for line in input_lines:
    rest_to_2020 = 2020 - line
    # print(line, rest_to_2020)
    if rest_to_2020 in input_lines:
        print(line, rest_to_2020)
        print(line * rest_to_2020)
        exit()
    # else:
    #     input_lines.remove(line)
