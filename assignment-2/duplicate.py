lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = []
for x in lst:
    if x not in unique_lst:
        unique_lst.append(x)
print(unique_lst)
