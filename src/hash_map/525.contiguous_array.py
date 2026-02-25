from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """_summary_

        Parameters
        ----------
        nums : List[int]
            _description_

        Returns
        -------
        int
            _description_

        Examples
        --------
        """

        dict_idx_sum_prefix = {0: -1}
        maximum_length_so_far = 0
        current_sum = 0

        # trick: convert every 0s to -1 and then search the maximum substring that sum up to 0.
        nums_conversion = [-1 if num == 0 else num for num in nums]

        for idx, num in enumerate(nums_conversion):
            # update the current sum with the num at each step
            current_sum += num
            print(f"Current Sum: {current_sum}")
            if current_sum not in dict_idx_sum_prefix:
                dict_idx_sum_prefix[current_sum] = idx
            else:
                # compute the length between the first seen and the next one
                temp_max_length = idx - dict_idx_sum_prefix[current_sum]
                if temp_max_length > maximum_length_so_far:
                    maximum_length_so_far = temp_max_length
                print(f"Value: {num}")

        return maximum_length_so_far


#################
### Test case ###
#################

nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]

solution = Solution()
print(solution.findMaxLength(nums=nums))
