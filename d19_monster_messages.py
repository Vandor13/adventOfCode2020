import functools


class MonsterMessage:

    def __init__(self, filename, len_parts):
        self.rules = dict()
        self.messages = []
        self.len_parts = len_parts
        self.read_file(filename)
        # print("Messages:", self.messages)
        # print([len(message) for message in self.messages])
        self.longest_message = max([len(message) for message in self.messages])
        self.rule42 = self.interpret_rule(42)
        print("Calculated Rule 42")
        self.rule31 = self.interpret_rule(31)
        print("Calculated Rule 31")
        # print("Longest message:", self.longest_message)

    def read_file(self, filename: str):
        with open(filename, "r") as file:
            while True:
                rule_string = file.readline()
                if rule_string != "\n":
                    rule_parts = rule_string.split(":")
                    self.rules[int(rule_parts[0])] = rule_parts[1].strip()
                else:
                    break
            self.messages = [line.rstrip("\n") for line in file.readlines()]

    def print_rules_and_messages(self):
        print(self.rules)
        print(self.messages)

    def interpret_rule(self, rule_number: int) -> list:
        interpretations = []
        rule_string = str(self.rules[rule_number])
        if rule_string.startswith('"'):
            interpretations.append(rule_string.strip('"'))
            # print(rule_string)
            return interpretations
        # elif rule_string.startswith("!"):
        #     interpretations += rule_string.lstrip("!").split("|")
        else:
            rule_alternatives = rule_string.split("|")
            for rule in rule_alternatives:
                new_interpretations = self.merge_rules_together(rule.strip().split())  #, max_length)
                if len(new_interpretations) > 0:
                    interpretations += new_interpretations
        return interpretations

    def merge_rules_together(self, rule_numbers: list) -> list:
        merged_rules = []
        # # print(max_length)
        # if max_length <= 0:
        #     return []
        if len(rule_numbers) > 1 and rule_numbers[0] == "11" and rule_numbers[1] == "8":
            massimov = 1
            massime = 2
        for number in rule_numbers:
            # print("Beep")
            if number == "11":
                rule_interpretations = ["!11"]
            elif number == "8":
                rule_interpretations = ["!8"]
            else:
                rule_interpretations = self.interpret_rule(int(number))  # ,max_length - len(rule_numbers) + 1)
            # print("Rule number:", number, "interpreted as:", rule_interpretations)
            if len(merged_rules) == 0:
                merged_rules = rule_interpretations
            else:
                old_merged_rules = merged_rules.copy()
                merged_rules = []
                for interpretation in rule_interpretations:
                    for old_rule in old_merged_rules:
                        merged_rules.append(str(old_rule + interpretation))
            # print(merged_rules)
        # print("Bop", rule_numbers)
        # for rule in merged_rules.copy():
        #     if len(rule) > max_length:
        #         merged_rules.remove(rule)
        return merged_rules

    def match_messages_to_rule(self, rule_number: int):
        number_of_correct_messages = 0
        rule_interpretations = self.interpret_rule(rule_number)  #, self.longest_message)
        print(rule_interpretations)
        print([len(rule) for rule in rule_interpretations])
        for message in self.messages:
            if message in rule_interpretations:
                number_of_correct_messages += 1
        print("Number of correct messages:", number_of_correct_messages)

    def match_messages_to_rule_v2(self):
        number_of_correct_messages = 0
        for message in self.messages:
            rest_message = message
            while len(rest_message) > self.len_parts * 2:
                if rest_message[:self.len_parts] in self.rule42:
                    if self.matches_rule_11(rest_message[self.len_parts:]):
                        number_of_correct_messages += 1
                        break
                    else:
                        rest_message = rest_message[self.len_parts:]
                else:
                    break
        print("Number of correct messages:", number_of_correct_messages)

    def matches_rule_11(self, message: str) -> bool:
        if len(message) < self.len_parts * 2:
            return False
        elif message[:self.len_parts] in self.rule42 and message[self.len_parts:] in self.rule31:
            return True
        else:
            if message[:self.len_parts] in self.rule42 and message[-self.len_parts:] in self.rule31:
                return self.matches_rule_11(message[self.len_parts:-self.len_parts])
            else:
                return False

    def change_rules_for_part2(self):
        self.rules[8] = "42 | 42 8"
        self.rules[11] = "42 31 | 42 11 31"


monster_message = MonsterMessage("input19.txt", 8)
# monster_message.print_rules_and_messages()
# print(monster_message.interpret_rule(0))
# print("Merged rules:", monster_message.merge_rules_together([4, 5]))
monster_message.change_rules_for_part2()
monster_message.match_messages_to_rule_v2()

