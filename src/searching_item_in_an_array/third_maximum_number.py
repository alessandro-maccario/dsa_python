from typing import List

# nums = [3, 2, 1]
# nums = [2, 2, 3, 1]
nums = [5, 2, 4, 1, 3, 6, 0]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the third distinct maximum number in this array.
        If the third maximum does not exist, return the maximum number.

        Parameters:
            nums List[int]
                An array of integers.

        Returns:
            int
               The third distinct maximum number in this array.

        Example 1:
        Input: nums = [3,2,1]
        Output: 1
        Explanation:
        The first distinct maximum is 3.
        The second distinct maximum is 2.
        The third distinct maximum is 1.

        Example 2:
        Input: nums = [1,2]
        Output: 2
        Explanation:
        The first distinct maximum is 2.
        The second distinct maximum is 1.
        The third distinct maximum does not exist, so the maximum (2) is returned instead.

        Example 3:
        Input: nums = [2,2,3,1]
        Output: 1
        Explanation:
        The first distinct maximum is 3.
        The second distinct maximum is 2 (both 2's are counted together since they have the same value).
        The third distinct maximum is 1.
        """
        m1 = float("-inf")
        m2 = float("-inf")
        m3 = float("-inf")

        for num in list(set(nums)):
            if num > m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif num > m2:
                m3 = m2
                m2 = num
            elif num > m3:
                m3 = num

        if m3 > float("-inf"):
            return m3
        else:
            return m1


print(Solution().thirdMax(nums=nums))
