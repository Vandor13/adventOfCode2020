with open("input6.txt") as file:
    answers = file.readlines()
no_answers = 0
answer_set = set()
set_active = False

for answer in answers:
    if str(answer) == "\n":
        print("This group answered", str(len(answer_set)), "questions with yes")
        no_answers += len(answer_set)
        answer_set = set()
        set_active = False
    else:
        new_set = set(str(answer))
        if set_active:
            answer_set = answer_set.intersection(new_set)
        else:
            answer_set = new_set
            set_active = True
        answer_set.discard("\n")
        print(answer_set)
print("This group answered", str(len(answer_set)), "questions with yes")
no_answers += len(answer_set)
answer_set = set()


print("Total answers:", no_answers)