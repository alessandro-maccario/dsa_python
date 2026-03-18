"""
NGE: Next Greater Element Problem Set
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Given a circular integer array nums (i.e., the next element of nums[nums.length - 1]
        is nums[0]), return the next greater number for every element in nums.

        The next greater number of a number x is the first greater number to its
        traversing-order next in the array, which means you could search circularly
        to find its next greater number. If it doesn't exist, return -1 for this number.

        Parameters
        ----------
        nums : List[int]
            A circular integer array nums.

        Returns
        -------
        List[int]
            Return the next greater number for every element in nums.

        Examples
        --------
        Example 1:
        Input: nums = [1,2,1]
        Output: [2,-1,2]
        Explanation: The first 1's next greater number is 2;
        The number 2 can't find next greater number.
        The second 1's next greater number needs to search circularly, which is also 2.

        Example 2:
        Input: nums = [1,2,3,4,3]
        Output: [2,3,4,-1,4]
        """
        result = len(nums) * [-1]
        n = len(nums)
        stack = []  # you store indexes in here

        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop(-1)] = nums[idx]

            if i < n:
                stack.append(idx)

        return result


#################
### TEST CASE ###
#################

nums = [5, 4, 3, 2, 1]
# nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 100]
nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]

solution = Solution()
print(solution.nextGreaterElements(nums=nums))
