line = input().split()
n = int(line[0])
m = int(line[1]) 
text = input() 
found_words = [] 
for i in range(n - m + 1):
    word = text[i : i + m] 
    if word not in found_words:
        found_words.append(word)

print(len(found_words))