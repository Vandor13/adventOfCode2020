class TicketTranslator():

    def __init__(self, filename: str):
        self.rules, self.your_ticket, self.nearby_tickets = self.interpret_file(filename)
        self.ticket_fields = ["" for rule in self.rules]

    def interpret_file(self, filename: str) -> [list, list, list]:
        with open(filename, "r") as file:
            line = file.readline()
            rules = dict()
            while line != "\n":
                # print(line)
                rule_name, rule_values = line.rstrip("\n").split(":")
                # print(rule_parts)
                rule_values = rule_values.strip().split(" ")
                rules[rule_name] = rule_values[0].split("-") + rule_values[2].split("-")
                line = file.readline()
            print("Rules:", rules)
            file.readline()
            your_ticket = file.readline().rstrip("\n").split(",")
            print("Your ticket:", your_ticket)
            file.readline()
            file.readline()
            tickets = [y.rstrip("\n").split(",") for y in file.readlines()]
            print("Nearby tickets:", tickets)
        return rules, your_ticket, tickets

    def check_nearby_tickets_for_errors(self) -> list:
        error_values = list()
        tickets_to_be_removed = []
        for ticket in self.nearby_tickets:
            ticket_valid = True
            for value in ticket:
                value_valid = False
                for rule in self.rules.values():
                    if (int(rule[0]) <= int(value) <= int(rule[1])) or (int(rule[2]) <= int(value) <= int(rule[3])):
                        value_valid = True
                        # print("Value is true:", value)
                        break
                if not value_valid:
                    error_values.append(int(value))
                    ticket_valid = False
            if not ticket_valid:
                tickets_to_be_removed.append(ticket)
        print("Error Values:", error_values)
        for ticket in tickets_to_be_removed:
            self.nearby_tickets.remove(ticket)
        return error_values

    def determine_fields(self):
        fields_to_be_determined = list(self.rules.keys())
        while "" in self.ticket_fields:
            print("Trying again:")
            for i in range(len(self.nearby_tickets[0])):
                if self.ticket_fields[i] == "":
                    possible_fields = fields_to_be_determined.copy()
                    for ticket in self.nearby_tickets:
                        value = ticket[i]
                        for rule_name in possible_fields.copy():
                            rule = self.rules[rule_name]
                            if not (int(rule[0]) <= int(value) <= int(rule[1])) and not (int(rule[2]) <= int(value) <= int(rule[3])):
                                possible_fields.remove(rule_name)
                                # print("Field", i, "Can't be field", rule_name, "because of value", value)
                        if len(possible_fields) == 1:
                            print("Field", i, "has to be field", possible_fields[0])
                            self.ticket_fields[i] = possible_fields[0]
                            fields_to_be_determined.remove(possible_fields[0])
                            break
                    print("For field", i, "there are", len(possible_fields), "left:", possible_fields)
            # print(possible_fields)
            print("Determined fields:", self.ticket_fields)

    def sum_departure_fields(self):
        departure_multiply = 1
        for i in range(len(self.ticket_fields)):
            if self.ticket_fields[i].startswith("departure"):
                print(self.ticket_fields[i], "is", self.your_ticket[i])
                departure_multiply *= int(self.your_ticket[i])
        print("Departure multiply:", departure_multiply)


ticket_translator = TicketTranslator("input16.txt")
print(sum(ticket_translator.check_nearby_tickets_for_errors()))
print("Valid tickets:", ticket_translator.nearby_tickets)
ticket_translator.determine_fields()
ticket_translator.sum_departure_fields()
