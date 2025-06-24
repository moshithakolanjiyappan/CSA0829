m = 25
n = 4
x = 3

max_per_child = m // n
remaining = m - (max_per_child * n)
peter_vehicles = min(remaining, x)

print(peter_vehicles)
print("Peter is luckier!" if peter_vehicles % 2 == 0 else "Peter is not luckier.")
