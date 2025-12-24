salaries = input().split()
salaries = list(map(int, salaries))
difference = max(salaries) - min(salaries)
print(difference)
