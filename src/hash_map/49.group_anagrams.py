"""
Reference
- https://www.youtube.com/watch?v=qqUYkoFRW8Y
- https://www.youtube.com/watch?v=RcZsTI5h0kg

"""

from typing import List


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        Parameters
        ----------
        strs : List[str]
            An array of anagram strings.

        Returns
        -------
        List[List[str]]
            A list of grouped anagrams.

        Examples
        --------
        Example 1:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Explanation:

        There is no string in strs that can be rearranged to form "bat".
        The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

        Example 2:
        Input: strs = [""]
        Output: [[""]]

        Example 3:
        Input: strs = ["a"]
        Output: [["a"]]
        """
        # Create a dictionary of the keys available in the strs list
        storing_dict = {}

        # For each key available, if the sorted key string is not in the dict add it and add the elements to the list that, sorted, gives back the same string value as the key
        for key in strs:
            new_key = "".join(sorted(key))
            if new_key not in storing_dict:
                storing_dict[new_key] = []
                storing_dict[new_key].append(key)
            else:
                storing_dict[new_key].append(key)

        return list(storing_dict.values())


solution = Solution()
print(solution.groupAnagrams(strs=strs))
