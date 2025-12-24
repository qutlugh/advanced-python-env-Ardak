def check_lucky_ticket():
    print("--- Task 9: Lucky ticket ---")
    
    while True:
        ticket_number_str = input("Enter a six-digit ticket number (e.g., 385916): ")
        
        if ticket_number_str.isdigit() and len(ticket_number_str) == 6:
            break
        else:
            print("Invalid input. Please enter exactly six digits.")

    first_half = ticket_number_str[0:3]
    second_half = ticket_number_str[3:6]
    
    sum_first = sum(int(digit) for digit in first_half)
    
    sum_second = sum(int(digit) for digit in second_half)
    
    if sum_first == sum_second:
        print("\nYES")
    else:
        print("\nNO")

check_lucky_ticket()