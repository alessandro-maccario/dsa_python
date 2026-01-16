"""
Valid Mountain Array

Reference:
- https://algo.monster/liteproblems/941
"""

from typing import List

arr1 = [0, 3, 2, 1]
arr2 = [2, 1]
arr3 = [3, 5, 5]
arr4 = [4, 4, 3, 2, 1]
arr5 = [1, 2, 3, 4, 9, 8, 7, 6, 5]
arr6 = [0, 2, 3, 4, 5, 2, 1, 0]
arr7 = [0, 2, 3, 3, 5, 2, 1, 0]
arr8 = [0, 1, 2, 3, 4, 5]

result = []
result.append(arr1)
result.append(arr2)
result.append(arr3)
result.append(arr4)
result.append(arr5)
result.append(arr6)
result.append(arr7)
result.append(arr8)
print(result)


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Given an array of integers arr, return true if and only if it is a valid mountain array.

        Recall that arr is a mountain array if and only if:

        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

        The mountain array problem can be though of as a two pointers problem both sections of the array
        must be monotonic (increasing, then decreasing).

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
        left = 0
        right = len(arr) - 1

        # Exit the function if the basic conditions are not met
        if len(arr) < 3:
            return False
        if arr[left] >= arr[left + 1]:
            # if the first element is already bigger than the second element, there is no upward trend
            return False
        if arr[right] >= arr[right - 1]:
            # if the last element is already bigger than the previous to last element, there is no downward trend in the second slice
            return False

        # Look for the left part of the array
        while arr[left] < arr[left + 1] and left < len(arr) - 1:
            left += 1
        # look for the right part of the array
        while arr[right] < arr[right - 1] and right > 0:
            right -= 1

        # if both indexes are the same, that means that the left and right indexes have found themselves at the peak of the array.
        # Both indexes must have also moved from their initial position
        return left == right and left != 0 and right != len(arr) - 1


for arr in result:
    print(arr, " -> ", Solution().validMountainArray(arr=arr))
