def fact(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += fact(i) // i  # Using integer division

print("Sum of the series is:", total)
