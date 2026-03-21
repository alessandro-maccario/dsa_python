stack_pge = []
map_nums = {}

nums = [5, 3, 4]

for element in nums:
    while stack_pge and stack_pge[-1] < element:
        stack_pge.pop(-1)

    if stack_pge:
        map_nums[element] = stack_pge[-1]

    stack_pge.append(element)

output = [map_nums.get(element, -1) for element in nums]
print(output)
