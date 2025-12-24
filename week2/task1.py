s = input()
k = 0 
for i in range(len(s) - 4):
    sub = s[i : i+5]
    if sub == ">>-->":
        k += 1
    elif sub == "<--<<":
        k += 1

print(k)