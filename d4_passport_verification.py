import re

def read_file() -> list:
    passports = []
    with open("input4.txt", "r") as file:
        passport_dictionary = {}
        lines = file.readlines()
        for line in lines:
            print(line)
            if line == "\n":
                print("empty line detected")
                passports.append(passport_dictionary)
                passport_dictionary = {}
            else:
                print("data:")
                items = str(line).split()
                for item in items:
                    key, value = item.split(":")
                    passport_dictionary[key] = value
    if passport_dictionary:
        passports.append(passport_dictionary)
    print(passports)
    return passports


def check_passport(passport_dictionary: dict, check_values: list) -> bool:
    # Check Birth Year
    if not passport_dictionary.get("byr") or \
        not (1920 <= int(passport_dictionary.get("byr")) <= 2002):
        return False
    # Check Issue Year
    if not passport_dictionary.get("iyr") or \
        not (2010 <= int(passport_dictionary.get("iyr")) <= 2020):
        return False
    # Check Expiration Year
    if not passport_dictionary.get("eyr") or \
        not (2020 <= int(passport_dictionary.get("eyr")) <= 2030):
        return False
    # Check Height
    if passport_dictionary.get("hgt"):
        height = str(passport_dictionary.get("hgt"))
        if "cm" in height:
            height_value = int(height.strip("cm"))
            if not (150 <= height_value <= 193):
                return False
        elif "in" in height:
            height_value = int(height.strip("in"))
            if not (59 <= height_value <= 76):
                return False
        else:
            return False
    else:
        return False
    if passport_dictionary.get("hcl"):
        hair_color = str(passport_dictionary.get("hcl"))
        regex = re.compile('#[0-9a-f]+')
        if not len(hair_color) == 7 or not regex.match(hair_color):
            return False
    else:
        return False
    if passport_dictionary.get("ecl"):
        eye_color = str(passport_dictionary.get("ecl"))
        if eye_color not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
    else:
        return False
    if passport_dictionary.get("pid"):
        pass_id = str(passport_dictionary.get("pid"))
        if len(pass_id) != 9 or not pass_id.isnumeric():
            return False
    else:
        return False

    return True




dictionaries = read_file()
number_correct_passports = 0
values = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for passport in dictionaries:
    if check_passport(passport, values):
        number_correct_passports += 1
print(number_correct_passports)
