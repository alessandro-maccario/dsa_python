import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        Create a min-heap and push the elements from nums to it.

        Parameters
        ----------
        k: int
            It represents the k-th largest element of the list.

        Return
        ------
        int
            Return the kth largest element of the min-heap.

        Examples
        --------
        Example 1:
        Input:
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

        Output: [null, 4, 5, 5, 8, 8]

        Explanation:
        KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        kthLargest.add(3); // return 4
        kthLargest.add(5); // return 5
        kthLargest.add(10); // return 5
        kthLargest.add(9); // return 8
        kthLargest.add(4); // return 8

        Example 2:
        Input:
        ["KthLargest", "add", "add", "add", "add"]
        [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

        Output: [null, 7, 7, 7, 8]

        Explanation:
        KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
        kthLargest.add(2); // return 7
        kthLargest.add(10); // return 7
        kthLargest.add(9); // return 7
        kthLargest.add(9); // return 8
        """
        self.k = k
        self.min_heap = []

        # add each element to the
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        Add a new value to the stream and return the kth largest element.

        The min-heap maintains exactly k elements (the k largest seen so far).
        The root of the min-heap is always the kth largest element.

        Parameters
        ----------
        val: int
            The new value to add to the stream.

        Returns
        -------
        k
            The kth largest element after adding the new value.
        """
        # push new element to the min_heap and rebalance the tree
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            # pop the smallest element of the heap
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


#################
### TEST CASE ###
#################

k = 3
nums = [4, 5, 8, 2]

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
val = 5
param_1 = obj.add(val)
print(param_1)
