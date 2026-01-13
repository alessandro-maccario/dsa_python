"""
Remove Element from an Array in-place

Reference:
- https://algo.monster/liteproblems/27

Explanation
-----------
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

Example
-------

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

from typing import List

nums = [3, 2, 2, 3]
val = 3


class Solution:
    """
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
    The order of the elements may be changed. Then return the number of elements in nums which are NOT equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted,
    you need to do the following things:
    - Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
    The remaining elements of nums are not important as well as the size of nums.
    - Return k.
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

        Parameters
        ----------
            nums: List[int]:
                List of integers
            val: int:
                Value to be compared within the list of elements

        Returns
        -------
            int
                The counter of elements in the List[int] that do not match the value.

        Example
        -------

        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 2.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        """
        k = 0  # number of elements not equal to val: Write Pointer
        i = 0  # read pointer

        while i < len(nums):
            # print(
            #     "i:",
            #     i,
            #     "|",
            #     "nums[i]:",
            #     nums[i],
            #     "|",
            #     "len(nums):",
            #     len(nums),
            #     "|",
            #     "Counter:",
            #     k,
            #     "Equality:",
            #     nums[i] == val,
            #     "|",
            #     nums,
            # )
            if nums[i] != val:
                # move the next element to be in the position of the element == val in order to replace the val in the list
                # Count the elements that are not equal to val
                nums[k] = nums[i]
                i += 1
                k += 1
            else:
                # if the current value is different than the specified val, just increase i
                i += 1

        # return (f"Final list: {nums}", f"Counter: {k}")
        return k


print(Solution().removeElement(nums=nums, val=val))
