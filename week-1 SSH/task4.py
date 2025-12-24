N = int(input())
if N >= 1:
    result = N * (N + 1) // 2
else:
    result = (1 + N) * (1 - N + 1) // 2
print(result)
