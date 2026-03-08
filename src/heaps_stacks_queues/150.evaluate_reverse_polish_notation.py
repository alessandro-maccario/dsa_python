"""
The method from_infix_to_postfix_notation is not related to the reverse polish notation
but it's the first step to understand how to solve that problem.
"""

from typing import List


class SolutionInfixPostfix:
    def from_infix_to_postfix_notation(self, s: str) -> str:
        # order of operators (brackets, order, division, multiplication, addition, subtraction)
        # The lowest priority in this case is represented by the bracket so that the "-" (which
        # should be of the lowest priority) is not able to kick out from the operators the actual
        # "(" which should be kicked out as the last element
        bodmas = {"(": 0, "-": 1, "+": 2, "*": 3, "/": 4, "^": 5}
        stack = []
        operators = []

        for element in s:
            # deal first with the parenthesis
            if element == "(":
                operators.append(element)
            elif element == ")":
                while operators[-1] != "(":
                    stack.append(operators.pop(-1))
                operators.pop(-1)

            elif element not in bodmas:
                stack.append(element)
            else:
                # here we need the correct ordering of the operators
                if operators:
                    if bodmas[operators[-1]] < bodmas[element]:
                        operators.append(element)
                    else:
                        while operators and bodmas[operators[-1]] >= bodmas[element]:
                            stack.append(operators.pop(-1))
                        operators.append(element)
                else:
                    # if the operators list is empty, simply append the element
                    operators.append(element)

        while operators:  # if there is still some operators left in the operators list, add them to the stack, at the end
            stack.append(operators.pop())

        return "".join(stack)


#################
### TEST CASE ###
#################

# s = "a+b/c*d-e"  # expected output: "abc/d*+e-"

# solution = SolutionInfixPostfix()
# print(solution.from_infix_to_postfix_notation(s=s))


########################################
### Evaluate Reverse Polish Notation ###
########################################


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        You are given an array of strings tokens that represents an arithmetic expression
        in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the value of the expression.

        Note that:

        - The valid operators are '+', '-', '*', and '/'.
        - Each operand may be an integer or another expression.
        - The division between two integers always truncates toward zero.
        - There will not be any division by zero.
        - The input represents a valid arithmetic expression in a reverse polish notation.
        - The answer and all the intermediate calculations can be represented in a 32-bit integer.

        Parameters
        ----------
        tokens : List[str]
            An array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation

        Returns
        -------
        int
            The result of the arithmetic operations between operands and operators.

        Examples
        --------
        Example 1:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9

        Example 2:
        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6

        Example 3:
        Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        Output: 22
        Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22
        """
        bodmas = ["-", "+", "*", "/", "^"]
        stack = []

        for token in tokens:
            if token not in bodmas:
                stack.append(int(token))
            else:
                # pop the last two elements
                last_element = stack.pop(-1)
                previous_to_last = stack.pop(-1)
                # evaluate them and append the result to the stack again
                if token == "+":
                    stack.append(int(previous_to_last + last_element))
                elif token == "*":
                    stack.append(int(previous_to_last * last_element))
                elif token == "/":
                    stack.append(int(previous_to_last / last_element))
                elif token == "-":
                    stack.append(int(previous_to_last - last_element))
                else:
                    stack.append(int(previous_to_last**last_element))

        return stack[0]


#################
### TEST CASE ###
#################

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

solution = Solution()
print(solution.evalRPN(tokens=tokens))
