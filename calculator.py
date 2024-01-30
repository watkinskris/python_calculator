from calculator_art import logo


def add(a, b):
    """add(a,b) takes two ints and returns their sum"""
    sum_total = a + b
    return sum_total


def subtract(a, b):
    """subtract(a,b) takes two ints and returns the difference"""
    dif = a - b
    return dif


def multiply(a, b):
    """multiply(a,b) takes two ints and returns their product"""
    product = a * b
    return product


def divide(a, b):
    """division(a,b) takes two ints and returns their quotient"""
    while b == 0:
        print("Division by 0 is not allowed. ")
        b = int(input("Pick another number: "))
    quotient = a / b
    return quotient


continue_calc = False
another_calc = True
total = 0

print(logo)
while another_calc:
    if not continue_calc:
        num1 = int(input("Enter a number: "))
    else:
        num1 = total
    num2 = int(input("Enter another number: "))
    operation = input("Enter the operator ( + - * / ): ")
    # check to see if it is division by 0
    if num2 == 0 and operation == "/":
        while num2 == 0:
            print("Division by 0 is not allowed. ")
            num2 = int(input("Pick another number: "))

    # picking correct function
    if operation == "+":
        total = add(num1, num2)
    elif operation == "-":
        total = subtract(num1, num2)
    elif operation == "*":
        total = multiply(num1, num2)
    elif operation == "/":
        total = divide(num1, num2)

    print(f"The total of {num1} {operation} {num2} is: {total}")
    user_calc_choice = input("Do you want to continue this calculation ('y' or 'n'): ")
    if user_calc_choice == 'y':
        continue_calc = True
    else:
        user_choice = input("Do you want to perform a new calculation ('y' or 'n'): ")
        if user_choice == 'n':
            another_calc = False
            print("Goodbye")
        else:
            continue_calc = False
            total = 0
