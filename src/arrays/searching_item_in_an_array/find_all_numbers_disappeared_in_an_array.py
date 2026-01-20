from typing import List

nums = [4, 3, 2, 7, 8, 2, 3, 1]
# nums = [1, 1]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n],
        return an array of all the integers in the range [1, n] that do not appear in nums.

        Parameters
        ----------
            nums: List[int]
                Array nums of n integers where nums[i] is in the range [1, n].

        Returns
        -------
            List[int]
                Array of all the integers in the range [1, n] that do not appear in nums.

        Example 1:
        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [5,6]

        Example 2:
        Input: nums = [1,1]
        Output: [2]
        """
        # 1. Take len(nums) and create using range a list of values containing all of the values in that range.
        # 2. Take the set(difference) between the two lists.
        # 3. Return the output
        return list(set(range(1, len(nums) + 1)) - set(nums))


print(Solution().findDisappearedNumbers(nums=nums))
