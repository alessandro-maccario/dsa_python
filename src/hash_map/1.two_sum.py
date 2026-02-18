from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers
        such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Parameters
        ----------
        nums : List[int]
            An array of integers.
        target : int
            An integer.

        Returns
        -------
        List[int]
            Return indices of the two numbers such that they add up to target.

        Examples
        --------

        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]

        """
        dictionary = {}  # already seen elements
        result = []  # list of indexes

        for idx, num in enumerate(nums):
            y = target - num
            if y not in dictionary:
                dictionary[num] = idx
                print(dictionary)
            else:
                # If found, append the current index to the result list and the current value index available in the dictionary of already seen elements
                result.append(idx)
                result.append(dictionary[y])
                return result

        return result


#################
### Test case ###
#################

nums = [1, 2, 3, 4]
target = 5

solution = Solution()
print(solution.twoSum(nums=nums, target=target))
