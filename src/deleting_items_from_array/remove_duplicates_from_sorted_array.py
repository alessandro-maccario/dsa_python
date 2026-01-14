"""
Remove Duplicates from Sorted Array

Reference
- https://algo.monster/liteproblems/26
"""

from typing import List


# nums = [1, 1, 2]
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1, 1, 2, 3, 3]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
        such that each unique element appears only once. The relative order of the elements should be kept the same.

        Consider the number of unique elements in nums to be k.
        After removing duplicates, return the number of unique elements k.

        The first k elements of nums should contain the unique numbers in sorted order.
        The remaining elements beyond index k - 1 can be ignored.

        Parameters
        ----------
            nums: List[int]
                An integer array nums sorted in non-decreasing order that contains duplicate values.

        Returns
        -------
            int
                The number of unique elements k.

        Example
        -------
        Input: nums = [1,1,2,3,3]
        Output: 3, nums = [1,2,3,_,_]
        Explanation: Your function should return k = 3, with the first three elements of nums being 1, 2 and 3 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        """
        i = 1  # read pointer
        k = 1  # write pointer. The first element is always unique, therefore we add it already

        while i < len(nums):
            # Because the array is already sorted, the duplicated values are next to each other
            if nums[k - 1] == nums[i]:
                i += 1
            else:
                nums[k] = nums[i]
                i += 1
                k += 1  # count the unique elements in the array, in addition to the first element which is by definition unique

        return k


print(Solution().removeDuplicates(nums=nums))
