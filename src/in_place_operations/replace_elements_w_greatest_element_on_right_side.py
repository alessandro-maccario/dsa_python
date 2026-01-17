from typing import List

arr1 = [400]
arr2 = [17, 18, 5, 4, 6, 1]

arr_concat = []
arr_concat.append(arr1)
arr_concat.append(arr2)
print(f"Original arr: {arr2}")


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
        After doing so, return the array.

        Parameters
        ----------
            arr: List[int]
                Array of integers.

        Returns
        -------
            List[int]:
                Return a list of integers where every element is replaced by the greatest element among the elements to its right.

        Example 1
        ---------
        Input: arr = [17,18,5,4,6,1]
        Output: [18,6,6,6,1,-1]
        Explanation:
        - index 0 --> the greatest element to the right of index 0 is index 1 (18).
        - index 1 --> the greatest element to the right of index 1 is index 4 (6).
        - index 2 --> the greatest element to the right of index 2 is index 4 (6).
        - index 3 --> the greatest element to the right of index 3 is index 4 (6).
        - index 4 --> the greatest element to the right of index 4 is index 5 (1).
        - index 5 --> there are no elements to the right of index 5, so we put -1.

        Example 2
        ---------
        Input: arr = [400]
        Output: [-1]
        Explanation: There are no elements to the right of index 0.

        Possible solution
        -----------------
        Right-to-left index approach.

        """
        j = len(arr) - 1

        # Main conditions
        # in the very first loop the max value is equal to the last element
        max_value = arr[-1]
        for j in range(len(arr), -1, -1):  # start, stop, step
            # this is the temporary variable to keep the current max value before replacing the current one
            temp = arr[j - 1]
            # replace the current index value with the max-so-far
            arr[j - 1] = max_value
            # Need to check again the max_value against the temp
            if temp > max_value:
                max_value = temp

        # Last element will always be -1 because there is no comparison to be done on its right side
        arr[-1] = -1

        return arr


print("Output:", Solution().replaceElements(arr=arr2))
print("Expected output:[18, 6, 6, 6, 1, -1]")
