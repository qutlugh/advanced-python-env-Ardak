def little_game():
    print("--- Task 8: A little game ---")
    
    word = input("Enter a word: ")
    
    while True:
        try:
            repeat_count = int(input("Enter a number (repetitions): "))
            if repeat_count >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    print("\n# Result")
    
    for char in word:
        repeated_char = char * repeat_count
        print(repeated_char)

little_game()