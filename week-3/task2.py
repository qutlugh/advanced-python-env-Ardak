import math

def calculate_equilateral_triangle_area(side):
    return (math.sqrt(3) / 4) * (side ** 2)

def solve_hexagon_task():
    print("\n=== Part 1: Hexagon Area via Triangle Subroutine ===")
    try:
        a = float(input("Enter the side length (a) of the regular hexagon: "))
        
        triangle_area = calculate_equilateral_triangle_area(a)
        hexagon_area = 6 * triangle_area
        
        print(f"Area of one triangle: {triangle_area:.2f}")
        print(f"Total Area of Hexagon (6 * triangle): {hexagon_area:.2f}")
        
    except ValueError:
        print("Please enter a valid number.")

def solve_rectangles_task():
    print("\n=== Part 2: Area of 3 Rectangles ===")
    
    for i in range(1, 4):
        print(f"\nRectangle {i}:")
        try:
            side1 = float(input(f"  Enter side 1: "))
            side2 = float(input(f"  Enter side 2: "))
            
            area = side1 * side2
            print(f"  -> Area of Rectangle {i}: {area:.2f}")
            
        except ValueError:
            print("  Invalid input. Skipping this rectangle.")

if __name__ == "__main__":
    solve_hexagon_task()
    solve_rectangles_task()