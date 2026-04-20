class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    def remove_duplicates(self):
        """Remove duplicates from linked list."""
        already_seen = set()

        slow = self.head
        # if empty list, just return the empty list
        if slow is None:
            return

        # add the head value to the set to have the first element in
        already_seen.add(self.head.value)

        while slow is not None:
            # print("slow: ", slow.value)  # , slow.next.value
            if slow.next is not None:
                if slow.next.value not in already_seen:
                    already_seen.add(slow.next.value)
                    slow = slow.next
                else:
                    slow.next = slow.next.next
            else:
                break

        return


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")


# NOTE: PASS
# Test 1: List with no duplicates
print("### -> TEST 1")
ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])
print("--------")

# NOTE: PASS
# Test 2: List with some duplicates
print("### -> TEST 2")
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])
print("--------")

# BUG: it fails here
# Test 3: List with all duplicates
print("### -> TEST 3")
ll = LinkedList(1)
ll.append(1)
ll.append(1)
# ll.append(54)
# ll.append(2)
test_remove_duplicates(ll, [1])
print("--------")


# NOTE: PASS
# # Test 4: List with consecutive duplicates
print("### -> TEST 4")
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])
print("--------")

# NOTE: PASS
# # Test 5: List with non-consecutive duplicates
print("### -> TEST 5")
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])
print("--------")

# NOTE: PASS
# # Test 6: List with duplicates at the end
print("### -> TEST 6")
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])
print("--------")

# NOTE: PASS
# # Test 7: Empty list
print("### -> TEST 7")
ll = LinkedList(None)
ll.head = None  # Directly setting the head to None
ll.length = 0  # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])
print("--------")
