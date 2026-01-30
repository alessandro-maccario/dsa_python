from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

        Parameters
        ----------
        head : Optional[ListNode]
            The head of the linked list.

        Returns
        -------
        bool
            True if the linked list is a Palindrome. False otherwise.

        Examples
        --------
        Example 1
        Input: head = [1,2,2,1]
        Output: true

        Example 2
        Input: head = [1,2]
        Output: false

        Explanation
        -----------
        The solution works in three steps:

        1. reach the half of the linked list with slow pointer
        2. reverse the second half of the linked list
        3. compare each values together to see if the two linked lists contain the same values
        """
        # 1. Create the slow and fast pointer
        slow_pointer = head
        fast_pointer = head.next

        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
        #     print(
        #         f"Slow pointer: {slow_pointer.val} | Fast Pointer: {fast_pointer.val if fast_pointer else None}"
        #     )
        # print("-------------")

        # 2. Reverse the second half
        previous = None
        current = slow_pointer.next

        while current:
            temp = current.next  # save reference to the next node
            current.next = (
                previous  # reverse the reference of the current.next to the previous
            )
            previous, current = current, temp  # move the pointers forward

        # print("Show the reversed linked list:\n")
        # # Print the entire linked list as a list
        # while previous:
        #     print(previous.val, end=" -> ")
        #     previous = previous.next
        # print("None")  # Prints: 1 -> 2 -> None
        # print("---------------")
        # print(current)
        # print("---------------")

        # 3. Compare the two linked lists
        while previous:  # which is the reversed second half of the linked list
            if (
                previous.val != head.val
            ):  # if any values do not match, exit and return False
                return False
            # move the pointers forward
            previous, head = previous.next, head.next

        # If all the values match, then return True
        return True


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
head1 = create_linked_list([1, 2, 3, 2, 1])  # Palindrome
# print(print_linked_list(head=head1))

# Test your solution
solution = Solution()
print(solution.isPalindrome(head1))  # Should return True
