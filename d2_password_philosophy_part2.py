with open("input2.txt", "r") as input_file:
    input_lines = input_file.readlines()
number_of_correct_passwords = 0
for line in input_lines:
    amounts, letter, password = line.split()
    first_index, second_index = amounts.split("-")
    letter = str(letter).strip(":")
    password = str(password)
    actual_amount = password.count(letter)
    print(first_index, second_index, letter, password)
    if (password[int(first_index)-1] == letter) ^ (password[int(second_index)-1] == letter):
        number_of_correct_passwords += 1
        print("True")
    else:
        print("False")
print(number_of_correct_passwords)