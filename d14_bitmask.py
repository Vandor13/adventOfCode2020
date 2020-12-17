class BitMask:
    def __init__(self, file_name, version="v1"):
        with open(file_name, "r") as file:
            self.commands = file.readlines()
            self.bitmask = None
            self.memory = dict()
            self.version = version

    def get_next_command(self):
        raw_command = self.commands.pop(0)
        command_name, command_value = str(raw_command).split(" = ")
        if str(command_name).startswith("mem"):
            command_context = str(command_name).lstrip("mem[").rstrip(" ]")
            print("command context:", command_context)
            command_context = int(command_context)
            command_name = "mem"
            command_value = int(command_value)
        else:
            command_context = None
        return command_name, command_context, command_value

    def set_bitmask(self, bitmask: str):
        self.bitmask = bitmask

    def apply_bitmask(self, value: int) -> int:
        bit_value = "{:36b}".format(value)
        print("value:", value, "bit value:", bit_value, "length:", len(bit_value))
        new_value = []
        # print("Using mask:", self.bitmask, "with length", len(self.bitmask))
        for i in range(len(self.bitmask)):
            if self.bitmask[i] != "X":
                new_value.append(self.bitmask[i])
                # print("Changed bit at", i, "to", self.bitmask[i])
            else:
                if bit_value[i] == " ":
                    new_value.append("0")
                else:
                    new_value.append(bit_value[i])
        result_value =  int("".join(new_value), 2)
        print("Result:", result_value)
        return result_value

    def apply_bitmask_v2(self, value: int) -> list:
        bit_value = "{:36b}".format(value)
        additions = []
        print("value:", value, "bit value:", bit_value, "length:", len(bit_value))
        new_value = []
        # print("Using mask:", self.bitmask, "with length", len(self.bitmask))
        for i in range(len(self.bitmask)):
            if self.bitmask[i] == "X":
                additions.append(pow(2, 36 - i - 1))
                new_value.append("0")
            elif self.bitmask[i] == "0":
                if bit_value[i] == " ":
                    new_value.append("0")
                else:
                    new_value.append(bit_value[i])
            elif self.bitmask[i] == "1":
                new_value.append(self.bitmask[i])
                # print("Changed bit at", i, "to", self.bitmask[i])

        result_value =  int("".join(new_value), 2)
        all_values = [result_value]
        print("Additions:", additions)
        for addition in additions:
            current_values = all_values.copy()
            for value in current_values:
                all_values.append(value + addition)
        all_values.sort()
        print("Results:", all_values)
        return all_values

    def set_memory(self, address, value):
        self.memory[address] = value
        print("Memory at", address, "set to", value)

    def set_memory_v2(self, addresses, value):
        for address in addresses:
            self.memory[address] = value
        # print("Memory at", address, "set to", value)

    def sum_all_memory(self):
        sum_of_memory = 0
        for value in self.memory.values():
            sum_of_memory += value
        return sum_of_memory

    def execute_next_command(self):
        command_name, command_context, command_value = self.get_next_command()
        if command_name == "mask":
            self.set_bitmask(command_value)
        else:
            masked_value = self.apply_bitmask(command_value)
            self.set_memory(command_context, masked_value)

    def execute_next_command_v2(self):
        command_name, command_context, command_value = self.get_next_command()
        if command_name == "mask":
            self.set_bitmask(command_value)
        else:
            masked_values = self.apply_bitmask_v2(command_context)
            self.set_memory_v2(masked_values, command_value)

    def execute_all_commands(self):
        if self.version == "v1":
            while len(self.commands) > 0:
                self.execute_next_command()
        else:
            while len(self.commands) > 0:
                self.execute_next_command_v2()
        return self.sum_all_memory()


bit_mask_program = BitMask("input14.txt", "v2")
result = bit_mask_program.execute_all_commands()
print(result)



