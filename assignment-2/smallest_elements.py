lst = [7, 2, 5, 3, 9, 1]
k = 3
sorted_lst = sorted(lst)
if 1 <= k <= len(lst):
    kth_smallest = sorted_lst[k-1]
    print(kth_smallest)
else:
    print("k is out of range")
