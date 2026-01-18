import time
from typing import List

# nums = [3, 1, 2, 4]
# nums = [4, 2, 4, 3, 5, 1]
nums = [0, 1, 2]


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
        Return any array that satisfies this condition.

        Parameters
        ----------
            nums List[int]
                Integer array.

        Returns
        -------
            List[int]
                Returns an array where all the initial even integers are moved to the start of the array, while the odd ones are moved to the end.

        Examples
        --------

        Example 1:
        Input: nums = [3,1,2,4]
        Output: [2,4,3,1]
        Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

        Example 2:
        Input: nums = [0]
        Output: [0]
        """
        i = 0
        j = 0

        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums


start_time = time.time()
print(Solution().sortArrayByParity(nums=nums))
print("---> %s seconds ---" % (time.time() - start_time))
