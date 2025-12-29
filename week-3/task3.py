import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def solve_hypotenuse_task():
    print("=== Part 1: Compare Hypotenuses ===")
    
    print("Triangle 1:")
    leg1_a = float(input("  Enter leg 1: "))
    leg1_b = float(input("  Enter leg 2: "))
    hyp1 = calculate_hypotenuse(leg1_a, leg1_b)
  
    print("Triangle 2:")
    leg2_a = float(input("  Enter leg 1: "))
    leg2_b = float(input("  Enter leg 2: "))
    hyp2 = calculate_hypotenuse(leg2_a, leg2_b)
    
    print(f"\nHypotenuse of Triangle 1: {hyp1:.2f}")
    print(f"Hypotenuse of Triangle 2: {hyp2:.2f}")
    
    if hyp1 > hyp2:
        print("Result: Triangle 1 has the larger hypotenuse.")
    elif hyp2 > hyp1:
        print("Result: Triangle 2 has the larger hypotenuse.")
    else:
        print("Result: Both triangles have equal hypotenuses.")

def solve_string_sort_task():
    print("\n=== Part 2: Sort Letters in Each Word ===")
    
    text = input("Enter a sentence: ")
    
    words = text.split()
    
    processed_words = []
    
    for word in words:
        sorted_word = "".join(sorted(word))
        processed_words.append(sorted_word)
    
    result = " ".join(processed_words)
    
    print(f"Original: {text}")
    print(f"Converted: {result}")

if __name__ == "__main__":
    solve_hypotenuse_task()
    solve_string_sort_task()