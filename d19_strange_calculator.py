def read_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        expressions = [line.rstrip("\n").replace("(", "( ").replace(")", " )") for line in file.readlines()]
    return expressions


def process_expression(expression: str) -> int:
    expression_parts = expression.split(" ")
    return process_expression_parts(expression_parts)


def process_expression_parts(expression_parts: list) -> int:
    result = None
    operation = None
    while expression_parts:
        part = expression_parts.pop(0)
        # Operations
        if part == "*" or part == "+":
            operation = part
        # Sub-results
        else:
            if part == "(":
                index_of_closing_bracket = get_index_for_closing_parant(expression_parts)
                sub_result = process_expression_parts(expression_parts[:index_of_closing_bracket])
                expression_parts = expression_parts[index_of_closing_bracket + 1:]
            else:
                sub_result = int(part)
            if not result:
                result = sub_result
            else:
                if operation == "+":
                    result += sub_result
                else:
                    result *= sub_result
    return result


def get_index_for_closing_parant(expression_parts: list) -> int: #returns the index of closing brackets
    no_of_other_open_brackets = 0
    for i in range(len(expression_parts)):
        if expression_parts[i] == "(":
            no_of_other_open_brackets += 1
        elif expression_parts[i] == ")":
            if no_of_other_open_brackets == 0:
                return i
            else:
                no_of_other_open_brackets -= 1
    return None  # Error Case, should not hapen with correct expressions


def calculate_all_results(expressions: list):
    sum_of_expressions = 0
    for expression in expressions:
        expression_result = process_expression(expression)
        print(expression, "becomes", expression_result)
        sum_of_expressions += expression_result
    print("Sum of all expressions:", sum_of_expressions)


expression_list = read_file("input18.txt")
calculate_all_results(expression_list)
