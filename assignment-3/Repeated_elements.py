arr = [1, 2, 3, 2, 4, 5, 1, 6]
repeated = []

for num in arr:
    if arr.count(num) > 1 and num not in repeated:
        repeated.append(num)

print("Repeated elements:", repeated)
