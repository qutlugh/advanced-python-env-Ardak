items = input().split()
counts = {}
for x in items:
    if x not in counts:
        counts[x] = 0
    counts[x] += 1
print("Purchase frequency:")
for x in counts:
    print(x + ":", counts[x])
most_popular = ""
max_count = 0
for x in counts:
    if counts[x] > max_count:
        max_count = counts[x]
        most_popular = x
print("\nMost popular item:", most_popular)
print("\nPurchased once:", end=" ")
for x in counts:
    if counts[x] == 1:
        print(x, end=" ")
print()
pairs = []
for x in counts:
    pairs.append([counts[x], x])
pairs.sort(reverse=True)
print("\nSorted by frequency:")
for p in pairs:
    print(p[1], p[0])   