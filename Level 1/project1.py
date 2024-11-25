import math

def operation():
    mes = input("Choose operation (+, -, *, /): ")
    correct_operations = ['+', '-', '*', '/']
    while mes not in correct_operations:
        print('Operation does not exist')
        mes = input()
    return mes

def summ(first, second):
    return first + second

def sub(first, second):
    return first - second

def div(first, second):
    return first / second

def mult(first, second):
    return first * second

def calc(first, second, oper):

    result = None

    if oper == '+':
        result = summ(first, second)

    elif oper == '-':
        result = sub(first, second)

    elif oper == '*':
        result = mult(first, second)

    elif oper == '/':
        if second == 0:
            print('Division by 0 is not allowed')
            exit (1)
        result = div(first, second)
    else:
        print('Incorrect operation!')

    return result

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def run():

    first = get_int_input("Enter first number: ")

    second = get_int_input("Enter second number: ")

    oper = operation()

    result = calc(first, second, oper)

    if result is not None:
        print('Result: ', result)

run()