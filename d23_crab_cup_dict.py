class CrabCup:
    debug = False

    def __init__(self, cups: list, no_of_actions, no_of_cups):
        self.cups = self.init_dict(cups, no_of_cups)
        self.no_of_cups = no_of_cups
        self.highest_cup = no_of_cups
        self.lowest_cup = 1
        self.no_of_actions = no_of_actions
        self.current_cup = cups[0]
        self.picked_up_cups = []
        self.destination_cup = None
        self.move_no = 0
        self.make_x_moves()

    def init_dict(self, cups: list, no_of_cups):
        cups_dict = dict()
        if no_of_cups > len(cups):
            previous_cup = no_of_cups
        else:
            previous_cup = cups[-1]
        for i in range(len(cups)):
            cups_dict[previous_cup] = cups[i]
            previous_cup = cups[i]
        if no_of_cups > len(cups):
            cups_dict[previous_cup] = len(cups) + 1
        print(cups_dict)
        return cups_dict

    def make_x_moves(self):
        for _ in range(self.no_of_actions):
            self.make_move()
        print("-- final --")
        index = 1
        cup_after = self.get_next_cup(1)
        cup_after_after = self.get_next_cup(cup_after)
        print("Cup After 1:", cup_after)
        print("Cup After After:", cup_after_after)
        print("Multiplication: ", cup_after * cup_after_after)
        # self.print_cup_list()

    def get_next_cup(self, cup_number):
        return self.cups.setdefault(cup_number, cup_number + 1)

    def make_move(self):
        self.move_no += 1
        if self.move_no % 100000 == 0:
            print("-- move", self.move_no, "--")
            print("Dictionary Use:", len(self.cups))
        if CrabCup.debug:
            print("-- move", self.move_no, "--")
            # self.print_cup_list()
            print(self.cups)
        self.pick_up_three_cups()
        self.select_destination()
        self.put_cups_back()
        self.select_new_current_cup()
        if CrabCup.debug:
            print()

    def pick_up_three_cups(self):
        self.picked_up_cups = []
        picked_up_cup = self.get_next_cup(self.current_cup)
        self.picked_up_cups.append(picked_up_cup)
        picked_up_cup = self.get_next_cup(picked_up_cup)
        self.picked_up_cups.append(picked_up_cup)
        picked_up_cup = self.get_next_cup(picked_up_cup)
        self.picked_up_cups.append(picked_up_cup)
        self.cups[self.current_cup] = self.get_next_cup(picked_up_cup)
        if CrabCup.debug:
            cups_string = ", ".join([str(x) for x in self.picked_up_cups])
            print("pick up:", cups_string)

    def select_destination(self):
        destination_label = self.current_cup - 1
        while True:
            if destination_label >= self.lowest_cup:
                if destination_label in self.picked_up_cups:
                    destination_label -= 1
                    continue
                else:
                    self.destination_cup = destination_label
                    break
            else:
                destination_label = self.highest_cup
                continue
        if CrabCup.debug:
            print("destination:", destination_label)

    def put_cups_back(self):
        destination = self.destination_cup
        cup_after_destination = self.get_next_cup(self.destination_cup)
        next_cup = self.picked_up_cups.pop(0)
        self.cups[destination] = next_cup
        destination = next_cup
        next_cup = self.picked_up_cups.pop(0)
        self.cups[destination] = next_cup
        destination = next_cup
        next_cup = self.picked_up_cups.pop(0)
        self.cups[destination] = next_cup
        destination = next_cup
        self.cups[destination] = cup_after_destination

    def select_new_current_cup(self):
        self.current_cup = self.get_next_cup(self.current_cup)
        if self.debug:
            print("Current Cup:", self.current_cup)

    def print_cup_list(self):
        cups_string = "cups: "
        cups_string += "(" + str(self.current_cup) + ") "
        cup = self.get_next_cup(self.current_cup)
        for _ in range(self.no_of_cups - 1):
            cups_string += str(cup) + " "
            cup = self.get_next_cup(cup)
        print(cups_string)


def list_of_million_cups(cups: list):
    cup_no = max(cups) + 1
    for _ in range(1000000 - len(cups)):
        cups.append(cup_no)
        cup_no += 1
    return cups


test_data = [3, 8, 9, 1, 2, 5, 4, 6, 7]
input_data = [9, 1, 6, 4, 3, 8, 2, 7, 5]
# crab_cup = CrabCup(test_data, 100)
# crab_cup = CrabCup(input_data, 100)
# cup_list = list_of_million_cups(test_data)
# crab_cup = CrabCup(test_data, 1000000, 1000000)
crab_cup = CrabCup(input_data, 10000000, 1000000)
