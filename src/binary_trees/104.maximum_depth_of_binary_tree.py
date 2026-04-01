# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        Given the root of a binary tree, return its maximum depth.

        A binary tree's maximum depth is the number of nodes along the
        longest path from the root node down to the farthest leaf node.

        Use of DFS with iterative approach (stack).

        Parameters
        ----------
        root: TreeNode
            A TreeNode object.

        Returns
        -------
        int
            The maximum depth of the Tree.

        Examples
        --------
        Example 1
        Input: root = [3,9,20,null,null,15,7]
        Output: 3

        Example 2:
        Input: root = [1,null,2]
        Output: 2
        """
        # Base Condition: if the Tree is None or empty, there is no depth
        if not root:
            return 0

        stack = [[root, 1]]
        running_max = 0

        # Create first Tree list representation
        while stack:
            node, node_depth = stack.pop()

            # Check if the current depth is higher than the max so far found
            if node_depth > running_max:
                running_max = node_depth

            # Always append the node with their current depth
            if node.right:
                stack.append([node.right, node_depth + 1])

            if node.left:
                stack.append([node.left, node_depth + 1])

        return running_max


#################
### TEST CASE ###
#################

# root = [1, 2, 2, None, 3, None, 3]
root = [3, 9, 20, None, None, 15, 7]
# root = []

# Create the Tree
root = TreeNode(3)

# Assign the pointers
root.left = TreeNode(9)
root.right = TreeNode(20)

root.left.left = None
root.left.right = None

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


solution = Solution()
print(solution.maxDepth(root=root))
