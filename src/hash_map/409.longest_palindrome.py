from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        A Palindrome is a string of characters that reads the same left-to-right and right-to-left.
        Given a string s which consists of lowercase or uppercase letters,
        return the length of the longest palindrome that can be built with those letters.

        Letters are case sensitive, for example, "Aa" is not considered a palindrome.

        Parameters
        ----------
        s : str
            A string of characters.

        Returns
        -------
        int
            Return the length of the longest palindrome that can be built with those characters.

        Examples
        --------
        Example 1:
        Input: s = "abccccdd"
        Output: 7
        Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

        Example 2:
        Input: s = "a"
        Output: 1
        Explanation: The longest palindrome that can be built is "a", whose length is 1.

        Explanation
        -----------
        - A palindrome needs pairs of characters (one on each side)
        - Each character with frequency v can contribute at most "v // 2 * 2" characters to the palindrome
            - e.g., if you have 7 'a's → you can use 6 of them as 3 pairs (aaa...aaa)
            - the leftover 1 'a' can't form a pair, so it gets added in the middle!

        Why this gives the largest even number ≤ v?

        If v is even (e.g., v = 6):
            - 6 // 2 = 3
            - 3 *  2 = 6  ✓ (unchanged, since it was already even)

        If v is odd (e.g., v = 7):
            - 7 // 2 = 3   ← integer division discards the remainder (0.5 → 0)
            - 3 *  2 = 6  ✓ (rounds down to nearest even)
        """
        string_counter = Counter(s)
        max_amount_of_pairs_possible = sum(v // 2 * 2 for v in string_counter.values())
        if max_amount_of_pairs_possible < len(s):
            max_amount_of_pairs_possible += 1

        return max_amount_of_pairs_possible


#################
### TEST CASE ###
#################

s = "cc"
solution = Solution()
print(solution.longestPalindrome(s=s))
