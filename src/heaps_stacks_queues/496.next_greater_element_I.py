"""
NGE: Next Greater Element Problem Set
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        The next greater element of some element x in an array is the first greater element
        that is to the right of x in the same array.
        You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

        For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and
        determine the next greater element of nums2[j] in nums2. If there is no next greater element,
        then the answer for this query is -1.

        Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

        Parameters
        ----------
        nums1 : List[int]
            A 0-indexed integer array where nums1 is a subset of nums2.
        nums2 : List[int]
            A 0-indexed integer array.

        Returns
        -------
        List[int]
            Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

        Examples
        --------
        Example 1:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        Output: [-1,3,-1]
        Explanation: The next greater element for each value of nums1 is as follows:
        - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
        - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
        - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

        Example 2:
        Input: nums1 = [2,4], nums2 = [1,2,3,4]
        Output: [3,-1]
        Explanation: The next greater element for each value of nums1 is as follows:
        - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
        - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
        """
        stack_nge = []
        map_nums = {}
        result_nge = []

        # Firt Loop: create a map of nums2 and the next greater element of its elements.
        # Because nums1 is a subset of nums2, the second loop will be needed to only
        # make a lookup in maps2 of its value.
        for element in nums2:
            while stack_nge and element > stack_nge[-1]:
                map_nums[stack_nge[-1]] = element
                stack_nge.pop(-1)

            stack_nge.append(element)

        for remaining_stack_element in stack_nge:
            map_nums[remaining_stack_element] = -1

        for element in nums1:
            result_nge.append(map_nums[element])

        return result_nge


#################
### TEST CASE ###
#################

nums1 = [1, 3, 5, 2, 4]
nums2 = [5, 4, 3, 2, 1]

solution = Solution()
print(solution.nextGreaterElement(nums1=nums1, nums2=nums2))
