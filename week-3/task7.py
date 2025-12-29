import math

def calculate_right_triangle_area(leg1, leg2):
    return 0.5 * leg1 * leg2

def calculate_general_triangle_area(a, b, c):
    s = (a + b + c) / 2
    
    if s <= a or s <= b or s <= c:
        return 0 # Invalid triangle
        
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def solve_quadrilateral_task():
    print("=== Part 1: Area of Quadrilateral ===")
    print("Given sides X, Y, Z, T (Angle between X and Y is 90 degrees).")
    
    try:
        x = float(input("Enter side X: "))
        y = float(input("Enter side Y: "))
        z = float(input("Enter side Z: "))
        t = float(input("Enter side T: "))

        if x <= 0 or y <= 0 or z <= 0 or t <= 0:
            print("Sides must be positive numbers.")
            return

        area1 = calculate_right_triangle_area(x, y)
        
        diagonal = math.sqrt(x**2 + y**2)
        
        area2 = calculate_general_triangle_area(z, t, diagonal)

        if area2 == 0:
            print("\nError: Sides Z, T and the Diagonal cannot form a closed triangle.")
        else:
            total_area = area1 + area2
            print(f"\nDiagonal length: {diagonal:.2f}")
            print(f"Area of Right Triangle (X,Y): {area1:.2f}")
            print(f"Area of Second Triangle (Z,T,Diag): {area2:.2f}")
            print(f"Total Area: {total_area:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers.")
def solve_octal_task():
    print("\n=== Part 2: Octal Code Converter ===")
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Please enter a non-negative integer.")
            return
        octal_string = f"{num:010o}"
        
        print(f"Octal representation (10 digits): {octal_string}")
        
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    solve_quadrilateral_task()
    solve_octal_task()