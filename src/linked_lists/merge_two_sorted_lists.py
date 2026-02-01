from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list.
        The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.

        Parameters
        ----------
        list1 : Optional[ListNode]
            First linked list to be merged.
        list2 : Optional[ListNode]
            Second linked list to be merged.

        Returns
        -------
        Optional[ListNode]
            Merged linked lists.

        Examples
        --------

        Example 1
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

        Example 2:
        Input: list1 = [], list2 = []
        Output: []

        Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]
        """
        # dummy node to attach the rest of the nodes to it
        dummy = ListNode(val=0)
        # pointer to the first list
        pointer_1 = list1
        # pointer to the second list
        pointer_2 = list2
        # current pointer to the dummy. It will keep track of the rest of the nodes
        current = dummy

        # while both are still not None
        while pointer_1 and pointer_2:
            if pointer_1.val <= pointer_2.val:
                current.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                current.next = pointer_2
                pointer_2 = pointer_2.next
            # always keep the current moving forwards
            current = current.next

        # if one of the pointers has reached the end of the list, need to attach the other list with the already sorted value to the current
        if pointer_1 is not None:
            current.next = pointer_1
        else:
            current.next = pointer_2

        # skipping the very first dummy node, return the rest of the linked list
        return dummy.next


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
list1 = [1, 2, 4]
list2 = [1, 3, 4]
# Create linked list
ll_list1 = create_linked_list(values=list1)
ll_list2 = create_linked_list(values=list2)


# Test your solution
solution = Solution()
traverse(solution.mergeTwoLists(list1=ll_list1, list2=ll_list2))
