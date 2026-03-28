# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical,
        and the nodes have the same value.

        Parameters
        ----------
        p: Optional[TreeNode]
            First Tree
        q: Optional[TreeNode]
            Second Tree

        Returns
        -------
        bool
            Return True if both Trees are the same. Else, return False.

        Examples
        --------

        Example 1
        Input: p = [1,2,3], q = [1,2,3]
        Output: true

        Example 2
        Input: p = [1,2], q = [1,null,2]
        Output: false

        Example 3
        Input: p = [1,2,1], q = [1,1,2]
        Output: false
        """

        stack_tree_1 = [p]
        output_tree_1 = []
        stack_tree_2 = [q]
        output_tree_2 = []

        # Base conditions
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        # Create first Tree list representation
        while stack_tree_1:
            node_tree_1 = stack_tree_1.pop(-1)
            output_tree_1.append(node_tree_1)

            if node_tree_1:
                if node_tree_1.right:
                    stack_tree_1.append(node_tree_1.right)
                else:
                    stack_tree_1.append(None)
                if node_tree_1.left:
                    stack_tree_1.append(node_tree_1.left)
                else:
                    stack_tree_1.append(None)

        # Create second Tree list representation
        while stack_tree_2:
            node_tree_2 = stack_tree_2.pop(-1)
            output_tree_2.append(node_tree_2)

            if node_tree_2:
                if node_tree_2.right:
                    stack_tree_2.append(node_tree_2.right)
                else:
                    stack_tree_2.append(None)
                if node_tree_2.left:
                    stack_tree_2.append(node_tree_2.left)
                else:
                    stack_tree_2.append(None)

        # Convert the memory allocation to actual values is not None
        output_tree_1 = [
            value.val if value is not None else None for value in output_tree_1
        ]
        output_tree_2 = [
            value.val if value is not None else None for value in output_tree_2
        ]

        # Compare the output of the first tree with the output of the second tree.
        # If they match, return True; if they do not match, return False
        return output_tree_1 == output_tree_2


#################
### TEST CASE ###
#################

# Tree 1
p = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)

# Tree 2
q = TreeNode(1)
D = TreeNode(2)
E = TreeNode(3)


# Assign the pointers
p.left, p.right = B, C
q.left, q.right = D, E


solution = Solution()
print(solution.isSameTree(p=p, q=q))
