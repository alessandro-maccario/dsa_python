stack_nge = []
map_nums2 = {}

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

for element in nums2:
    while stack_nge and element <= stack_nge[-1]:
        map_nums2[element] = stack_nge[-1]
        stack_nge.pop(-1)
        break
    stack_nge.append(element)

output = [map_nums2.get(element, -1) for element in nums1]
print(output)
