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
        adjacent_rows = [x for x in range(row-1, row+2) if (0 <= x < no_rows)]
        # print("For row:", row, "Adjacent Rows:", [x for x in range(row-1, row+2) if (0 <= x < no_rows)])
        for column in range(no_columns):
            adjacent_columns = [x for x in range(column-1, column+2) if (0 <= x < no_columns)]
            # print("For column", column, "Adjacent Columns:", [x for x in range(column-1, column+2) if (0 <= x < no_columns)])
            for row2 in adjacent_rows:
                for column2 in adjacent_columns:
                    if (row2 != row or column2 != column) and (seats[row2][column2] == occupied_seat):
                        no_adjacent_occupied_seats[row][column] += 1
    # print(no_adjacent_occupied_seats)
    return no_adjacent_occupied_seats


def calculate_next_seat_matrix(seats: list, adjacent_occupation: list) -> [list, bool]:
    matrix_changed = False
    for row in range(len(seats)):
        for column in range(len(seats[0])):
            if seats[row][column] == empty_seat and adjacent_occupation[row][column] == 0:
                seats[row][column] = occupied_seat
                matrix_changed = True
            elif seats[row][column] == occupied_seat and adjacent_occupation[row][column] >= 4:
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
