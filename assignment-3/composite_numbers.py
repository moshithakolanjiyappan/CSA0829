def is_composite(num):
    if num <= 3:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

arr = [1, 4, 6, 7, 9, 10, 13]
count = sum(is_composite(x) for x in arr)
print(count)
