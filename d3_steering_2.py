def calculate_trees(tree_map, delta_x, delta_y) -> int:
    pos_x, pos_y = 0, 0
    number_of_trees = 0
    pattern_length = len(str(tree_map[0]))
    for i in range((len(tree_map) - 1) // delta_y):
        # print(i)
        pos_x = (pos_x + delta_x) % (pattern_length - 1)
        pos_y += delta_y
        tree_line = str(tree_map[pos_y])
        if tree_line[pos_x] == "#":
            print_trees = tree_line[:pos_x] + "X" + tree_line[pos_x + 1:]
            # print(print_trees)
            number_of_trees += 1
        else:
            print_trees = tree_line[:pos_x] + "O" + tree_line[pos_x + 1:]
            # print(print_trees)
    print(number_of_trees)
    return number_of_trees


with open("input3.txt", "r") as file:
    input_map = file.readlines()
# print(str(tree_map[0]))
# print(pattern_length)
num1 = calculate_trees(input_map, 1, 1)
num2 = calculate_trees(input_map, 3, 1)
num3 = calculate_trees(input_map, 5, 1)
num4 = calculate_trees(input_map, 7, 1)
num5 = calculate_trees(input_map, 1, 2)

product_all = num1 * num2 * num3 * num4 * num5
print(product_all)
