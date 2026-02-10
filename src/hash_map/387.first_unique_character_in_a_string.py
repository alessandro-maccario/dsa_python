from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Given a string s, find the first non-repeating character in it and return its index.
        If it does not exist, return -1.

        Parameters
        ----------
        s : str
            A string.

        Returns
        -------
        int
            Index of the first non-repeating character in the string.

        Examples
        --------

        Example 1:
        Input: s = "leetcode"
        Output: 0

        Explanation:
        The character 'l' at index 0 is the first character that does not occur at any other index.

        Example 2:
        Input: s = "loveleetcode"
        Output: 2

        Example 3:
        Input: s = "aabb"
        Output: -1
        """

        storage = dict()
        for letter in s:
            if letter not in storage:
                storage[letter] = 1
            else:
                storage[letter] += 1

        # Return first value where value > 5
        first_value = next((k for k, v in storage.items() if v == 1), None)
        if first_value:
            # extrac the index of the value that appears once in the string from the dict mapping
            return s.index(first_value)
        else:
            # if no value is available
            return -1


#################
### TEST CASE ###
#################

s = "aabb"
solution = Solution()
print(solution.firstUniqChar(s=s))
