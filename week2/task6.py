def all_eq(lst):
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)
    new_list = []
    for s in lst:
        diff = max_len - len(s)
        temp = s + "_" * diff
        new_list.append(temp)   
    return new_list
my_list = ["a333", "abc", "desdfsdf"]
print(all_eq(my_list))