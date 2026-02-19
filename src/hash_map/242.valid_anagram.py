from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        Parameters
        ----------
        s : str
            A string.
        t : str
            A string.

        Returns
        -------
        bool
            Return true if t is an anagram of s, and false otherwise.

        Examples
        --------
        Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true

        Example 2:
        Input: s = "rat", t = "car"
        Output: false
        """
        return Counter(s) == Counter(t)


#################
### Test case ###
#################

s = "anagram"
t = "nagaram"

solution = Solution()
print(solution.isAnagram(s=s, t=t))
