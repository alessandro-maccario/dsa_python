class Solution(object):
    def kClosest(self, points, k):
        """
        Given an array of points where points[i] = [xi, yi] represents a point on the
        X-Y plane and an integer k, return the k closest points to the origin (0, 0).

        The distance between two points on the X-Y plane is the Euclidean
        distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

        You may return the answer in any order.
        The answer is guaranteed to be unique (except for the order that it is in).

        Parameters
        ----------
        points: List[int]
            Array of points.
        k: int
            k closest points to the origin (0, 0).

        Examples
        --------
        Example 1
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]

        Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

        Example 2:
        Input: points = [[3,3],[5,-1],[-2,4]], k = 2
        Output: [[3,3],[-2,4]]

        Explanation: The answer [[-2,4],[3,3]] would also be accepted.
        """
        import heapq

        heap = []
        output = []

        for point in points:
            # Calculate the Euclidean distance between the point and the origin (as the origin is anyway
            # (0,0), no need to be added in here)
            dist = (point[0]) ** 2 + (point[1]) ** 2

            # Add the point and the distance value to the heap using a tuple.
            # The next comparison will work on the first element of each tuple which is the distance
            # Keep the heap invariant.
            heapq.heappush(heap, (dist, point))

        for i in range(k):
            # pop the minimum element from the heap and get the corresponding point from the original points
            # list. Then add it to the output list
            pop_min_heap_element = heapq.heappop(heap)
            # Add the smallest point tuple to the list
            output.append(pop_min_heap_element[1])

        return output


#################
### TEST CASE ###
#################

k = 1
points = [[1, 3], [-2, 2]]

k = 2
points = [[3, 3], [5, -1], [-2, 4]]

solution = Solution()
print(solution.kClosest(points=points, k=k))
