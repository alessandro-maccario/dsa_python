class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Given a string s of '(' , ')' and lowercase English characters.

        Your task is to remove the minimum number of parentheses ( '(' or ')',
        in any positions ) so that the resulting parentheses string is valid
        and return any valid string.

        Formally, a parentheses string is valid if and only if:

        It is the empty string, contains only lowercase characters, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.

        Parameters
        ----------
        s : str
            A string of '(', ')' and lowercase English characters.

        Returns
        -------
        str
            Return a valid string that removes the minimum number of parentheses in any position.

        Examples
        --------
        Example 1:
        Input: s = "lee(t(c)o)de)"
        Output: "lee(t(c)o)de"
        Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

        Example 2:
        Input: s = "a)b(c)d"
        Output: "ab(c)d"

        Example 3:
        Input: s = "))(("
        Output: ""
        Explanation: An empty string is also valid.
        """

        # Constants
        # the algorithm uses a counter to keep track of the opening and closing brackets in excess
        bracket_counter = 0
        stack = []

        # Two step approach: first round to remove all unclosed parenthesis ')' going from left-to-right
        for element in s:
            if element != ")":
                if element == "(":
                    bracket_counter += 1
                stack.append(element)
            else:
                # it can happen that an ')' unclosed parenthesis is found immediately at the beginning
                # and it has to be removed. Need to check if the opening counter is still 0
                if element == ")" and bracket_counter == 0:
                    pass
                else:
                    bracket_counter -= 1
                    stack.append(element)

        # use additional stack to create the final result and the counter
        stack_final = []
        bracket_counter = 0

        # Second run: to remove all open and unclosed parenthesis '(' going from right-to-left
        for element in reversed(stack):
            if element != "(":
                if element == ")":
                    bracket_counter += 1
                stack_final.append(element)
            else:
                if element == "(" and bracket_counter == 0:
                    pass
                else:
                    bracket_counter -= 1
                    stack_final.append(element)

        return "".join(reversed(stack_final))


#################
### TEST CASE ###
#################

s = "a)b(c)d"  # "a)b(c)d" -> expected: "ab(c)d" | "lee(t(c)o)de)" -> expected: "lee(t(c)o)de"

solution = Solution()
print(solution.minRemoveToMakeValid(s=s))
