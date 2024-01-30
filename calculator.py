from calculator_art import logo


def add(a, b):
    """add(a,b) takes two ints and returns their sum"""
    return a + b


def subtract(a, b):
    """subtract(a,b) takes two ints and returns the difference"""
    return a - b


def multiply(a, b):
    """multiply(a,b) takes two ints and returns their product"""
    return a * b


def divide(a, b):
    """division(a,b) takes two ints and returns their quotient"""
    while b == 0:
        print("Division by 0 is not allowed. ")
        b = int(input("Pick another number: "))
    quotient = a / b
    return quotient

def choose_operator(op_dict):
    for symbol in op_dict:
        print(symbol)
    user_operator = input("Pick an operation from the list above: ")
    return user_operator

def division_by_0(a, symbol):
    while a == 0 and symbol == "/":
        print("Division by 0 is not allowed. ")
        a = int(input("Pick another number: "))
    return a


continue_calc = True
total = 0
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
print(logo)
num1 = int(input("Enter a number: "))
while continue_calc:
    operator = choose_operator(operations)
    num2 = int(input("Enter another number: "))
    # check to see if it is division by 0
    num2 = division_by_0(num2, operator)

    function = operations[operator]
    total = function(num1, num2)

    print(f"The total of {num1} {operator} {num2} is: {total}")
    user_calc_choice = input("Do you want to continue this calculation ('y' or 'n'): ")
    if user_calc_choice == 'n':
        continue_calc = False
    else:
        num1 = total
