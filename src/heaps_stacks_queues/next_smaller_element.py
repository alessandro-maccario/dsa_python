stack = []
nums = [1, 3, 4, 2]
result = [-1] * len(nums)

for i in range(len(nums)):
    while stack and nums[stack[-1]] > nums[i]:
        current = stack.pop(-1)
        result[current] = nums[i]

    stack.append(i)

print(result)
