import math

def calculate_shape_area():
    print("\n=== Part 1: Geometric Shapes ===")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    try:
        choice = int(input("Choose a shape (1-3): "))
        
        if choice == 1:
            r = float(input("Enter radius: "))
            area = math.pi * (r ** 2)
            print(f"Result: Area of Circle = {area:.2f}")
            
        elif choice == 2:
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            area = w * h
            print(f"Result: Area of Rectangle = {area:.2f}")
            
        elif choice == 3:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = 0.5 * b * h
            print(f"Result: Area of Triangle = {area:.2f}")
            
        else:
            print("Invalid selection.")
            
    except ValueError:
        print("Error: Please enter numbers only.")

def process_arrays():
    print("\n=== Part 2: Array Statistics ===")
    arrays = [
        [10, 20, 30, 40, 50],            
        [3, 1, 4, 1, 5, 9, 2, 6, 5],   
        [7, 7, 7]                        
    ]

    for i, arr in enumerate(arrays, 1):
        total = sum(arr)
        mean = total / len(arr)
        
        print(f"Array {i}: {arr}")
        print(f" - Sum: {total}")
        print(f" - Arithmetic Mean: {mean:.2f}")
        print("-" * 20)

if __name__ == "__main__":
    calculate_shape_area()
    
    process_arrays()