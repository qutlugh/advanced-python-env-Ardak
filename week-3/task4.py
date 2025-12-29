import math

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve_fraction_task():
    print("--- Part 1: Divide Fractions (A/B) / (C/D) ---")
    try:
        print("Fraction 1 (A/B):")
        a = int(input("  Enter numerator A: "))
        b = int(input("  Enter denominator B: "))
        
        print("Fraction 2 (C/D):")
        c = int(input("  Enter numerator C: "))
        d = int(input("  Enter denominator D: "))

        if b == 0 or d == 0 or c == 0:
            print("Error: Denominators (and numerator C) cannot be zero.")
            return
        
        res_numerator = a * d
        res_denominator = b * c

        common_divisor = get_gcd(res_numerator, res_denominator)
        
        final_num = res_numerator // common_divisor
        final_den = res_denominator // common_divisor

        print(f"\nResult: {final_num}/{final_den}")
        
    except ValueError:
        print("Please enter valid integers.")

def is_point_inside(x, y, cx, cy, r):
    distance_squared = (x - cx)**2 + (y - cy)**2
    radius_squared = r**2
    
    if distance_squared < radius_squared:
        return True
    else:
        return False

def solve_circle_task():
    print("\n--- Part 2: Points Inside a Circle ---")
    try:
        print("Enter Circle Properties:")
        cx = float(input("  Center X (a): "))
        cy = float(input("  Center Y (b): "))
        r = float(input("  Radius (R): "))

        points_inside_count = 0
        point_names = ['P', 'F', 'L']
        
        for name in point_names:
            print(f"\nEnter coordinates for point {name}:")
            px = float(input(f"  {name}_x: "))
            py = float(input(f"  {name}_y: "))
            
            if is_point_inside(px, py, cx, cy, r):
                print(f"  -> Point {name} is INSIDE the circle.")
                points_inside_count += 1
            else:
                print(f"  -> Point {name} is OUTSIDE (or on the edge).")

        print(f"\nTotal points inside the circle: {points_inside_count}")

    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    solve_fraction_task()
    solve_circle_task()