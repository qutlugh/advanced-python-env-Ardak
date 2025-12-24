def smart_calculator():
    print("--- Smart Calculator ---")
    
    while True:
        try:
            num1 = float(input("First number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        operation = input("Operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation. Please enter one of these: +, -, *, /.")

    while True:
        try:
            num2 = float(input("Second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    result = None
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
            return 
        result = num1 / num2

    print(f"\nResult: {num1} {operation} {num2} = {result}")

smart_calculator()