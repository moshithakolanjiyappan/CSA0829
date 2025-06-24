nums = [1, -2, 3, 5, -1, 2]
max_sum = curr_sum = nums[0]

for num in nums[1:]:
    curr_sum = max(num, curr_sum + num)
    max_sum = max(max_sum, curr_sum)

print(max_sum)
