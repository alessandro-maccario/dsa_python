class Solution(object):
    def lastStoneWeight(self, stones):
        """
        You are given an array of integers stones where stones[i] is the weight of the ith stone.

        We are playing a game with the stones. On each turn, we choose the heaviest two stones and
        smash them together. Suppose the heaviest two stones have weights x and y with x <= y.
        The result of this smash is:

        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
        At the end of the game, there is at most one stone left.

        Return the weight of the last remaining stone. If there are no stones left, return 0.

        The solution uses a max-heap data structure (negated min-heap).

        Parameters
        ----------
        stones: List[int]
            List of integers representing stones.

        Return
        ------
        int
            The weight of the last remaining stone.

        Examples
        --------
        Example 1:
        Input: stones = [2,7,4,1,8,1]
        Output: 1

        Explanation:
        We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

        Example 2:
        Input: stones = [1]
        Output: 1
        """
        import heapq

        # 1. Negate all elements so that, once heapified, the biggest (negative) values will be at the top
        stones = [(-1) * stone for stone in stones]

        # 2. Heapify the list
        heapq.heapify(stones)

        while len(stones) > 1:
            # 3. Grab the first two biggest elements, negate them again (to get the actual original value),
            # then subtract the highest one to the second highest one
            first_bigger = heapq.heappop(stones)  # pop the first biggest element
            second_biggest = heapq.heappop(stones)  # pop the second biggest element
            # Calculate the difference
            diff = ((first_bigger * (-1)) - (second_biggest * (-1))) * (-1)

            # Add the recalculated element to the list
            heapq.heappush(stones, diff)

        else:
            return stones[0] * (-1)


#################
### TEST CASE ###
#################

stones = [2, 7, 4, 1, 8, 1]

solution = Solution()
print(solution.lastStoneWeight(stones=stones))
