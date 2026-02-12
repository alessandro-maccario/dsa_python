from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Given two integer arrays nums1 and nums2, return an array of their intersection.
        Each element in the result must appear as many times as it shows in both arrays
        and you may return the result in any order.

        Parameters
        ----------
        nums1 : List[int]
            An array of integers.
        nums2 : List[int]
            An array of integers.

        Returns
        -------
        List[int]
            Return an intersection list between nums1 and nums2.

        Examples
        --------
        Example 1:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]

        Example 2:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]
        Explanation: [9,4] is also accepted.
        """
        # Find intersection
        return list((Counter(nums1) & Counter(nums2)).elements())


#################
### TEST CASE ###
#################

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
solution = Solution()
print(solution.intersection(nums1=nums1, nums2=nums2))
