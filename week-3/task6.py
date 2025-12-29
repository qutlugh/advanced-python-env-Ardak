import math

def get_gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve_gcd_lcm_task():
    print("=== Part 1: GCD and LCM Calculator ===")
    try:
        num1 = int(input("Enter first natural number (A): "))
        num2 = int(input("Enter second natural number (B): "))

        if num1 <= 0 or num2 <= 0:
            print("Please enter natural numbers     (integers > 0).")
            return

        gcd = get_gcd_euclid(num1, num2)

        lcm = (num1 * num2) // gcd

        print(f"\nResults for {num1} and {num2}:")
        print(f" - Greatest Common Divisor (GCD): {gcd}")
        print(f" - Least Common Multiple (LCM):   {lcm}")

    except ValueError:
        print("Invalid input. Please enter integers.")

def calculate_triangle_area(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 0  # Invalid triangle
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def solve_quadrilateral_area():
    print("\n=== Part 2: Area of Convex Quadrilateral ===")
    print("A diagonal splits a quadrilateral into two triangles.")
    
    try:
        diagonal = float(input("Enter the length of the diagonal: "))
        
        print("--- First Triangle (formed by diagonal and 2 sides) ---")
        side1 = float(input("Enter side 1: "))
        side2 = float(input("Enter side 2: "))
        
        print("--- Second Triangle (formed by diagonal and other 2 sides) ---")
        side3 = float(input("Enter side 3: "))
        side4 = float(input("Enter side 4: "))

        area1 = calculate_triangle_area(side1, side2, diagonal)
        area2 = calculate_triangle_area(side3, side4, diagonal)

        if area1 == 0 or area2 == 0:
            print("\nError: The sides provided cannot form a valid triangle with the given diagonal.")
        else:
            total_area = area1 + area2
            print(f"\nTotal Area of Quadrilateral: {total_area:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    solve_gcd_lcm_task()
    solve_quadrilateral_area()