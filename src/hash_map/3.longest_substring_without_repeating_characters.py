"""
Reference
---------
- https://algo.monster/liteproblems/3
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without duplicate characters.

        Parameters
        ----------
        s : str
            A string s.

        Returns
        -------
        int
            Length of the longest substring without duplicate characters.

        Examples
        --------

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Idea
        ----
        The approach uses a two-pointers technique with a sliding window approach. Whenever a duplicate
        is found, the left side of the window gets shrinked to keep a substring (and not a subsequence)
        of the string always available. If duplicates are found, add a counter to the corresponding
        character in the dictionary, but then loop through them again to keep the counter equal to 1.
        """
        count_element = {}
        left_pointer = 0
        max_length = 0

        for right_pointer, char in enumerate(s):
            print(f"Char is: {char}")
            if char not in count_element:
                count_element[char] = 1
                print(count_element)
            else:
                count_element[char] += 1

            while count_element[char] > 1:
                count_element[s[left_pointer]] -= 1
                left_pointer += 1
            max_length = max(max_length, (right_pointer - left_pointer + 1))
            print(f"Counter element dictionary: {count_element}")
        return max_length


#################
### TEST CASE ###
#################

s = "pwwkew"
# s = "bbbbb"
# s = "abcabcbb"
s = "c"
solution = Solution()
print(solution.lengthOfLongestSubstring(s=s))
