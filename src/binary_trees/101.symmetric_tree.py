# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        Given the root of a binary tree, check whether it is a mirror of itself
        (i.e., symmetric around its center).

        Parameters
        ----------
        root: TreeNode
            A TreeNode object.

        Return
        ------
        bool
            True if the Tree is symmetric. False if it is not.

        Examples
        --------

        Example 1
        Input: root = [1,2,2,3,4,4,3]
        Output: true

        Example 2
        Input: root = [1,2,2,null,3,null,3]
        Output: false
        """
        from collections import deque

        # base cases
        if root is None:  # if the root itself is None, it is symmetric to itself
            return True

        # add the first two elements
        queue = deque([root.left, root.right])

        # core of the algorithm
        while queue:
            # get the left and right element and compare them. If they represents the same value
            left_node, right_node = queue.popleft(), queue.popleft()

            if left_node is None and right_node is not None:
                # if they are the same, no need just keep processing the rest of the nodes
                return False
            if left_node is not None and right_node is None:
                return False
            if left_node is None and right_node is None:
                continue
            if left_node.val == right_node.val:
                # append values
                queue.append(left_node.left)
                queue.append(right_node.right)
                queue.append(left_node.right)
                queue.append(right_node.left)
                continue
            else:
                return False

        return True


#################
### TEST CASE ###
#################

root = [1, 2, 2, None, 3, None, 3]

# Create the Tree
root = TreeNode(1)

# Assign the pointers
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = None
root.left.right = TreeNode(3)

root.right.left = None
root.right.right = TreeNode(3)


solution = Solution()
print(solution.isSymmetric(root=root))
