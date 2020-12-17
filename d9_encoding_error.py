def check_number(number: int, preamble: list) -> bool:
    print("Checking", number, "with Preamble", preamble)
    for i in range(len(preamble) - 1):
        # print("index i", i)
        current_number = preamble[i]
        for j in range(i + 1, len(preamble)):
            # print("index j", i)
            # print("Trying", current_number, "plus", preamble[j])
            if number == current_number + preamble[j]:
                print(number, "is the sum of", current_number, "and", preamble[j])
                return True
    print(number, "is incorrect")
    return False


def find_incorrect_number(numbers: list, preamble_size: int) -> int:
    numbers, preamble = initialize_preamble(numbers, preamble_size)
    for _ in range(len(numbers)):
        number = numbers.pop(0)
        if not check_number(number, preamble):
            return number
        else:
            preamble.append(number)
            # print(preamble)
            preamble.pop(0)
            # print(preamble)
    return None


def initialize_preamble(numbers: list, amount: int) -> [list, list]:
    preamble_list = []
    for _ in range(amount):
        number = numbers.pop(0)
        preamble_list.append(number)
    print("Preamble:", preamble_list)
    return numbers, preamble_list


def find_set(number: int, numbers: list):
    while len(numbers) > 0:
        print("Searching for sum in ", numbers)
        current_number = numbers[0]
        sum_sum = current_number
        if current_number == number:
            trash = numbers.pop(0)
            continue
        for i in range(1, len(numbers)):
            sum_sum += numbers[i]
            if sum_sum == number:
                solution = numbers[:i+1]
                print("Found set:", solution)
                minimum = min(solution)
                maximum = max(solution)
                print("Min:", minimum, "Max:", maximum)
                print("Sum:", minimum + maximum)
                numbers = []
                exit()
            elif sum_sum > number:
                break
        trash = numbers.pop(0)



with open("input9.txt", "r") as file:
    number_list = [int(x) for x in file.readlines()]
# number_list.reverse()
incorrect_number = find_incorrect_number(number_list.copy(), 25)
find_set(incorrect_number, number_list)

