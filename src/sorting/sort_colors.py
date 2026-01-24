from typing import List

nums = [2, 0, 2, 1, 1, 0]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Given an array nums with n objects colored red, white, or blue, sort them in-place
        so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

        You must solve this problem without using the library's sort function.

        Parameters
        ----------
        nums: List
            An array nums with n objects colored red, white, or blue.

        Return
        ------
        None
            The sorting of the array must happen in-place.

        Examples
        --------

        Example 1:
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]

        Example 2:
        Input: nums = [2,0,1]
        Output: [0,1,2]
        """
        """
        Mutates nums so that it is sorted via selecting the minimum element and
        swapping it with the corresponding index
        """
        # NOTE: to improve it you can try to track the max value as well and add it at the end
        for i in range(len(nums)):
            # print("-----------")
            min_index = i
            # print(f"i is: {i} | min_index is: {min_index}")
            # print("-----------")

            for j in range(i + 1, len(nums)):
                # print("j is:", j)

                # Update minimum index
                if nums[j] < nums[min_index]:
                    min_index = j
                    # print(
                    #     f"Updated min_index is: {min_index} | Is j less than min_index? {nums[j] <= nums[min_index]} | Current nums[j]: {nums[j]} | Current nums[min_index]: {min_index}"
                    # )

            # Swap current index with minimum element in rest of list
            nums[min_index], nums[i] = nums[i], nums[min_index]
            # print(f"Current list: {nums}")


# Input: nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums=nums)
print(nums)
