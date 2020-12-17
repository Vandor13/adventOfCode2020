def interpret_rules(rule_list) -> dict:
    bag_contained_in = dict()
    for rule in rule_list:
        outer_bag, inner_bags_string = str(rule).split(" bags contain ")
        # print("Outer bag:", outer_bag)
        raw_inner_bags = str(inner_bags_string).split(",")
        inner_bags = []
        for raw_inner_bag in raw_inner_bags:
            inner_bag = raw_inner_bag.strip().strip(".").rstrip("s").strip("bag").strip()
            # print(raw_inner_bag)
            if inner_bag == "no other":
                continue
            inner_bag = inner_bag[2:]
            if inner_bag in bag_contained_in.keys():
                bag_set = bag_contained_in.get(inner_bag)
                bag_set.add(outer_bag)
                bag_contained_in[inner_bag] = bag_set
            else:
                bag_set = {outer_bag}
                bag_contained_in[inner_bag] = bag_set
    return bag_contained_in


def find_containing_bags(bag_color: str, bag_contained_in: dict) -> set:
    searched_bags = set()
    bags_to_be_searched = [bag_color]
    found_bags = set()

    while len(bags_to_be_searched) > 0:
        current_bag = bags_to_be_searched.pop()
        searched_bags.add(current_bag)
        bags_containing_current_bag = bag_contained_in.get(current_bag)
        if bags_containing_current_bag:
            for bag in bags_containing_current_bag:
                found_bags.add(bag)
                if bag not in searched_bags and bag not in bags_to_be_searched:
                    bags_to_be_searched.append(bag)
    return found_bags


with open("input7.txt", "r") as file:
    rules = file.readlines()
bag_dict = interpret_rules(rules)
# print(bag_dict)
result_bags = find_containing_bags("shiny gold", bag_dict)
print(result_bags)
print(len(result_bags))

