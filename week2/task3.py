s = input()
if s[0] == 'x':
    b = int(s[2]) 
    c = int(s[4])
    
    if s[1] == '+':
        print(c - b) 
    else:
        print(c + b) 
elif s[2] == 'x':
    a = int(s[0])
    c = int(s[4])
    
    if s[1] == '+':
        print(c - a)
    else:
        print(a - c)
else:
    a = int(s[0])
    b = int(s[2])
    
    if s[1] == '+':
        print(a + b)
    else:
        print(a - b)