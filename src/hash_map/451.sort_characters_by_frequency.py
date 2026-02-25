from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Given a string s, sort it in decreasing order based on the frequency of the characters.
        The frequency of a character is the number of times it appears in the string.

        Return the sorted string. If there are multiple answers, return any of them.

        Parameters
        ----------
        s : str
            A string of characters.

        Returns
        -------
        str
            Return a sorted string of characters in decreasing order based on the frequency of the characters.
            The frequency of a character is the number of times it appears in the string.

        Examples
        --------

        Example 1:
        Input: s = "tree"
        Output: "eert"
        Explanation: 'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

        Example 2:
        Input: s = "cccaaa"
        Output: "aaaccc"
        Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
        Note that "cacaca" is incorrect, as the same characters must be together.

        Example 3:
        Input: s = "Aabb"
        Output: "bbAa"
        Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
        Note that 'A' and 'a' are treated as two different characters.
        """
        # create a frequency map of the characters
        result = ""

        # sort desc based on the values of each key
        char_frequency_map = dict(
            sorted(Counter(s).items(), key=lambda item: item[1], reverse=True)
        )

        # create the final string
        for char in char_frequency_map.keys():
            result += char * char_frequency_map[char]

        return result


#################
### Test case ###
#################

s = "tree"

solution = Solution()
print(solution.frequencySort(s=s))
