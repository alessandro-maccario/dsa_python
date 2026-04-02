# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        Given a binary tree, determine if it is height-balanced.
        A height-balanced binary tree is a binary tree in which the depth of the
        two subtrees of every node never differs by more than one.

        Parameters
        ----------
        root: object
            The TreeNode root.

        Returns
        -------
        bool
            True if the tree is balanced. False otherwise.


        Approach using DFS Post order Traversal:
        Left -> Right -> Root

        Examples
        --------
        Example 1
        Input: root = [3,9,20,null,null,15,7]
        Output: true

        Example 2
        Input: root = [1,2,2,3,3,null,null,4,4]
        Output: false

        Example 3
        Input: root = []
        Output: true
        """
        # A list can be modified from an enclosed function, but not a bool. Therefore the usage of the list
        balanced = [True]

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            if balanced[0] is False:
                return 0

            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]


#################
### TEST CASE ###
#################

# root = [1, 2, 2, None, 3, None, 3]
root = [3, 9, 20, None, None, 15, 7]

root = []

# # Create the Tree
# root = TreeNode(3)

# # Assign the pointers
# root.left = TreeNode(9)
# root.right = TreeNode(20)

# root.left.left = None
# root.left.right = None

# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = [1, 2, 2, 3, 3, None, None, 4, 4]

# Create the Tree
root = TreeNode(1)

# Assign the pointers
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(3)

root.right.left = None
root.right.right = None

root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)


solution = Solution()
print(solution.isBalanced(root=root))
