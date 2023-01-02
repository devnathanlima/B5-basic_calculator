def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue == True:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the number?: "))
        calculation_function = operations[operation_symbol]
        total = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {total}")

        again = input("Do you want to calc more with Answer? Continue/Y/N ")
        if again == "Continue":
            num1 = total
        elif again == "Y":
            should_continue = False
            calculator()
        else:
            break


calculator()
