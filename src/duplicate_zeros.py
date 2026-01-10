"""
Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        Parameters
        ----------
        arr: list
            The input array

        Returns
        -------
        None

        Examples
        --------
        arr = [1,0,2,3,0,4,5,0]
        expected output => arr = [1,0,0,2,3,0,0,4]

        Reference
        ---------
        - https://algo.monster/liteproblems/1089

        Explanation:
        The idea is to define two phases:
        1. Phase 1: in phase 1 you scan the array to define what your two pointers (i: Read; j: Write) are.
        The i is the last possible elements in arr[i] that will be considered as valid value before exceeding the length of the array.
        The j will be the last writable position, before exceeding the length of the array.

        2. Phase 2: in phase 2, while i and j >=0, you can loop simulate the shifting values and decreasing i and j accordingly,
        based on 0s found in the array and their duplication.
        Looping over the original array would be conceptually wrong: only a while loop over the array's indexes is needed
        as you can replace the j-th value with the i-th array's value to properly shift the elements.

        The filling of the array goes backward: you start from the end of the array and you are going back to the
        beginning of the array.
        """
        # Instantiate a virtual length arr
        virtual_length_arr = 0

        for idx, value in enumerate(arr):
            if value == 0:
                virtual_length_arr += 2
            else:
                virtual_length_arr += 1
            # If reach end of array, break out
            if virtual_length_arr >= len(arr):
                i = idx
                j = virtual_length_arr - 1
                break

        # 2. Phase 2: iterate over the indexes of the original arr and replace the array values depending if arr[i] == 0 or not; update the indexes accordingly
        while i >= 0 and j >= 0:
            if arr[i] != 0:
                arr[j] = arr[i]
                i -= 1
                j -= 1
            else:
                i -= 1
                arr[j] = 0
                arr[j - 1] = 0
                j -= 2

        return
