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

        if len(arr) < 3:
            print("Too short")
            return False
        else:
            # add conditions
            len_array = len(
                arr
            )  # needed to find where the center of the arr can be found
            middle_index = len_array // 2
            print("Middle index:", middle_index)

            if len(arr) % 2 == 0:
                while i < len(arr[: middle_index - 1]):
                    print(
                        f"i is: {i} | middle index: {middle_index} | first part of the array {arr[:middle_index]} | arr+1 = {arr[i + 1]}"
                    )
                    if arr[i] >= arr[i + 1]:
                        # the first part of the array is in decreasing order
                        print("First halves, False")
                        return False
                    else:
                        print("First part of the array increasing order ↗️")
                    i += 1
                    print(f"Current i: {i}")
                print(f"Current arr at position i = {i} -> {arr[i]}")
                while i < len(arr[middle_index:]):
                    if arr[i] <= arr[i + 1]:
                        print("Second halves, False")
                        return False
                    else:
                        print("Second part of the array in decreasing order ↘️")
                        return True
            else:
                while i < len(arr[:middle_index]):
                    print(
                        f"i is: {i} | middle index: {middle_index} | first part of the array {arr[:middle_index]} | arr+1 = {arr[i + 1]}"
                    )
                    if arr[i] >= arr[i + 1]:
                        # the first part of the array is in decreasing order
                        print("First halves, False")
                        return False
                    else:
                        print("First part of the array increasing order ↗️")
                    i += 1
                    print(f"Current i: {i}")
                print(f"Current arr at position i = {i} -> {arr[i]}")
                while i < len(arr[middle_index:]):
                    if arr[i] <= arr[i + 1]:
                        print("Second halves, False")
                        return False
                    else:
                        print("Second part of the array in decreasing order ↘️")
                        return True

        return False


print(Solution().validMountainArray(arr=arr))
