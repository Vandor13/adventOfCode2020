empty_seat = "L"
occupied_seat = "#"
floor = "."


def read_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        lines = file.readlines()
    matrix = []
    for line in lines:
        line.rstrip()
        matrix.append([symbol for symbol in line if symbol != "\n"])
    return matrix


def calculate_occupied_seat(seats: list) -> list:
    no_adjacent_occupied_seats = [[0 for seat in row] for row in seats]
    no_rows = len(seats)
    no_columns = len(seats[0])
    for row in range(no_rows):
        for column in range(no_columns):
            for row_dif in [-1, 0, 1]:
                for column_dif in [-1, 0, 1]:
                    if (row_dif != 0 or column_dif != 0) and occupied_seat_in_direction(seats, row, column, row_dif, column_dif):
                        no_adjacent_occupied_seats[row][column] += 1
    return no_adjacent_occupied_seats


def occupied_seat_in_direction(seats, start_row, start_column, row_dif, column_dif) -> bool:
    no_rows = len(seats)
    no_columns = len(seats[0])
    row = start_row + row_dif
    column = start_column + column_dif
    while in_bounds(no_rows, no_columns, row, column):
        if seats[row][column] == occupied_seat:
            return True
        elif seats[row][column] == empty_seat:
            return False
        row += row_dif
        column += column_dif
    return False


def in_bounds(no_rows, no_columns, row, column) -> bool:
    if 0 <= row < no_rows and 0 <= column < no_columns:
        return True
    else:
        return False


def calculate_next_seat_matrix(seats: list, adjacent_occupation: list) -> [list, bool]:
    matrix_changed = False
    for row in range(len(seats)):
        for column in range(len(seats[0])):
            if seats[row][column] == empty_seat and adjacent_occupation[row][column] == 0:
                seats[row][column] = occupied_seat
                matrix_changed = True
            elif seats[row][column] == occupied_seat and adjacent_occupation[row][column] >= 5:
                seats[row][column] = empty_seat
                matrix_changed = True
    return [seats, matrix_changed]


def print_seat_matrix(seats: list):
    for row in seats:
        print(''.join(row))


seat_matrix = read_file("input11.txt")
print_seat_matrix(seat_matrix)
was_changed = True
while was_changed:
    occupation_matrix = calculate_occupied_seat(seat_matrix)
    print(occupation_matrix)
    seat_matrix, was_changed = calculate_next_seat_matrix(seat_matrix, occupation_matrix)
    print_seat_matrix(seat_matrix)
sum_of_occupied_seats = 0
for row_no in seat_matrix:
    for seat_no in row_no:
        if seat_no == occupied_seat:
            sum_of_occupied_seats += 1
print("Number of occupied seats:", sum_of_occupied_seats)
