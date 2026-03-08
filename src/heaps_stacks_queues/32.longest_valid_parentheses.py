class Solution:
    def longestValidParentheses(self, s: str) -> int:

        valid_idx = []
        final_valid_idx = []

        # first loop: create the valid indexes list
        for idx, par in enumerate(s):
            if par == "(":
                valid_idx.append(idx)
            else:
                if valid_idx:  # if not empty
                    valid_pop = valid_idx.pop(-1)
                    final_valid_idx.append(valid_pop)
                    final_valid_idx.append(idx)

        current_streak = 1
        max_streak = 0
        # loop through the valid indexes list and check if there is a gap > 1 between indexes:
        # if yes, it means that there is a gap in the continuity between valid braces
        if not final_valid_idx:
            return 0

        # sort before checking the indexes, needed for the correct check of the next - previous value
        final_valid_idx.sort()
        for idx in range(len(final_valid_idx) - 1):
            if final_valid_idx[idx + 1] - final_valid_idx[idx] == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                # reset the current streak to the first group of valid braces that you can find
                current_streak = 1
                max_streak = max(max_streak, current_streak)

        max_streak = max(max_streak, current_streak)

        return max_streak


#################
### TEST CASE ###
#################

s = "()(())"

solution = Solution()
print(solution.longestValidParentheses(s=s))
