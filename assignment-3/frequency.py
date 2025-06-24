arr = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
max_elem = max(freq, key=freq.get)
max_freq = freq[max_elem]
print("Frequencies:", freq)
print("Highest Frequency Element:", max_elem)
print("Frequency:", max_freq)
