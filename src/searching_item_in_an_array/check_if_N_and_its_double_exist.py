"""
Check If N and Its Double Exist

Reference:
- https://algo.monster/liteproblems/1346
"""

from typing import List

# arr = [10, 2, 5, 3]
# arr = [3, 1, 7, 11]
# arr = [4, 2]
arr = [7, 1, 14, 11]


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Given an array arr of integers, check if there exist two indices i and j such that :

        i != j
        0 <= i, j < arr.length
        arr[i] == 2 * arr[j]

        Parameters
        ----------
            arr: List[int]
                Array arr of integers.

        Returns
        -------
            bool
                Return True if N and its double exist, otherwise False.

        Example 1
        ---------
        Input: arr = [10,2,5,3]
        Output: true
        Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

        Example 2
        ---------
        Input: arr = [3,1,7,11]
        Output: false
        Explanation: There is no i and j that satisfy the conditions.

        """

        if not arr:  # if arr is empty
            return False

        # create a set to store the already seen elements
        already_seen = set()

        for element in arr:
            # Does the element exist in the set?
            # We only check when x is even because odd numbers don't have integer halves
            if element % 2 == 0 and (element / 2) in already_seen:
                return True
            elif (element * 2) in already_seen:
                return True
            else:
                already_seen.add(element)

        return False


print(Solution().checkIfExist(arr=arr))
