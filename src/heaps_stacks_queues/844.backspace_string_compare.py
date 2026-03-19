class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if they are equal when both are
        typed into empty text editors. '#' means a backspace character.

        Note that after backspacing an empty text, the text will continue empty.

        Parameters
        ----------
        s : str
            A string of characters.
        t : str
            A string of characters.

        Returns
        -------
        bool
            Return True if both s and t yield the same results, else False.

        Examples
        --------
        Example 1:
        Input: s = "ab#c", t = "ad#c"
        Output: true
        Explanation: Both s and t become "ac".

        Example 2:
        Input: s = "ab##", t = "c#d#"
        Output: true
        Explanation: Both s and t become "".

        Example 3:
        Input: s = "a#c", t = "b"
        Output: false
        Explanation: s becomes "c" while t becomes "b".
        """

        stack_s = []
        stack_t = []

        # Process the "s" string
        for element in s:
            if element != "#":
                stack_s.append(element)
            else:
                if stack_s and element == "#":
                    stack_s.pop(-1)

        # Process the "t" string
        for element in t:
            if element != "#":
                stack_t.append(element)
            else:
                if stack_t and element == "#":
                    stack_t.pop(-1)

        return "".join(stack_s) == "".join(stack_t)


#################
### TEST CASE ###
#################

s = "ab#c"
t = "ad#c"

solution = Solution()
print(solution.backspaceCompare(s=s, t=t))
