from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        """
        You are given a string s of lowercase English letters and an array widths denoting how many
        pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a',
        widths[1] is the width of 'b', and so on.

        You are trying to write s across several lines, where each line is no longer than 100 pixels.
        Starting at the beginning of s, write as many letters on the first line such that the total
        width does not exceed 100 pixels.
        Then, from where you stopped in s, continue writing as many letters as you can on the second line.

        Continue this process until you have written all of s.

        Parameters
        ----------
        widths : List[int]
            An array widths denoting how many pixels wide each lowercase English letter is.
        s : str
            A string s of lowercase English letters.

        Returns
        -------
        List[int]
            Return an array result of length 2 where:
                - result[0] is the total number of lines.
                - result[1] is the width of the last line in pixels.

        Examples
        --------

        Example 1:
        Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
        Output: [3,60]
        Explanation: You can write s as follows:
        abcdefghij  // 100 pixels wide
        klmnopqrst  // 100 pixels wide
        uvwxyz      // 60 pixels wide
        There are a total of 3 lines, and the last line is 60 pixels wide.

        Example 2:
        Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
        Output: [2,4]
        Explanation: You can write s as follows:
        bbbcccdddaa  // 98 pixels wide
        a            // 4 pixels wide
        There are a total of 2 lines, and the last line is 4 pixels wide.
        """
        # count how many lines you are creating
        line_counter = 0
        # value in width pixel of the line: if > 100, next line will be saved into current lines
        current_val_line = 0

        for letter in s:
            current_val_line += widths[ord(letter) - ord("a")]

            if current_val_line <= 100:
                continue
            else:
                # count the number of lines created so far
                line_counter += 1

                # access directly the index at which the current letter has the corresponding value
                current_val_line = widths[ord(letter) - ord("a")]

        line_counter += 1

        return [line_counter, current_val_line]


widths = [
    4,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
]

s = "bbbcccdddaaaaaaa"
solution = Solution()
print(solution.numberOfLines(widths=widths, s=s))
