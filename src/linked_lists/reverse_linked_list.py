"""
Reference
---------
- https://algo.monster/liteproblems/234
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, return the reverse linked list.

        Parameters
        ----------
        head : Optional[ListNode]
            The head of the linked list.

        Returns
        -------
        head : Optional[ListNode]
            The original linked list in reverse order.

        Examples
        --------
        Example 1
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Example 2
        Input: head = [1,2]
        Output: [2,1]

        Example 3:
        Input: head = []
        Output: []
        """
        # 1. Reverse the linked list
        previous = None
        current = head

        while current:
            temp = current.next  # save reference to the next node
            current.next = (
                previous  # reverse the reference of the current.next to the previous
            )
            previous, current = current, temp  # move the pointers forward

        return previous


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to print a linked list (useful for debugging)
def traverse(head):
    """
    Traverse the list and display it.
    """
    current_node = head

    while current_node:
        print(current_node.val, end=" -> ")
        current_node = current_node.next

    print("null")


# Create test cases
list1 = [1, 2, 4, 8, 9, 10]
# Create linked list
ll_list1 = create_linked_list(values=list1)


# Test your solution
solution = Solution()
traverse(solution.reverseList(head=ll_list1))
