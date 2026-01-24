from typing import List

# nums = [2, 0, 2, 1, 1, 0]
# nums = [1, 2, 3, 4, 5, 6]
nums = [1, 2, 4, 3, 5, 6]


class Solution:
    def bubble_sort(self, nums: List[int]) -> None:
        """
        Implementation of Bubble Sort

        Parameters
        ----------
            nums: List[int]
                An array of unsorted integers.

        Returns
        -------
            List
                The input array sorted in-place using bubble sort.

        Examples
        --------

        Example 1
        nums = [1, 2, 4, 3, 5, 6]
        output = [1, 2, 3, 4, 5, 6]

        Example 2
        nums = [2, 0, 2, 1, 1, 0]
        output = [0, 0, 1, 1, 2, 2]

        References
        ----------
        - https://www.youtube.com/watch?v=xli_FI7CuzA
        """
        # The biggest elements are already sorted after the each pass, therefore no need to have a look at those anymore
        current_scanning_idx = len(nums)

        for i in range(1, current_scanning_idx):
            # The swap flag checks if any comparison has already the condition num[j] < nums[j+1].
            # If this is true, then the array is already sorted and there is no need to sort it even more
            swap_flag = False
            # for j in range(0, len(nums) - 1):
            for j in range(0, current_scanning_idx - 1):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    swap_flag = True
            current_scanning_idx -= 1
            # If the flag is False, there as been no valid swaps, therefore the array is already sorted
            if not swap_flag:
                break

        return


Solution().bubble_sort(nums=nums)
print(nums)
