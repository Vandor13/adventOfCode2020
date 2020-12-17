number_to_arrangements = dict()


def find_no_of_arrangements(joltage_list: list, current_value: int, current_list: list) -> int:
    if len(joltage_list) == 1:
        # current_list.append(joltage_list[0])
        # print("Found arrangement:", current_list)
        return 1
    elif len(joltage_list) < 1:
        return 0
    loaded_no = number_to_arrangements.get(current_value)
    if loaded_no:
        return loaded_no
    no_of_arrangements = 0
    for i in range(len(joltage_list)):
        if joltage_list[i] - current_value <= 3:
            # new_list = current_list.copy()
            # new_list.append(joltage_list[i])
            no_of_arrangements += find_no_of_arrangements(joltage_list.copy()[i+1:], joltage_list[i], []) #  new_list)
        else:
            break
    number_to_arrangements[current_value] = no_of_arrangements
    return no_of_arrangements


with open("input10.txt", "r") as file:
    joltages = [int(x) for x in file.readlines()]

# joltages.append(0)
joltages.append(max(joltages) + 3)
joltages.sort()
# diff_of_one = 0
# diff_of_three = 0
# for i in range(len(joltages) - 1):
#     if joltages[i] + 1 == joltages[i+1]:
#         diff_of_one += 1
#     elif joltages[i] + 3 == joltages[i+1]:
#         diff_of_three += 1
# print("Found", diff_of_one, "differences of 1 jolt and", diff_of_three, "differences of 3 jolts")
# print("Multiplication:", diff_of_one * diff_of_three)
number_of_arrangements = find_no_of_arrangements(joltages, 0, [0])
print("Number of possible arrangements:", number_of_arrangements)
