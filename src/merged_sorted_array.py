from typing import List

# Inputs
nums1 = [0, 0, 3, 0, 0, 0, 0, 0, 0]
m = 3
nums2 = [-1, 1, 1, 1, 2, 3]
n = 6
# Expected output: [-1,0,0,1,1,1,2,3,3]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Merge Sorted Array

        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
        and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
        """
        # Pointers
        i = m - 1
        j = n - 1
        k = len(nums1) - 1

        # Two-Pointers approach starting from the end of the list
        while (
            i >= 0 and j >= 0
        ):  # Check for i and j being >= 0 and for truthness of nums1 and nums2 (they do not have to be empty)
            # decrease the index of the higher value in the comparison so that you are moving to the next value comparison
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1  # decrease pointer in nums2
                k -= 1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1  # decrease pointer in nums1
                k -= 1
            else:
                # in case the two values are the same, keep decreasing only i and treat j separately outside this first while loop
                nums1[k] = nums1[i]
                i -= 1
                k -= 1

        # if i < 0 but j >= 0, then the rest of the values from nums2 must be copied into nums1 as they are, because it means that they are already ordered and simply missing from nums1 output
        if j >= 0:
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        return nums1


print(Solution().merge(nums1=nums1, nums2=nums2, m=m, n=n))
