lst = [4, 1, 7, 3, 9]

unique_lst = list(set(lst))  # Remove duplicates
unique_lst.sort()

if len(unique_lst) >= 2:
    second_largest = unique_lst[-2]
    print(second_largest)
else:
    print("List doesn't have enough unique elements.")
