def is_divisible_by_digits(num):
    temp = num
    while temp > 0:
        digit = temp % 10
        
        if digit == 0:
            return False
            
        if num % digit != 0:
            return False
            
        temp //= 10
        
    return True

def solve_divisible_numbers_task():
    print("=== Part 1: Numbers Divisible by Their Digits ===")
    try:
        n = int(input("Enter natural number n: "))
        
        print(f"Numbers <= {n} divisible by their digits:")
        results = []
        
        for i in range(1, n + 1):
            if is_divisible_by_digits(i):
                results.append(i)
                
        print(*results)
        
    except ValueError:
        print("Invalid input. Please enter a natural number.")

def swap_first_last(arr):
    """
    Procedure to swap the first and last elements of an array.
    Since lists in Python are mutable, this changes the original list directly.
    """
    if len(arr) < 2:
        return 
        
    arr[0], arr[-1] = arr[-1], arr[0]

def solve_array_swap_task():
    print("\n=== Part 2: Swap First and Last Array Elements ===")
    try:
        m = int(input("Enter the length of the array (m): "))
        
        if m <= 0:
            print("Length must be greater than 0.")
            return

        print(f"Enter {m} elements separated by space (or press Enter after each):")
        raw_input = input().split()
        
        while len(raw_input) < m:
            raw_input.extend(input().split())
            
        array_a = [int(x) for x in raw_input[:m]]
        
        print(f"Original Array:  {array_a}")
        
        swap_first_last(array_a)
        
        print(f"Resulting Array: {array_a}")

    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    solve_divisible_numbers_task()
    solve_array_swap_task()