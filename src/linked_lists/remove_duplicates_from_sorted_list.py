from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
        Return the linked list sorted as well.

        Parameters
        ----------
        head : Optional[ListNode]
            The reference pointer to the linked list.

        Returns
        -------
        Optional[ListNode]
            Return the linked list without duplicates and sorted as well.

        Examples
        --------

        Example 1
        Input: head = [1,1,2]
        Output: [1,2]

        Example 2
        Input: head = [1,1,2,3,3]
        Output: [1,2,3]

        """
        # edge case if head is None
        if head is None:
            return None

        # Pointer 1 waits until Pointer 2 changes, then it bridges the current node with the next one to remove duplicates
        pointer_1 = head
        # Pointer 2 keeps moving until the values are matching Pointer 1
        pointer_2 = head.next

        while pointer_2:
            if pointer_1.val == pointer_2.val:
                # as long as the values are the same, keep moving the second scanning pointer
                pointer_2 = pointer_2.next
            else:
                pointer_1.next = pointer_2
                pointer_1 = pointer_2

        # after traversing the list, connect the current pointer_1 to the None that pointer_2 has reached
        pointer_1.next = pointer_2

        return head


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
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print("Linked List: ", values)


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
# expect a linked list without duplicates and sorted asc
head1 = create_linked_list([1, 1, 2])
print_linked_list(head=head1)
# # Test your solution
solution = Solution()
solution.deleteDuplicates(head1)
traverse(head=head1)
