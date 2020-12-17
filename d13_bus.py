from functools import reduce

def parse_file(file_name: str) -> [int, list]:
    with open(file_name, "r") as file:
        departure_time = int(file.readline())
        bus_ids = file.readline().split(",")
    return [departure_time, bus_ids]


def find_best_bus(departure_time: int, bus_ids: list) -> int:
    bus_ids = [int(id_string) for id_string in bus_ids if id_string != "x"]
    best_wait_time = None
    best_bus = None
    for bus_id in bus_ids:
        multiplicand = departure_time // bus_id + 1
        wait_time = bus_id * multiplicand - departure_time
        if not best_wait_time or wait_time < best_wait_time:
            best_wait_time = wait_time
            best_bus = bus_id
    return best_bus * best_wait_time


def find_strange_timestamp(bus_ids: list):
    modulos = []
    remainders = []
    ids = []
    for i in range(len(bus_ids)):
        if bus_ids[i] == "x":
            continue
        modulos.append(int(bus_ids[i]))
        if 10 != 10:
            remainders.append(0)
        else:
            remainders.append((int(bus_ids[i]) - i) % int(bus_ids[i]))
        ids.append(i)
    print(modulos)
    print(remainders)
    print(ids)
    return chinese_remainder(modulos, remainders)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


departure, bus_id_list = parse_file("input13.txt")
print("Best bus:", find_best_bus(departure, bus_id_list))
print("Strange timestamp:", find_strange_timestamp(bus_id_list))
# cr = chinese_remainder([7, 13, 59, 31, 19], [0, 12, 55, 25, 12])
# print(cr)
