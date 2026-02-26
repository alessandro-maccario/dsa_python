class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:

        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.

        Parameters
        ----------
        s : str
            A string

        Returns
        -------
        bool
            True if he string matches the conditions.

        Examples
        --------
        Example 1:
        Input: s = "()"
        Output: true

        Example 2:
        Input: s = "()[]{}"
        Output: true

        Example 3:
        Input: s = "(]"
        Output: false

        Example 4:
        Input: s = "([])"
        Output: true

        Example 5:
        Input: s = "([)]"
        Output: false
        """
        possible_closing_brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for char in s:
            if char not in possible_closing_brackets:  # if available as key
                stack.append(char)
            else:
                if stack:
                    # check if the opening bracket is on top of the stack. If not, return False, otherwise True
                    if stack[-1] == possible_closing_brackets[char]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


#################
### TEST CASE ###
#################

s = "([)]"
solution = Solution()
print(solution.isValid(s=s))
