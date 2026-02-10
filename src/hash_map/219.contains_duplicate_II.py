from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k, return true if there are two distinct indices i and j
        in the array such that nums[i] == nums[j] and abs(i - j) <= k.

        Parameters
        ----------
        nums : List[int]
            An integer array.
        k : int
            k represents the distance between the two indeces.

        Returns
        -------
        bool
            Return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

        Examples
        --------

        Example 1:
        Input: nums = [1,2,3,1], k = 3
        Output: true

        Example 2:
        Input: nums = [1,0,1,1], k = 1
        Output: true

        Example 3:
        Input: nums = [1,2,3,1,2,3], k = 2
        Output: false
        """
        storage = dict()
        for idx, num in enumerate(nums):
            if num not in storage:
                # save the index where you have seen the element
                storage[num] = idx
            else:
                # check if the distance between indexes and k is already <= k
                distance_from_last_occurrence = abs(idx - storage[num])
                if distance_from_last_occurrence <= k:
                    return True
                else:
                    # if already available, update the value and continue with the rest of the list
                    storage[num] = idx
                    print("Storage:", storage, "|", f"i: {idx} | j: {storage[num]}")
                    continue

        return False


#################
### TEST CASE ###
#################

nums = [1, 0, 1, 1]
solution = Solution()
print(solution.containsNearbyDuplicate(nums=nums, k=1))
