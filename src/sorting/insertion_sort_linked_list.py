from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Apply the insertion sort algorithm on a Linked List.

        Parameters
        -------
            head: Optional[ListNode]
                An unsorted ListNode object.

        Returns
        -------
            Optional[ListNode]
                A sorted ListNode object.

        References
        ----------
        - https://www.youtube.com/watch?v=Kk6mXAzqX3Y
        """
        # if head is either missing (empty Linked List) or head.next is None (so the head is the only element), then return the head object
        # Edge case: if the list is empty or has only one node, it's already sorted
        if head is None or head.next is None:
            return head

        # Create a dummy node to apply the same insertion conept to each and every element.
        # If no dummy node would be added at the start of the Linked List, and you would want to insert
        # a value before the head, you would need to treat the insertion differently compared to an insertion
        # in any other part of the list.

        # Create a dummy node that represents the head itself.
        # previous: tracks the last node in the sorted portion
        # current: points to the current node being processed
        dummy = ListNode(val=head, next=head)
        previous, current = head, head.next

        while current:
            # edge case: if the current node is already greater/equal than the previous node, the element in
            # the list is already at the right position
            if current.val >= previous.val:
                previous, current = current, current.next
                continue

            # move the current in the previous position than the previous
            temp = dummy

            while current.val > temp.next.val:
                temp = temp.next

            # if we have found a spot where to insert our next value, then:
            previous.next = current.next  # let's save what is the next position
            # let's actually move the element in between the previous elements
            current.next = (
                temp.next
            )  # the previous temp.next will be the current.next pointer
            temp.next = current  # let's assign the temp.next pointer to the current
            # now, advance the current pointer
            current = previous.next  # pointer that we save in the previous steps so that the current element can point to the next one

        return dummy.next  # which will always point to the head


# Create nodes
node1 = ListNode(7)
node2 = ListNode(11)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(9)

# Create pointers
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# create instance of the class
# pass the entire existing node chain as the head so that any changes will be flowing on the same LinkedList
linked_list = Solution().insertionSortList(head=node1)
print(linked_list)
