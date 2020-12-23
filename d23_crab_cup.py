class CrabCup:
    debug = False

    def __init__(self, cup_list: list, no_of_actions):
        self.cups = cup_list
        self.no_of_cups = len(cup_list)
        self.highest_cup = max(cup_list)
        self.lowest_cup = min(cup_list)
        self.no_of_actions = no_of_actions
        self.current_cup = cup_list[0]
        self.current_cup_index = 0
        self.picked_up_cups = []
        self.destination_cup = None
        self.move_no = 0
        self.make_x_moves()

    def make_x_moves(self):
        for _ in range(self.no_of_actions):
            self.make_move()
        print("-- final --")
        index = self.cups.index(1)
        print("Cup After:", self.cups[index + 1])
        print("Cup After After:", self.cups[index + 2])
        print("Multiplication: ", self.cups[index + 1] * self.cups[index + 2])
        # self.print_cup_list()

    def make_move(self):
        self.move_no += 1
        if self.move_no % 1000 == 0:
            print("-- move", self.move_no, "--")
        if CrabCup.debug:
            print("-- move", self.move_no, "--")
            self.print_cup_list()
        self.pick_up_three_cups()
        self.select_destination()
        self.put_cups_back()
        self.select_new_current_cup()
        if CrabCup.debug:
            print()

    def pick_up_three_cups(self):
        current_index = self.current_cup_index
        for i in range(3):
            index = (current_index + 1) % len(self.cups)
            if index == 0:
                current_index = -1
                self.current_cup_index = - 1
                # index wrapped around and now we should only take from front of list
            cup = self.cups.pop(index)
            self.picked_up_cups.append(cup)
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
        current_index = self.cups.index(self.destination_cup)
        for i in range(3):
            self.cups.insert(current_index + i + 1, self.picked_up_cups.pop(0))
            if current_index < self.current_cup_index:
                self.current_cup_index += 1

    def select_new_current_cup(self):
        old_index = self.current_cup_index
        new_index = (old_index + 1) % len(self.cups)
        self.current_cup = self.cups[new_index]
        self.current_cup_index = new_index

    def print_cup_list(self):
        cups_string = "cups: "
        for cup in self.cups:
            if cup == self.current_cup:
                cups_string += "(" + str(cup) + ") "
            else:
                cups_string += str(cup) + " "
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
cup_list = list_of_million_cups(test_data)
crab_cup = CrabCup(cup_list, 1000000)
