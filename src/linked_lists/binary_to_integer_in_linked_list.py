from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        Given head which is a reference node to a singly-linked list.
        The value of each node in the linked list is either 0 or 1.
        The linked list holds the binary representation of a number.

        Parameters
        ----------
        head : Optional[ListNode]
            The head of the linked list.

        Returns
        -------
        int
            The decimal representation of the binary values from the linked list.

        Examples
        --------

        Example 1
        Input: head = [1,0,1]
        Output: 5
        Explanation: (101) in base 2 = (5) in base 10

        Example 2
        Input: head = [0]
        Output: 0
        """
        current = head
        # use a string to store the binary elements of the linked list
        binary_to_string = ""

        while current:
            binary_to_string += str(current.val)
            current = current.next

        return int(binary_to_string, 2)


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
    print(values)


# Create test cases
head1 = create_linked_list([1, 0, 1])
# print(print_linked_list(head=head1))

# Test your solution
solution = Solution()
print(solution.getDecimalValue(head1))
