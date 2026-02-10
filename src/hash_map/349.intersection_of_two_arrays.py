from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Given two integer arrays nums1 and nums2, return an array of their intersection.
        Each element in the result must be unique and you may return the result in any order.

        Parameters
        ----------
        nums1 : List[int]
            An integer array.
        nums2 : List[int]
            An integer array.

        Returns
        -------
        List[int]
            Intersection list of nums1 and nums2, without duplicates.

        Examples
        --------

        Example 1:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]

        Example 2:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
        Explanation: [4,9] is also accepted.
        """
        return list(set(nums1) & set(nums2))


#################
### TEST CASE ###
#################

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
solution = Solution()
print(solution.intersection(nums1=nums1, nums2=nums2))
