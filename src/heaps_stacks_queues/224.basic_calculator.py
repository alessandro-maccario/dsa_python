# continue from 1:48:25
# https://www.youtube.com/watch?v=zNgAQPlMqdg

from typing import List


class Solution:
    def from_infix_to_postfix_notation(self, s: str) -> List:
        # order of operators (brackets, order, division, multiplication, addition, subtraction)
        # The lowest priority in this case is represented by the bracket so that the "-" (which
        # should be of the lowest priority) is not able to kick out from the operators the actual
        # "(" which should be kicked out as the last element
        bodmas = {"(": 0, "+": 1, "-": 2, "*": 3, "/": 4, "^": 5}
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

        return stack  # [2, 1, 2, +, -]

    def check_unary_binary_operators(self, s) -> str:
        """
        Handle special cases of unary operators (operators that are attached to only one operand, such as -2).
        The way to handle this is to simply add, only for cases in which the operator is a "+" or a "-",
        or if the unary operator is at the beginning of the string or if it is in between a "(" and an operand
        or right after another operator.

        Parameters
        ----------
        s : _type_
            _description_

        Returns
        -------
        str
            A string where unary operators are converted to binary.

        Examples
        --------

        Example 1
        1 - (-2)

        Example 2
        (+3 + 1)

        Example 3
        +5 - 1

        Cases
        -----
        # TODO: are you covering all cases?
        - At the very start of the expression
        - Right after an opening parenthesis (
        - Right after another operator
        """
        write_output = []

        for idx, char in enumerate(s):
            print(f"idx: {idx} | char: {char}")
            if idx == 0 and char in ("+", "-"):
                # append a 0 so that the unary becomes a binary operator
                write_output.append("0")
                write_output.append(char)
            elif char == "(" and s[idx + 1] in ("+", "-"):
                write_output.append(char)
                write_output.append("0")
            elif s[idx - 1] in ("+", "-", "*", "/", "^") and char in ("+", "-"):
                write_output.append("0")
                write_output.append(char)
            else:
                write_output.append(char)

        return "".join(write_output)

    def evalRPN(self, tokens: List[str]) -> str:
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

        # Handle special cases of unary operators (operators that are attached to only one operand, such as -2).
        # The way to handle this is to simply add, only for cases in which the operator is a "+" or a "-",
        # or if the unary operator is at the beginning of the string or if it is in between a "(" and an operand
        # or right after another operator.
        # Examples:
        # 1 - (-2) | (+3 + 1) | +5 - 1

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

        return "".join(list(map(str, stack)))

    def calculate(self, s: str) -> int:
        # strip and remove spaces from input string
        s = s.strip().replace(" ", "")
        evaluate = self.evalRPN(tokens=self.from_infix_to_postfix_notation(s=s))
        return int(evaluate)


#################
### TEST CASE ###
#################

s = "1-(     -2)"

solution = Solution()
print(solution.calculate(s=s))
