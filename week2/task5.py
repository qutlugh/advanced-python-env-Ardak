n = int(input())
valid_letters = "ABCEHKMOPTXY"
digits = "0123456789"

for i in range(n):
    s = input()
    if len(s) != 6:
        print("No")
    else:
        is_good = True
        if s[0] not in valid_letters:
            is_good = False
        if s[1] not in digits:
            is_good = False
        if s[2] not in digits:
            is_good = False
        if s[3] not in digits:
            is_good = False
        if s[4] not in valid_letters:
            is_good = False
        if s[5] not in valid_letters:
            is_good = False
        if is_good:
            print("Yes")
        else:
            print("No")