import time
from typing import List

# nums = [0, 1, 0, 3, 12]
# nums = [0]
# nums = [1, 0, 1]
nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Parameters
        ----------
        nums: List[int]
            An integer array nums

        Results
        -------
        None


        Examples
        --------

        Example 1
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Example 2:
        Input: nums = [0]
        Output: [0]
        """
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

        return nums


start_time = time.time()
print(Solution().moveZeroes(nums=nums))
print("---> %s seconds ---" % (time.time() - start_time))
