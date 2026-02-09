from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.

        Parameters
        ----------
        nums : List[int]
            An integer array nums.

        Returns
        -------
        bool
            Return true if any value appears at least twice in the array.

        Examples
        --------

        Example 1:
        Input: nums = [1,2,3,1]
        Output: true

        Explanation:
        The element 1 occurs at the indices 0 and 3.

        Example 2:
        Input: nums = [1,2,3,4]
        Output: false

        Explanation:
        All elements are distinct.

        Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
        """
        # A set for this task is better because you just need to store an element that you have never seen before
        # and in case you have it already seen, then simply return true
        storage = set()
        for num in nums:
            if num not in storage:
                storage.add(num)
            else:
                return True
        return False


#################
### TEST CASE ###
#################

nums = [1, 2, 3, 4]
solution = Solution()
print(solution.containsDuplicate(nums=nums))
