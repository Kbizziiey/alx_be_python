first_number = int(input("Enter the first number: ").strip())
second_number = int(input("Enter the second number: ").strip())
operator = input("Choose the operation (+, -, *, /): ").strip()

match operator:
    case "+":
        print("The result is",first_number + second_number)
    case "-":
        print("The result is",first_number - second_number)
    case "*":
        print("The result is",first_number * second_number)
    case "/":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is",first_number / second_number)
    case _:
        print("Not an operation")
