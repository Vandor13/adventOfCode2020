def read_input(file_name) -> list:
    with open(file_name) as file:
        return file.readlines()


def interpret_instruction(instruction: str, index: int, accumulator) -> [int, int]:
    command, raw_number = instruction.split()
    number = int(raw_number)
    print("Executing line", str(index), "with command", command, "and number", str(number))
    if command == "nop":
        return accumulator, index + 1
    elif command == "acc":
        return accumulator + number, index + 1
    else:
        return accumulator, index + number


def run_instructions(instructions: list) -> [bool, int]:
    loop_found = False
    instruction_index = 0
    accumulator = 0
    visited_instructions = set()
    error_found = False
    while True:
        instruction = instructions[instruction_index]
        visited_instructions.add(instruction_index)
        accumulator, instruction_index = interpret_instruction(str(instruction), instruction_index, accumulator)
        if instruction_index == len(instructions):
            error_found = False
            break
        elif instruction_index in visited_instructions :
            error_found = True
            print("Found loop")
            break
        elif instruction_index > len(instructions) or instruction_index < 0:
            error_found = True
            print("Jumped too far")
            break
    if error_found:
        print("Before error accumulator is:", str(accumulator))
    return error_found, accumulator

def try_changing_line(instructions: list):
    changed_index = None
    for i in range(len(instructions)):
        changed_instructions = instructions.copy()
        instruction = str(instructions[i])
        if instruction.startswith("nop"):
            changed_instructions[i] = "jmp" + instruction[3:]
            print("Changed line", str(i), "from nop to jmp")
        elif instruction.startswith("jmp"):
            changed_instructions[i] = "nop" + instruction[3:]
            print("Changed line", str(i), "from jmp to nop")
        else:
            continue
        error_found, accumulator = run_instructions(changed_instructions)
        if error_found:
            print("Trying next index \n")
        else:
            print("Solution found with changed line", str(i), "and accumulator", str(accumulator))
            break


instructions_list = read_input("input8.txt")
# run_instructions(instructions_list)
try_changing_line(instructions_list)

