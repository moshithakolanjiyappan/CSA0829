import statistics
numbers = list(map(float, input("Enter numbers separated by space: ").split()))
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
