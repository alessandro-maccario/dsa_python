from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Remove any occurrences of the val searched in the Linked List.

        Parameters
        ----------
        head : Optional[ListNode]
            Entry point of the Linked List.
        val : int
            Value(s) to be searched and removed.

        Returns
        -------
        Optional[ListNode]
            The original Linked List without the removed value.
        """
        # edge case: empty list
        if not head:
            return head

        # use a dummy node to be inserted before the original head.
        # It handles the edge case where the head itself needs to be removed
        dummy = ListNode(val=0, next=head)

        previous_node = dummy

        while previous_node.next:  # while the next value is not None
            print(f"Previous node next is {previous_node.next.val}")
            if previous_node.next.val != val:
                previous_node = previous_node.next
            else:
                previous_node.next = previous_node.next.next

        return dummy.next

    def traverse(self, head):
        current_node = head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("null")


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

# Create pointers
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

# create instance of the class
# pass the entire existing node chain as the head so that any changes will be flowing on the same LinkedList

Solution().removeElements(head=node1, val=6)
print(Solution().traverse(head=node1))
