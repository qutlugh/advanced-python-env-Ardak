def smart_calculator_with_zero_check():
    print("--- Task 6 & 7: Smart Calculator with Zero Check ---")
    
    try:
        num1 = float(input("First number: "))
        operation = input("Operation (+, -, *, /): ").strip()
        num2 = float(input("Second number: "))
    except ValueError:
        print("Error: Invalid input for numbers.")
        return

    result = None
    
    if operation == '+':
        result = num1 + num2
        
    elif operation == '-':
        result = num1 - num2
        
    elif operation == '*':
        result = num1 * num2
        
    elif operation == '/':
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
            
    else:
        result = f"Error: Invalid operation '{operation}'."

    if isinstance(result, (int, float)):
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    else:
        print(f"\n{result}")

smart_calculator_with_zero_check()