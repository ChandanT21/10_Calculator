import math


def add(a, b):
    """
    :param a: input value 1
    :param b: input value 2
    :return: sum of input value 1 & input value 2
    """
    return a + b


def subtract(a, b):
    """
    :param a: input value 1
    :param b: input value 2
    :return: difference between value 1 & value 2
    """
    return a - b


def multiply(a, b):
    """
    :param a: input value 1
    :param b: input value 2
    :return: product of value 1 & value 2
    """
    return a * b


def divide(a, b):
    """
    :param a: input value 1
    :param b: input value 2
    :return: factor of value 1 from value 2
    """
    return round(a / b)


def launch():
    calculate = True
    input_1 = ''
    result_val = {"result": ''}

    while calculate:
        if result_val["result"] == '':
            input_1 = float(input("What's the first number: "))
        else:
            input_1 = result_val["result"]

        option = input("Operation to choose from: + - * / \nEnter an operation: ")
        input_2 = float(input("What's the next number: "))

        operation = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide}

        calc_funct = operation[option]
        result_val["result"] = calc_funct(input_1, input_2)

        print(f"\n{input_1} {option} {input_2} = {result_val['result']}\n")

        reset_result = input(f"Type 'y' to continue calculating with {result_val['result']}, "
                             f"or type 'n' to start a new calculation.")
        if reset_result == 'n':
            result_val["result"] = ''

