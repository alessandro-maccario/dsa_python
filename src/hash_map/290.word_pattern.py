class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Given a pattern and a string s, find if s follows the same pattern.

        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

        Each letter in pattern maps to exactly one unique word in s.
        Each unique word in s maps to exactly one letter in pattern.
        No two letters map to the same word, and no two words map to the same letter.

        Parameters
        ----------
        pattern : str
            _description_
        s : str
            _description_

        Returns
        -------
        bool
            _description_

        Examples
        --------
        Example 1:
        Input: pattern = "abba", s = "dog cat cat dog"
        Output: true

        Explanation:
        The bijection can be established as:

        'a' maps to "dog".
        'b' maps to "cat".

        Example 2:
        Input: pattern = "abba", s = "dog cat cat fish"
        Output: false

        Example 3:
        Input: pattern = "aaaa", s = "dog cat cat dog"
        Output: false
        """
        if len(pattern) != len(s.split(" ")):
            return False

        # This will return true if and only if each unique letter maps to each unique word.
        # Otherwise, the result will be a non matching tuple of letter and word with a letter repeating for a different word.
        return (
            len(set(zip(pattern, s.split(" "))))
            == len(set(s.split(" ")))
            == len(set(pattern))
        )


#################
### Test case ###
#################

pattern = "abba"
s = "dog cat cat dog"

solution = Solution()
print(solution.wordPattern(pattern=pattern, s=s))
