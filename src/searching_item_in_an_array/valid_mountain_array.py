"""
Valid Mountain Array

Reference:
-
"""

from typing import List

# arr = [0, 3, 2, 1]
# arr = [2, 1]
# arr = [3, 5, 5]
# arr = [4, 4, 3, 2, 1]
arr = [1, 2, 3, 4, 9, 8, 7, 6, 5]


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Given an array of integers arr, return true if and only if it is a valid mountain array.

        Recall that arr is a mountain array if and only if:

        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

        Parameters
        ----------
            arr List[int]
                An array of integers arr.

        Returns
        -------
            bool
                Return true if and only if it is a valid mountain array.

        Example 1
        ---------
        Input: arr = [2,1] -> len(arr) < 3
        Output: false

        Example 2
        ---------
        Input: arr = [3,5,5] -> increasing, but not strictly
        Output: false

        Example 3
        ---------
        Input: arr = [0,3,2,1]
        Output: true

        """
        i = 0
        # if one of the two flag is False, then False
        flag_up = False
        flag_down = False

        # Exit the function if the basic conditions are not met
        if len(arr) < 3:
            return False
        if arr[i] >= arr[i + 1]:
            # if the first element is already bigger than the second element, there is no upward trend
            return False

        # in this case check the upwards/downwards trend
        while i < len(arr) - 1:
            print(f"Current i {i}")
            if arr[i] < arr[i + 1]:
                i += 1
                flag_up = True
            elif arr[i] == arr[i + 1]:
                return False
            else:
                i += 1
                flag_down = True

        return flag_up == flag_down


print(Solution().validMountainArray(arr=arr))
