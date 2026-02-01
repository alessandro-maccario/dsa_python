from typing import List
from operator import itemgetter


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        You are given an integer array coordinates, coordinates[i] = [x, y],
        where [x, y] represents the coordinate of a point.
        Check if these points make a straight line in the XY plane.

        Parameters
        ----------
        coordinates : List[List[int]]
            List of lists containing coordinates.

        Returns
        -------
        bool
            True if the line is a straight line, otherwise False.

        Examples
        --------

        Example 1
        Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
        Output: true

        Example 2
        Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        Output: false
        """

        # check if it is a straing vertical line -> (itemgetter, 0) with map will get all the value at index 1 of the list of lists. If the len(set) == 1 it means all of the values are duplicates
        vertical_line = len(set(list(map(itemgetter(0), coordinates)))) == 1
        # check if it is a horizontal line -> (itemgetter, 1) with map will get all the value at index 1 of the list of lists. If the len(set) == 1 it means all of the values are duplicates
        horizontal_line = len(set(list(map(itemgetter(1), coordinates)))) == 1

        if vertical_line or horizontal_line:
            return True

        # check first slope
        y_2 = coordinates[1][1]
        y_1 = coordinates[0][1]
        x_2 = coordinates[1][0]
        x_1 = coordinates[0][0]
        # calculate the reference slope of the first two element, then compare this slope with the rest of the available coordinates
        # precompute the numerator/denominator. If one of these two is equal to 0, then we have a vertical line/horizontal line, therefore there is no slope
        numerator = y_2 - y_1
        denominator = x_2 - x_1
        if numerator == 0 or denominator == 0:
            return False
        reference_m_slope = numerator / denominator

        # for each subsequent sublist, keep the first as a reference and calculate the slope to see if they match with the reference slope
        for each_sublist in coordinates[1:]:
            # precompute the numerator/denominator. If one of these two is equal to 0, then we have a vertical line/horizontal line, therefore there is no slope
            numerator = each_sublist[1] - y_1
            denominator = each_sublist[0] - x_1

            # If one of these two is equal to 0, then we have a vertical line/horizontal line, not a slope
            if numerator == 0 or denominator == 0:
                return False

            m_slope = (each_sublist[1] - y_1) / (each_sublist[0] - x_1)
            if m_slope != reference_m_slope:
                return False

        return True


# Test solution
solution = Solution()
coordinates = [[0, 0], [0, 5], [5, 5], [5, 0]]
print(solution.checkStraightLine(coordinates=coordinates))
