"""
NGE: Next Greater Element Problem Set
"""

from typing import List


class Solution:
    def buildingWithOceanView(self, buildings: List[int]) -> List[int]:
        """
        Given a list of integer values representing a line of buildings, find the ones that have a
        view to the ocean on their right side.

        This creates a monothonically decreasing stack of elements that,
        on their right side do not have any bigger element then them.

        Parameters
        ----------
        buildings : List[int]
            A list of integer values that represent buildings.

        Returns
        -------
        List[int]
            Return the highest buildings that, on their right side do have an ocean view because no other biggger building is available.

        Examples
        --------
        buildings = [1, 3, 2, 5, 4, 1, 3]
        output = [3, 4, 6] -> index-wise
        """
        # building with an ocean view stack
        bwow_stack = []

        for idx, building in enumerate(buildings):
            if idx == 0:
                bwow_stack.append(idx)
            else:
                while bwow_stack and buildings[idx] >= buildings[bwow_stack[-1]]:
                    # remove the previous lower building and add the taller one
                    bwow_stack.pop(-1)

                bwow_stack.append(idx)

        return bwow_stack


#################
### TEST CASE ###
#################

buildings = [1, 3, 2, 5, 4, 1, 3]

solution = Solution()
print(solution.buildingWithOceanView(buildings=buildings))
