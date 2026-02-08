from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.

        Parameters
        ----------
        nums : List[int]
            A non-empty array of integers where every element appears twice except for one.

        Returns
        -------
        int
            The element that appears once.

        Examples
        --------
        Example 1:
        Input: nums = [2,2,1]
        Output: 1

        Example 2:
        Input: nums = [4,1,2,1,2]
        Output: 4

        Example 3:
        Input: nums = [1]
        Output: 1
        """
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        return sorted(counts.items(), key=lambda item: item[1])[0][0]


#################
### TEST CASE ###
#################

nums = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber(nums=nums))
