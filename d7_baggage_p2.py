def interpret_rules(rule_list) -> dict:
    bags_dict = dict()
    for rule in rule_list:
        outer_bag, inner_bags_string = str(rule).split(" bags contain ")
        # print("Outer bag:", outer_bag)
        raw_inner_bags = str(inner_bags_string).split(",")
        inner_bags = []
        for raw_inner_bag in raw_inner_bags:
            inner_bag = raw_inner_bag.strip().strip(".").rstrip("s").strip("bag").strip()
            # print(raw_inner_bag)
            if inner_bag == "no other":
                break
            amount = int(inner_bag[0])
            inner_bag_name = inner_bag[2:]
            bag_rule = [inner_bag_name, amount]
            inner_bags.append(bag_rule)
        bags_dict[outer_bag] = inner_bags
    return bags_dict


def no_of_bags_contained(bag_rules: dict, bag_name: str) -> int:
    print_text = "------\n"
    no_of_bags = 0
    bags_contained = bag_rules[bag_name]
    print_text += bag_name + " contains: \n"
    for bag in bags_contained:
        print_text += str(bag[1]) + " " + str(bag[0]) + " bags \n"
        no_of_bags += no_of_bags_contained(bag_rules, bag[0]) * int(bag[1]) + int(bag[1])
    if no_of_bags == 0:
        print_text += "No other bags\n"
    else:
        print(print_text)
        print("Total of bags in", bag_name, ":", no_of_bags)
    return no_of_bags


with open("input7.txt", "r") as file:
    rules = file.readlines()
bag_dict = interpret_rules(rules)
print(bag_dict)
result_bags = no_of_bags_contained(bag_dict, "shiny gold")
print("No of bags in shiny gold bag:", result_bags)
# print(len(result_bags))

