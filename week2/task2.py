a = input()
b = input()
len_a = len(a)
len_b = len(b)
count = 0
shifts = []
for i in range(len_b):
    s = b[i:] + b[:i]
    shifts.append(s)
for i in range(len_a - len_b + 1):
    sub = a[i : i + len_b] 
    if sub in shifts:
        count += 1
print(count)