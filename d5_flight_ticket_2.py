def get_seat_number(ticket: str) -> int:
    row_floor, row_ceil = 0, 127
    for i in range(7):
        print("row_floor " + str(row_floor) + " row_ceil " + str(row_ceil) + " Next Letter: " + ticket[i])
        new_limit = (row_floor + row_ceil) // 2
        if ticket[i] == "F":
            row_ceil = new_limit
        else:
            row_floor = new_limit + 1
    row_number = row_floor
    seat_floor, seat_ceil = 0, 7
    for i in range(7, 10):
        new_limit = (seat_floor + seat_ceil) // 2
        if ticket[i] == "L":
            seat_ceil = new_limit
        else:
            seat_floor = new_limit + 1
    seat_number = seat_floor
    print("Row:", str(row_number), "Seat:", str(seat_number))
    return row_number * 8 + seat_number


def find_empty_seat(tickets: list) -> int:
    taken_seats = []
    for ticket in tickets:
        taken_seats.append(get_seat_number(str(ticket)))
    taken_seats.sort()
    for seat in taken_seats:
        if (seat + 1) not in taken_seats and (seat + 2) in taken_seats:
            return seat + 1

with open("input5.txt", "r") as file:
    tickets = file.readlines()
print(find_empty_seat(tickets))

# print(get_seat_number("FBFBBFFRLR"))  # 357
# print(get_seat_number("BFFFBBFRRR"))  # 567
# print(get_seat_number("FFFBBBFRRR"))  # 119
# print(get_seat_number("BBFFBBFRLL"))  # 820

