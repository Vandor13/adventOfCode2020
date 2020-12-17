with open("input3.txt", "r") as file:
    tree_map = file.readlines()
pattern_length = len(str(tree_map[0]))
# print(str(tree_map[0]))
# print(pattern_length)
pos_x, pos_y = 0, 0
number_of_trees = 0
for i in range(len(tree_map) - 1):
    print(i)
    pos_x = (pos_x + 3) % (pattern_length - 1)
    pos_y += 1
    tree_line = str(tree_map[pos_y])
    if tree_line[pos_x] == "#":
        print_trees = tree_line[:pos_x] + "X" + tree_line[pos_x + 1:]
        print(print_trees)
        number_of_trees += 1
    else:
        print_trees = tree_line[:pos_x] + "O" + tree_line[pos_x + 1:]
        print(print_trees)
print(number_of_trees)