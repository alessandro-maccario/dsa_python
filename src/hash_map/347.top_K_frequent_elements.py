from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

        Parameters
        ----------
        nums : List[int]
            A list of integers.
        k : int
            Number of k most frequent element.

        Returns
        -------
        List[int]
            Return the k most frequent elements.

        Examples
        --------
        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]

        Example 3:
        Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
        Output: [1,2]
        """
        return [x[0] for x in Counter(nums).most_common(k)]


#################
### Test case ###
#################

nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2

solution = Solution()
print(solution.topKFrequent(nums=nums, k=k))
