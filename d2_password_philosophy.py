with open("input2.txt", "r") as input_file:
    input_lines = input_file.readlines()
number_of_correct_passwords = 0
for line in input_lines:
    amounts, letter, password = line.split()
    low_amount, high_amount = amounts.split("-")
    letter = str(letter).strip(":")
    password = str(password)
    actual_amount = password.count(letter)
    print(low_amount, high_amount, letter, password)
    print(int(low_amount) <= actual_amount <= int(high_amount))
    if int(low_amount) <= actual_amount <= int(high_amount):
        number_of_correct_passwords += 1
print(number_of_correct_passwords)